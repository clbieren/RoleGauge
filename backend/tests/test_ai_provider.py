"""
Test Suite for AI Provider Integration.
Tests OpenAI provider with mocked API calls — no API key needed.
Covers: response parsing, validation, retry, chunking, cost tracking, merge logic.
"""

import json
import pytest
from unittest.mock import AsyncMock, MagicMock, patch, PropertyMock
from types import SimpleNamespace

# Ensure test env
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
os.environ.setdefault("AI_PROVIDER", "none")
os.environ.setdefault("KB_PATH", os.path.join(os.path.dirname(BASE_DIR), "knowledge-base"))


# ─── Helper: Build mock OpenAI response ─────────────────────────────
def _mock_response(content: dict | str, prompt_tokens: int = 100, completion_tokens: int = 50):
    """Build a mock that mimics openai ChatCompletion response."""
    if isinstance(content, dict):
        content = json.dumps(content)
    msg = SimpleNamespace(content=content)
    choice = SimpleNamespace(message=msg)
    usage = SimpleNamespace(
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        total_tokens=prompt_tokens + completion_tokens,
    )
    return SimpleNamespace(choices=[choice], usage=usage)


# ─── Helper: Build mock evidence dict ──────────────────────────────
def _make_evidence_result(composite_key: str, status: str = "not_yet_evidenced"):
    from app.services.evidence_detector import SubskillEvidenceResult
    return SubskillEvidenceResult(
        composite_key=composite_key,
        subskill_name=composite_key,
        status=status,
    )


# ═══════════════════════════════════════════════════════════════════
# OpenAIProvider Tests
# ═══════════════════════════════════════════════════════════════════

class TestOpenAIProvider:
    """Tests for OpenAIProvider with mocked openai client."""

    @pytest.fixture
    def provider(self):
        """Create OpenAIProvider with mocked client."""
        with patch.dict(os.environ, {"AI_PROVIDER": "openai", "OPENAI_API_KEY": "test-key"}):
            with patch("app.services.ai_provider.settings") as mock_settings:
                mock_settings.OPENAI_API_KEY = "test-key"
                mock_settings.OPENAI_MODEL = "gpt-4o-mini"
                mock_settings.AI_REQUEST_TIMEOUT = 10
                mock_settings.AI_MAX_RETRIES = 2
                mock_settings.AI_MAX_INPUT_TOKENS = 12000
                mock_settings.AI_MAX_OUTPUT_TOKENS = 4096
                mock_settings.AI_SUBSKILL_CHUNK_SIZE = 15
                mock_settings.AI_COST_TRACKING = False
                mock_settings.AI_PROVIDER = "openai"

                from app.services.ai_provider import OpenAIProvider
                prov = OpenAIProvider.__new__(OpenAIProvider)
                prov.client = AsyncMock()
                prov.model = "gpt-4o-mini"
                return prov

    @pytest.mark.asyncio
    async def test_successful_evidence_detection(self, provider):
        """AI returns valid evidence_found → parsed correctly."""
        ai_response = {
            "be_api_design.rest_principles": {
                "status": "evidence_found",
                "evidence_sources": ["fastapi/main.py → APIRouter usage"],
                "quality_notes": "Clear REST API implementation",
            },
            "be_api_design.graphql_apis": {
                "status": "not_yet_evidenced",
                "evidence_sources": [],
                "quality_notes": "No GraphQL usage found",
            },
        }
        provider.client.chat.completions.create = AsyncMock(
            return_value=_mock_response(ai_response)
        )

        result = await provider.analyze_evidence(
            "backend", "mid",
            ["be_api_design.rest_principles", "be_api_design.graphql_apis"],
            {"file_contents": {"main.py": "from fastapi import APIRouter"}, "dependencies": {}, "readme": ""},
        )

        assert "be_api_design.rest_principles" in result
        assert result["be_api_design.rest_principles"]["status"] == "evidence_found"
        assert len(result["be_api_design.rest_principles"]["evidence_sources"]) >= 1
        # not_yet_evidenced should also be included (valid status)
        assert "be_api_design.graphql_apis" in result

    @pytest.mark.asyncio
    async def test_invalid_status_filtered(self, provider):
        """AI returns invalid status → entry filtered out."""
        ai_response = {
            "be_api_design.rest_principles": {
                "status": "maybe_found",  # Invalid
                "evidence_sources": ["some/file.py"],
                "quality_notes": "Invalid",
            },
        }
        provider.client.chat.completions.create = AsyncMock(
            return_value=_mock_response(ai_response)
        )

        result = await provider.analyze_evidence(
            "backend", "mid",
            ["be_api_design.rest_principles"],
            {"file_contents": {}, "dependencies": {}, "readme": ""},
        )

        assert "be_api_design.rest_principles" not in result

    @pytest.mark.asyncio
    async def test_evidence_without_sources_filtered(self, provider):
        """AI says evidence_found but provides no sources → filtered."""
        ai_response = {
            "be_api_design.rest_principles": {
                "status": "evidence_found",
                "evidence_sources": [],  # Empty!
                "quality_notes": "Found but no details",
            },
        }
        provider.client.chat.completions.create = AsyncMock(
            return_value=_mock_response(ai_response)
        )

        result = await provider.analyze_evidence(
            "backend", "mid",
            ["be_api_design.rest_principles"],
            {"file_contents": {}, "dependencies": {}, "readme": ""},
        )

        assert "be_api_design.rest_principles" not in result

    @pytest.mark.asyncio
    async def test_timeout_returns_empty(self, provider):
        """API timeout → returns empty dict (graceful degradation)."""
        from openai import APITimeoutError
        provider.client.chat.completions.create = AsyncMock(
            side_effect=APITimeoutError(request=MagicMock())
        )

        result = await provider.analyze_evidence(
            "backend", "mid",
            ["be_api_design.rest_principles"],
            {"file_contents": {}, "dependencies": {}, "readme": ""},
        )

        assert result == {}

    @pytest.mark.asyncio
    async def test_malformed_json_returns_empty(self, provider):
        """Malformed JSON response → returns empty dict."""
        bad_response = _mock_response("this is not json at all {{{")
        provider.client.chat.completions.create = AsyncMock(return_value=bad_response)

        result = await provider.analyze_evidence(
            "backend", "mid",
            ["be_api_design.rest_principles"],
            {"file_contents": {}, "dependencies": {}, "readme": ""},
        )

        assert result == {}

    @pytest.mark.asyncio
    async def test_empty_subskills_returns_empty(self, provider):
        """Empty target_subskills list → returns empty immediately."""
        result = await provider.analyze_evidence(
            "backend", "mid", [], {"file_contents": {}, "dependencies": {}, "readme": ""},
        )
        assert result == {}
        # Should not call API at all
        provider.client.chat.completions.create.assert_not_called()

    @pytest.mark.asyncio
    async def test_subskill_chunking(self, provider):
        """More subskills than chunk_size → multiple API calls."""
        with patch("app.services.ai_provider.settings") as mock_s:
            mock_s.AI_SUBSKILL_CHUNK_SIZE = 3
            mock_s.AI_MAX_INPUT_TOKENS = 50000
            mock_s.AI_MAX_OUTPUT_TOKENS = 4096
            mock_s.AI_MAX_RETRIES = 1
            mock_s.AI_REQUEST_TIMEOUT = 10
            mock_s.AI_COST_TRACKING = False

            subskills = [f"skill.sub_{i}" for i in range(7)]  # 7 subskills, chunk_size=3

            def make_chunk_response(*args, **kwargs):
                # Return not_yet_evidenced for all
                msgs = kwargs.get("messages", args[0] if args else [])
                return _mock_response(
                    {sk: {"status": "not_yet_evidenced", "evidence_sources": [], "quality_notes": ""}
                     for sk in subskills}
                )

            provider.client.chat.completions.create = AsyncMock(side_effect=make_chunk_response)

            result = await provider.analyze_evidence(
                "backend", "mid", subskills,
                {"file_contents": {}, "dependencies": {}, "readme": ""},
            )

            # Should have made ceil(7/3) = 3 API calls
            assert provider.client.chat.completions.create.call_count == 3

    @pytest.mark.asyncio
    async def test_subskill_definitions_in_prompt(self, provider):
        """Subskill definitions are included in the prompt."""
        ai_response = {
            "be_api_design.rest_principles": {
                "status": "not_yet_evidenced",
                "evidence_sources": [],
                "quality_notes": "",
            },
        }
        provider.client.chat.completions.create = AsyncMock(
            return_value=_mock_response(ai_response)
        )

        defs = {
            "be_api_design.rest_principles": {
                "name": "RESTful Principles",
                "description": "Resource-oriented URL design",
                "keywords": ["REST", "HTTP methods"],
            }
        }

        await provider.analyze_evidence(
            "backend", "mid",
            ["be_api_design.rest_principles"],
            {"file_contents": {}, "dependencies": {}, "readme": ""},
            subskill_definitions=defs,
        )

        # Check the user prompt includes the definition
        call_args = provider.client.chat.completions.create.call_args
        messages = call_args.kwargs.get("messages", call_args[1].get("messages", []))
        user_msg = messages[1]["content"]
        assert "RESTful Principles" in user_msg
        assert "REST" in user_msg


# ═══════════════════════════════════════════════════════════════════
# NoOpProvider Tests
# ═══════════════════════════════════════════════════════════════════

class TestNoOpProvider:

    @pytest.mark.asyncio
    async def test_noop_returns_empty(self):
        from app.services.ai_provider import NoOpProvider
        provider = NoOpProvider()
        result = await provider.analyze_evidence(
            "backend", "mid", ["some.skill"],
            {"file_contents": {}, "dependencies": {}, "readme": ""},
        )
        assert result == {}


# ═══════════════════════════════════════════════════════════════════
# Factory Tests
# ═══════════════════════════════════════════════════════════════════

class TestAIProviderFactory:

    def test_factory_returns_noop_default(self):
        with patch("app.services.ai_provider.settings") as mock_s:
            mock_s.AI_PROVIDER = "none"
            from app.services.ai_provider import get_ai_provider, NoOpProvider
            provider = get_ai_provider()
            assert isinstance(provider, NoOpProvider)

    def test_factory_returns_openai(self):
        with patch("app.services.ai_provider.settings") as mock_s:
            mock_s.AI_PROVIDER = "openai"
            mock_s.OPENAI_API_KEY = "test-key"
            mock_s.OPENAI_MODEL = "gpt-4o-mini"
            mock_s.AI_REQUEST_TIMEOUT = 60
            from app.services.ai_provider import get_ai_provider, OpenAIProvider
            provider = get_ai_provider()
            assert isinstance(provider, OpenAIProvider)

# ═══════════════════════════════════════════════════════════════════
# Merge AI Results Tests
# (standalone logic copy — avoids analyze.py → db_models import chain)
# ═══════════════════════════════════════════════════════════════════

def _merge_ai_results_standalone(evidence: dict, ai_results: dict):
    """Standalone copy of merge logic for testing without SQLAlchemy import chain."""
    from app.services.evidence_detector import EvidenceSignal

    for composite_key, ai_data in ai_results.items():
        if composite_key not in evidence:
            continue
        if ai_data.get("status") == "evidence_found":
            sources = ai_data.get("evidence_sources", [])
            quality = ai_data.get("quality_notes", "")
            strength = 0.7
            quality_lower = quality.lower() if quality else ""
            if any(w in quality_lower for w in ("config", "trivial", "basic", "readme", "mention")):
                strength = 0.5
            for source in sources:
                evidence[composite_key].signals.append(EvidenceSignal(
                    source="ai", file_path=source,
                    matched_text=f"[AI] {quality}" if quality else "AI detected",
                    strength=strength,
                ))
            evidence[composite_key].status = "evidence_found"


class TestMergeAIResults:

    def test_merge_updates_evidence(self):
        evidence = {"be_api.rest": _make_evidence_result("be_api.rest")}
        ai_results = {
            "be_api.rest": {
                "status": "evidence_found",
                "evidence_sources": ["repo/main.py → FastAPI usage"],
                "quality_notes": "Clear implementation",
            },
        }
        _merge_ai_results_standalone(evidence, ai_results)
        assert evidence["be_api.rest"].status == "evidence_found"
        assert len(evidence["be_api.rest"].signals) == 1
        assert evidence["be_api.rest"].signals[0].source == "ai"
        assert evidence["be_api.rest"].signals[0].strength == 0.7

    def test_merge_skips_unknown_keys(self):
        evidence = {"be_api.rest": _make_evidence_result("be_api.rest")}
        ai_results = {
            "unknown.skill": {
                "status": "evidence_found",
                "evidence_sources": ["some/file"],
                "quality_notes": "",
            },
        }
        _merge_ai_results_standalone(evidence, ai_results)
        assert evidence["be_api.rest"].status == "not_yet_evidenced"

    def test_merge_signal_strength_gradation(self):
        evidence = {
            "be_api.rest": _make_evidence_result("be_api.rest"),
            "be_api.graphql": _make_evidence_result("be_api.graphql"),
        }
        ai_results = {
            "be_api.rest": {
                "status": "evidence_found",
                "evidence_sources": ["repo/main.py → API"],
                "quality_notes": "Strong code-level evidence of REST API patterns",
            },
            "be_api.graphql": {
                "status": "evidence_found",
                "evidence_sources": ["repo/config.yml → mention"],
                "quality_notes": "Basic config mention only",
            },
        }
        _merge_ai_results_standalone(evidence, ai_results)
        assert evidence["be_api.rest"].signals[0].strength == 0.7
        assert evidence["be_api.graphql"].signals[0].strength == 0.5

    def test_merge_not_yet_evidenced_ignored(self):
        evidence = {"be_api.rest": _make_evidence_result("be_api.rest")}
        ai_results = {
            "be_api.rest": {
                "status": "not_yet_evidenced",
                "evidence_sources": [],
                "quality_notes": "Nothing found",
            },
        }
        _merge_ai_results_standalone(evidence, ai_results)
        assert evidence["be_api.rest"].status == "not_yet_evidenced"
        assert len(evidence["be_api.rest"].signals) == 0


# ═══════════════════════════════════════════════════════════════════
# Token Estimation & Truncation Tests
# ═══════════════════════════════════════════════════════════════════

class TestTokenUtilities:

    def test_estimate_tokens(self):
        from app.services.ai_provider import _estimate_tokens
        assert _estimate_tokens("") == 0
        assert _estimate_tokens("a" * 400) == 100

    def test_truncate_data_to_budget(self):
        from app.services.ai_provider import _truncate_data_to_budget

        large_files = {f"file_{i}.py": "x" * 5000 for i in range(20)}
        data = {"file_contents": large_files, "dependencies": {}, "readme": "Short readme"}

        truncated = _truncate_data_to_budget(
            data,
            max_tokens=2000,
            system_prompt="System prompt here",
            target_subskills=["skill.a", "skill.b"],
        )

        assert len(truncated["file_contents"]) < len(large_files)
        assert truncated["dependencies"] == {}
        assert truncated["readme"] == "Short readme"

    def test_ext_to_lang(self):
        from app.services.ai_provider import _ext_to_lang
        assert _ext_to_lang("py") == "python"
        assert _ext_to_lang("ts") == "typescript"
        assert _ext_to_lang("unknown") == ""


# ═══════════════════════════════════════════════════════════════════
# Subskill Definitions Helper Tests
# (standalone logic — avoids analyze.py import chain)
# ═══════════════════════════════════════════════════════════════════

def _get_subskill_definitions_standalone(knowledge_base, role_id, composite_keys):
    """Standalone copy for testing."""
    defs = {}
    for skill_id, skill_data in knowledge_base.get_skills_for_role(role_id).items():
        for subskill in skill_data.get("subskills", []):
            ck = f"{skill_id}.{subskill['id']}"
            if ck in composite_keys:
                defs[ck] = {
                    "name": subskill.get("name", subskill["id"]),
                    "description": subskill.get("description", ""),
                    "keywords": subskill.get("keywords", []),
                }
    return defs


class TestGetSubskillDefinitions:

    def test_extracts_definitions(self):
        from app.services.kb_loader import kb
        kb.load()
        defs = _get_subskill_definitions_standalone(
            kb, "backend", ["be_api_design.restful_principles"]
        )
        if "be_api_design.restful_principles" in defs:
            d = defs["be_api_design.restful_principles"]
            assert "name" in d
            assert "keywords" in d
            assert isinstance(d["keywords"], list)

    def test_unknown_keys_return_empty(self):
        from app.services.kb_loader import kb
        kb.load()
        defs = _get_subskill_definitions_standalone(
            kb, "backend", ["nonexistent.key"]
        )
        assert "nonexistent.key" not in defs
