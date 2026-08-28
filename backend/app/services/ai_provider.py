"""
AI Provider Abstraction Layer.
Provides a unified interface for AI-assisted evidence detection.
Supports OpenAI (GPT-4o-mini) and Google Gemini.
"""

import json
import logging
from abc import ABC, abstractmethod
from typing import Any

from app.config import settings

logger = logging.getLogger(__name__)


class AIProvider(ABC):
    """Abstract base class for AI providers."""

    @abstractmethod
    async def analyze_evidence(
        self,
        role_category: str,
        level: str,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        """
        Analyze filtered repo data for evidence of specific subskills.

        Args:
            role_category: The role being evaluated (e.g., "game-dev")
            level: Target level (junior/mid/senior)
            target_subskills: List of composite keys to look for
            filtered_data: Dict with file contents, dependencies, etc.

        Returns:
            {composite_key: {"status": "evidence_found"|"not_yet_evidenced",
                             "evidence_sources": [...],
                             "quality_notes": str}}
        """
        pass

    def _build_system_prompt(self, role_category: str, level: str) -> str:
        """Build the system prompt for evidence analysis."""
        return f"""You are a technical skill evaluator analyzing GitHub repository code.
Your task is to determine whether specific subskills are evidenced in the provided code.

Role: {role_category}
Level: {level}

RULES:
1. You ONLY detect evidence — you do NOT assign scores or ratings.
2. For each subskill, report "evidence_found" or "not_yet_evidenced".
3. If evidence is found, list the specific files and code patterns that prove it.
4. Be conservative — only mark "evidence_found" if there is clear, concrete usage.
5. Mentioning a technology in README without code usage is NOT strong evidence.
6. Return VALID JSON only."""

    def _build_user_prompt(
        self,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
    ) -> str:
        """Build the user prompt with filtered data."""
        prompt_parts = [
            "Analyze the following repository data and determine evidence for each subskill.\n",
            "## Target Subskills (composite keys):",
            json.dumps(target_subskills, indent=2),
            "\n## Repository Data:",
        ]

        # Add file contents
        files = filtered_data.get("file_contents", {})
        if files:
            prompt_parts.append("\n### File Contents:")
            for path, content in files.items():
                # Truncate large files
                truncated = content[:2000] if len(content) > 2000 else content
                prompt_parts.append(f"\n#### {path}\n```\n{truncated}\n```")

        # Add dependencies
        deps = filtered_data.get("dependencies", {})
        if deps:
            prompt_parts.append(f"\n### Dependencies:\n{json.dumps(deps, indent=2)}")

        # Add README
        readme = filtered_data.get("readme", "")
        if readme:
            prompt_parts.append(f"\n### README:\n{readme[:1500]}")

        # Output format instruction
        prompt_parts.append("""
## Required Output Format (JSON):
{
  "subskill_key": {
    "status": "evidence_found" | "not_yet_evidenced",
    "evidence_sources": ["file:line → pattern"],
    "quality_notes": "brief note"
  }
}""")

        return "\n".join(prompt_parts)


class OpenAIProvider(AIProvider):
    """OpenAI GPT-4o-mini implementation."""

    def __init__(self):
        try:
            from openai import AsyncOpenAI
            self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
            self.model = settings.OPENAI_MODEL
        except ImportError:
            raise RuntimeError("openai package not installed. Run: pip install openai")

    async def analyze_evidence(
        self,
        role_category: str,
        level: str,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._build_system_prompt(role_category, level)},
                    {"role": "user", "content": self._build_user_prompt(target_subskills, filtered_data)},
                ],
                response_format={"type": "json_object"},
                temperature=0.1,
                max_tokens=4096,
            )

            content = response.choices[0].message.content
            return json.loads(content) if content else {}
        except Exception as e:
            logger.error(f"OpenAI analysis failed: {e}")
            return {}


class GeminiProvider(AIProvider):
    """Google Gemini implementation."""

    def __init__(self):
        try:
            import google.generativeai as genai
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel(settings.GEMINI_MODEL)
        except ImportError:
            raise RuntimeError("google-generativeai package not installed. Run: pip install google-generativeai")

    async def analyze_evidence(
        self,
        role_category: str,
        level: str,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        try:
            full_prompt = (
                self._build_system_prompt(role_category, level)
                + "\n\n"
                + self._build_user_prompt(target_subskills, filtered_data)
            )

            response = await self.model.generate_content_async(
                full_prompt,
                generation_config={
                    "response_mime_type": "application/json",
                    "temperature": 0.1,
                    "max_output_tokens": 4096,
                },
            )

            return json.loads(response.text) if response.text else {}
        except Exception as e:
            logger.error(f"Gemini analysis failed: {e}")
            return {}


class NoOpProvider(AIProvider):
    """No-op provider when AI is disabled. Returns empty results."""

    async def analyze_evidence(
        self,
        role_category: str,
        level: str,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        logger.info("AI provider disabled — using keyword-only detection")
        return {}


def get_ai_provider() -> AIProvider:
    """Factory function to get the configured AI provider."""
    provider = settings.AI_PROVIDER.lower()

    if provider == "openai":
        return OpenAIProvider()
    elif provider == "gemini":
        return GeminiProvider()
    else:
        return NoOpProvider()
