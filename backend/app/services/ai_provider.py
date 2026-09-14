"""
AI Provider Abstraction Layer.
Provides a unified interface for AI-assisted evidence detection.
Production-ready OpenAI & Groq implementations with:
- Retry logic (exponential backoff for 429/500/timeout)
- Token budget control & prompt truncation
- Subskill chunking for large roles (>15 subskills per request)
- Response validation & structured output enforcement
- Cost tracking & logging
"""

import json
import logging
import math
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
        subskill_definitions: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, dict[str, Any]]:
        """
        Analyze filtered repo data for evidence of specific subskills.

        Args:
            role_category: The role being evaluated (e.g., "backend")
            level: Target level (junior/mid/senior)
            target_subskills: List of composite keys to look for
            filtered_data: Dict with file_contents, dependencies, readme
            subskill_definitions: Optional {composite_key: {name, description, keywords}}

        Returns:
            {composite_key: {"status": "evidence_found"|"not_yet_evidenced",
                             "evidence_sources": [...],
                             "quality_notes": str}}
        """
        pass

    def _build_system_prompt(self, role_category: str, level: str) -> str:
        """Build the system prompt for evidence analysis."""
        return f"""You are an expert technical skill evaluator analyzing GitHub repository code.
Your task is to determine whether specific developer subskills are evidenced in the provided code.

Role Category: {role_category}
Target Level: {level}

STRICT RULES:
1. You ONLY detect evidence — you NEVER assign scores, ratings, or confidence values.
2. For each subskill composite key, report exactly one of:
   - "evidence_found": Clear, concrete code usage that demonstrates the skill.
   - "not_yet_evidenced": No sufficient evidence found in the provided code.
3. If "evidence_found", you MUST list at least one specific evidence_source in format "repo/filepath → concrete pattern".
4. Be CONSERVATIVE:
   - README mentions alone are NOT sufficient evidence.
   - Import statements without actual usage are NOT sufficient evidence.
   - Configuration files count only for infrastructure/config subskills.
   - Comments or docstrings about a technology are NOT evidence of usage.
5. Evidence must match the TARGET LEVEL expectations:
   - junior: basic usage is sufficient
   - mid: applied usage with some depth
   - senior: advanced patterns, architecture-level usage
6. Return VALID JSON only. Every requested composite key MUST appear in your response."""

    def _build_user_prompt(
        self,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
        subskill_definitions: dict[str, dict[str, Any]] | None = None,
    ) -> str:
        """Build the user prompt with filtered data and subskill context."""
        prompt_parts = [
            "Analyze the following repository data for evidence of these subskills:\n",
            "## Target Subskills:\n",
        ]

        # Include subskill definitions for better AI understanding
        for ck in target_subskills:
            if subskill_definitions and ck in subskill_definitions:
                defn = subskill_definitions[ck]
                name = defn.get("name", ck)
                desc = defn.get("description", "")
                kws = defn.get("keywords", [])[:5]
                kw_str = ", ".join(kws) if kws else ""
                prompt_parts.append(f"- **{ck}**: {name} — {desc} (look for: {kw_str})")
            else:
                prompt_parts.append(f"- **{ck}**")

        prompt_parts.append("\n## Repository Data:")

        # Add file contents (already truncated by caller)
        files = filtered_data.get("file_contents", {})
        if files:
            prompt_parts.append("\n### File Contents:")
            for path, content in files.items():
                # Detect language from extension
                ext = path.rsplit(".", 1)[-1] if "." in path else ""
                lang_hint = _ext_to_lang(ext)
                truncated = content[:2000] if len(content) > 2000 else content
                prompt_parts.append(f"\n#### {path}\n```{lang_hint}\n{truncated}\n```")

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
## REQUIRED JSON Output (include ALL composite keys listed above):
{
  "composite_key": {
    "status": "evidence_found" | "not_yet_evidenced",
    "evidence_sources": ["repo/file.py → Pattern description"],
    "quality_notes": "Brief explanation of what was found or why not"
  }
}""")

        return "\n".join(prompt_parts)


def _ext_to_lang(ext: str) -> str:
    """Map file extension to markdown language hint."""
    mapping = {
        "py": "python", "js": "javascript", "ts": "typescript", "tsx": "tsx",
        "jsx": "jsx", "java": "java", "go": "go", "rs": "rust", "rb": "ruby",
        "cs": "csharp", "cpp": "cpp", "c": "c", "swift": "swift", "kt": "kotlin",
        "yaml": "yaml", "yml": "yaml", "json": "json", "toml": "toml",
        "sql": "sql", "sh": "bash", "dockerfile": "dockerfile", "proto": "protobuf",
    }
    return mapping.get(ext.lower(), "")


def _estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token for English/code."""
    return len(text) // 4


class OpenAIProvider(AIProvider):
    """
    Production-ready OpenAI GPT-4o-mini implementation.
    Features: retry, chunking, validation, cost tracking.
    """

    def __init__(self):
        try:
            from openai import AsyncOpenAI
            self.client = AsyncOpenAI(
                api_key=settings.OPENAI_API_KEY,
                timeout=settings.AI_REQUEST_TIMEOUT,
            )
            self.model = settings.OPENAI_MODEL
        except ImportError:
            raise RuntimeError("openai package not installed. Run: pip install openai")

    async def analyze_evidence(
        self,
        role_category: str,
        level: str,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
        subskill_definitions: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, dict[str, Any]]:
        """
        Analyze with automatic chunking for large subskill lists.
        Chunks ensure we stay within output token limits.
        """
        if not target_subskills:
            return {}

        chunk_size = settings.AI_SUBSKILL_CHUNK_SIZE

        # If within chunk size, single call
        if len(target_subskills) <= chunk_size:
            return await self._analyze_chunk(
                role_category, level, target_subskills, filtered_data, subskill_definitions
            )

        # Chunk and merge results
        logger.info(
            f"Chunking {len(target_subskills)} subskills into "
            f"{math.ceil(len(target_subskills) / chunk_size)} chunks of {chunk_size}"
        )
        merged: dict[str, dict[str, Any]] = {}
        for i in range(0, len(target_subskills), chunk_size):
            chunk = target_subskills[i : i + chunk_size]
            chunk_result = await self._analyze_chunk(
                role_category, level, chunk, filtered_data, subskill_definitions
            )
            merged.update(chunk_result)

        return merged

    async def _analyze_chunk(
        self,
        role_category: str,
        level: str,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
        subskill_definitions: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, dict[str, Any]]:
        """Analyze a single chunk of subskills with retry logic."""
        system_prompt = self._build_system_prompt(role_category, level)
        user_prompt = self._build_user_prompt(target_subskills, filtered_data, subskill_definitions)

        # Token budget check — truncate file contents if needed
        total_estimate = _estimate_tokens(system_prompt + user_prompt)
        if total_estimate > settings.AI_MAX_INPUT_TOKENS:
            logger.warning(
                f"Prompt too large ({total_estimate} est. tokens > {settings.AI_MAX_INPUT_TOKENS}). "
                f"Truncating file contents."
            )
            filtered_data = _truncate_data_to_budget(
                filtered_data, settings.AI_MAX_INPUT_TOKENS, system_prompt, target_subskills
            )
            user_prompt = self._build_user_prompt(target_subskills, filtered_data, subskill_definitions)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        response = await self._call_with_retry(messages)
        if response is None:
            return {}

        # Parse and validate
        raw = self._parse_response(response)
        validated = self._validate_response(raw, target_subskills)

        # Cost tracking
        self._log_cost(response)

        return validated

    async def _call_with_retry(self, messages: list[dict]) -> Any:
        """Call OpenAI API with exponential backoff retry."""
        from openai import (
            RateLimitError,
            APITimeoutError,
            APIConnectionError,
            InternalServerError,
        )
        from tenacity import (
            retry,
            stop_after_attempt,
            wait_exponential,
            retry_if_exception_type,
        )

        @retry(
            stop=stop_after_attempt(settings.AI_MAX_RETRIES),
            wait=wait_exponential(multiplier=1, min=2, max=30),
            retry=retry_if_exception_type(
                (RateLimitError, APITimeoutError, APIConnectionError, InternalServerError)
            ),
            before_sleep=lambda rs: logger.warning(
                f"OpenAI retry #{rs.attempt_number} after {type(rs.outcome.exception()).__name__}"
            ),
        )
        async def _do_call():
            return await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.1,
                max_tokens=settings.AI_MAX_OUTPUT_TOKENS,
            )

        try:
            return await _do_call()
        except Exception as e:
            logger.error(f"OpenAI call failed after retries: {type(e).__name__}: {e}")
            return None

    def _parse_response(self, response: Any) -> dict:
        """Extract and parse JSON from OpenAI response."""
        try:
            content = response.choices[0].message.content
            if not content:
                logger.warning("OpenAI returned empty content")
                return {}
            return json.loads(content)
        except (json.JSONDecodeError, IndexError, AttributeError) as e:
            logger.error(f"Failed to parse OpenAI response: {e}")
            return {}

    def _validate_response(
        self, raw: dict, expected_keys: list[str]
    ) -> dict[str, dict[str, Any]]:
        """Validate AI response structure — filter invalid entries."""
        validated: dict[str, dict[str, Any]] = {}
        for key in expected_keys:
            if key not in raw:
                continue
            item = raw[key]
            if not isinstance(item, dict):
                continue

            status = item.get("status")
            if status not in ("evidence_found", "not_yet_evidenced"):
                logger.warning(f"AI returned invalid status for {key}: {status}")
                continue

            # evidence_found must have at least one source
            if status == "evidence_found":
                sources = item.get("evidence_sources", [])
                if not sources or not isinstance(sources, list):
                    logger.warning(f"AI found evidence for {key} but no valid sources")
                    continue

            validated[key] = item

        skipped = len(expected_keys) - len(validated)
        if skipped > 0:
            logger.info(f"AI response: {len(validated)} valid, {skipped} skipped/missing")

        return validated

    def _log_cost(self, response: Any) -> None:
        """Log token usage and estimated cost."""
        if not settings.AI_COST_TRACKING:
            return
        try:
            usage = response.usage
            if not usage:
                return
            prompt_tokens = usage.prompt_tokens
            completion_tokens = usage.completion_tokens
            total_tokens = usage.total_tokens
            # GPT-4o-mini pricing: $0.15/1M input, $0.60/1M output
            cost = (prompt_tokens * 0.15 / 1_000_000) + (completion_tokens * 0.60 / 1_000_000)
            logger.info(
                f"[AI Cost] model={self.model} "
                f"prompt={prompt_tokens} completion={completion_tokens} total={total_tokens} "
                f"est_cost=${cost:.6f}"
            )
        except Exception:
            pass


class GroqProvider(AIProvider):
    """
    Groq LPU implementation using OpenAI-compatible API.
    Features: sub-second inference, retry, chunking, validation, cost tracking.
    """

    def __init__(self):
        try:
            from openai import AsyncOpenAI
            self.client = AsyncOpenAI(
                api_key=settings.GROQ_API_KEY,
                base_url="https://api.groq.com/openai/v1",
                timeout=settings.AI_REQUEST_TIMEOUT,
            )
            self.model = settings.GROQ_MODEL
        except ImportError:
            raise RuntimeError("openai package not installed. Run: pip install openai")

    async def analyze_evidence(
        self,
        role_category: str,
        level: str,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
        subskill_definitions: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, dict[str, Any]]:
        """
        Analyze with automatic chunking for large subskill lists.
        Chunks ensure we stay within output token limits.
        """
        if not target_subskills:
            return {}

        chunk_size = settings.AI_SUBSKILL_CHUNK_SIZE

        # If within chunk size, single call
        if len(target_subskills) <= chunk_size:
            return await self._analyze_chunk(
                role_category, level, target_subskills, filtered_data, subskill_definitions
            )

        # Chunk and merge results
        logger.info(
            f"[Groq] Chunking {len(target_subskills)} subskills into "
            f"{math.ceil(len(target_subskills) / chunk_size)} chunks of {chunk_size}"
        )
        merged: dict[str, dict[str, Any]] = {}
        for i in range(0, len(target_subskills), chunk_size):
            chunk = target_subskills[i : i + chunk_size]
            chunk_result = await self._analyze_chunk(
                role_category, level, chunk, filtered_data, subskill_definitions
            )
            merged.update(chunk_result)

        return merged

    async def _analyze_chunk(
        self,
        role_category: str,
        level: str,
        target_subskills: list[str],
        filtered_data: dict[str, Any],
        subskill_definitions: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, dict[str, Any]]:
        """Analyze a single chunk of subskills with retry logic."""
        system_prompt = self._build_system_prompt(role_category, level)
        user_prompt = self._build_user_prompt(target_subskills, filtered_data, subskill_definitions)

        # Token budget check — truncate file contents if needed
        total_estimate = _estimate_tokens(system_prompt + user_prompt)
        if total_estimate > settings.AI_MAX_INPUT_TOKENS:
            logger.warning(
                f"[Groq] Prompt too large ({total_estimate} est. tokens > {settings.AI_MAX_INPUT_TOKENS}). "
                f"Truncating file contents."
            )
            filtered_data = _truncate_data_to_budget(
                filtered_data, settings.AI_MAX_INPUT_TOKENS, system_prompt, target_subskills
            )
            user_prompt = self._build_user_prompt(target_subskills, filtered_data, subskill_definitions)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        response = await self._call_with_retry(messages)
        if response is None:
            return {}

        # Parse and validate
        raw = self._parse_response(response)
        validated = self._validate_response(raw, target_subskills)

        # Cost tracking
        self._log_cost(response)

        return validated

    async def _call_with_retry(self, messages: list[dict]) -> Any:
        """Call Groq OpenAI-compatible API with exponential backoff retry."""
        from openai import (
            RateLimitError,
            APITimeoutError,
            APIConnectionError,
            InternalServerError,
        )
        from tenacity import (
            retry,
            stop_after_attempt,
            wait_exponential,
            retry_if_exception_type,
        )

        @retry(
            stop=stop_after_attempt(settings.AI_MAX_RETRIES),
            wait=wait_exponential(multiplier=1, min=2, max=30),
            retry=retry_if_exception_type(
                (RateLimitError, APITimeoutError, APIConnectionError, InternalServerError)
            ),
            before_sleep=lambda rs: logger.warning(
                f"Groq retry #{rs.attempt_number} after {type(rs.outcome.exception()).__name__}"
            ),
        )
        async def _do_call():
            return await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.1,
                max_tokens=settings.AI_MAX_OUTPUT_TOKENS,
            )

        try:
            return await _do_call()
        except Exception as e:
            logger.error(f"Groq call failed after retries: {type(e).__name__}: {e}")
            return None

    def _parse_response(self, response: Any) -> dict:
        """Extract and parse JSON from Groq response."""
        try:
            content = response.choices[0].message.content
            if not content:
                logger.warning("Groq returned empty content")
                return {}
            return json.loads(content)
        except (json.JSONDecodeError, IndexError, AttributeError) as e:
            logger.error(f"Failed to parse Groq response: {e}")
            return {}

    def _validate_response(
        self, raw: dict, expected_keys: list[str]
    ) -> dict[str, dict[str, Any]]:
        """Validate AI response structure — filter invalid entries."""
        validated: dict[str, dict[str, Any]] = {}
        for key in expected_keys:
            if key not in raw:
                continue
            item = raw[key]
            if not isinstance(item, dict):
                continue

            status = item.get("status")
            if status not in ("evidence_found", "not_yet_evidenced"):
                logger.warning(f"Groq returned invalid status for {key}: {status}")
                continue

            # evidence_found must have at least one source
            if status == "evidence_found":
                sources = item.get("evidence_sources", [])
                if not sources or not isinstance(sources, list):
                    logger.warning(f"Groq found evidence for {key} but no valid sources")
                    continue

            validated[key] = item

        skipped = len(expected_keys) - len(validated)
        if skipped > 0:
            logger.info(f"Groq response: {len(validated)} valid, {skipped} skipped/missing")

        return validated

    def _log_cost(self, response: Any) -> None:
        """Log token usage and estimated cost."""
        if not settings.AI_COST_TRACKING:
            return
        try:
            usage = response.usage
            if not usage:
                return
            prompt_tokens = usage.prompt_tokens
            completion_tokens = usage.completion_tokens
            total_tokens = usage.total_tokens
            # Llama-3.3-70b: ~$0.59/1M input, $0.79/1M output (free tier $0)
            cost = (prompt_tokens * 0.59 / 1_000_000) + (completion_tokens * 0.79 / 1_000_000)
            logger.info(
                f"[AI Cost] provider=groq model={self.model} "
                f"prompt={prompt_tokens} completion={completion_tokens} total={total_tokens} "
                f"est_cost=${cost:.6f}"
            )
        except Exception:
            pass


class GeminiProvider(AIProvider):
    """Google Gemini implementation (kept for future use)."""

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
        subskill_definitions: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, dict[str, Any]]:
        try:
            full_prompt = (
                self._build_system_prompt(role_category, level)
                + "\n\n"
                + self._build_user_prompt(target_subskills, filtered_data, subskill_definitions)
            )

            response = await self.model.generate_content_async(
                full_prompt,
                generation_config={
                    "response_mime_type": "application/json",
                    "temperature": 0.1,
                    "max_output_tokens": settings.AI_MAX_OUTPUT_TOKENS,
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
        subskill_definitions: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, dict[str, Any]]:
        logger.info("AI provider disabled — using keyword-only detection")
        return {}


def get_ai_provider() -> AIProvider:
    """Factory function to get the configured AI provider."""
    provider = settings.AI_PROVIDER.lower()

    if provider == "openai":
        return OpenAIProvider()
    elif provider == "groq":
        if not settings.GROQ_API_KEY or "BURAYA" in settings.GROQ_API_KEY:
            logger.warning("AI_PROVIDER is set to 'groq', but GROQ_API_KEY is not configured. Falling back to keyword-only detection.")
            return NoOpProvider()
        return GroqProvider()
    elif provider == "gemini":
        return GeminiProvider()
    else:
        return NoOpProvider()


def _truncate_data_to_budget(
    filtered_data: dict[str, Any],
    max_tokens: int,
    system_prompt: str,
    target_subskills: list[str],
) -> dict[str, Any]:
    """
    Truncate file contents to fit within token budget.
    Prioritizes: dependencies > small files > large files.
    README is always included (capped at 1500 chars).
    """
    # Reserve tokens for system prompt, subskill list, deps, readme, output format
    overhead = _estimate_tokens(system_prompt) + len(target_subskills) * 40 + 500
    deps = filtered_data.get("dependencies", {})
    deps_tokens = _estimate_tokens(json.dumps(deps)) if deps else 0
    readme = filtered_data.get("readme", "")
    readme_tokens = _estimate_tokens(readme[:1500]) if readme else 0

    available = max_tokens - overhead - deps_tokens - readme_tokens
    if available <= 0:
        return {"file_contents": {}, "dependencies": deps, "readme": readme}

    # Sort files: smaller first (more files = more evidence diversity)
    files = filtered_data.get("file_contents", {})
    sorted_files = sorted(files.items(), key=lambda x: len(x[1]))

    truncated_files: dict[str, str] = {}
    used = 0
    for path, content in sorted_files:
        file_tokens = _estimate_tokens(content[:2000])  # Cap per file
        if used + file_tokens > available:
            # Try truncating this file
            remaining_chars = (available - used) * 4
            if remaining_chars > 200:
                truncated_files[path] = content[:remaining_chars]
            break
        truncated_files[path] = content[:2000]
        used += file_tokens

    logger.info(
        f"Token budget: {len(truncated_files)}/{len(files)} files included "
        f"({used} est. tokens used of {available} available)"
    )

    return {
        "file_contents": truncated_files,
        "dependencies": deps,
        "readme": readme,
    }
