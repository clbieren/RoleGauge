"""
Stage 1 Verification Script.
Proves that:
1. analyze.py properly persists contributing_sources, ceiling_applied, and calculation_trace to DB.
2. assessment.py properly restores existing GitHub evidence signals from DB using contributing_sources.
3. Submitting a correct assessment answer results in multi-source fusion (GitHub + Assessment signals coexist in contributing_sources), and subskill confidence increases without wiping out GitHub signals.
"""

import os
import sys
import uuid

# Setup path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_DIR = os.path.join(PROJECT_ROOT, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test_stage1.db"
os.environ["KB_PATH"] = os.path.join(PROJECT_ROOT, "knowledge-base")
os.environ["AI_PROVIDER"] = "none"

from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import get_db, async_session, create_tables
from app.main import app
from app.models.db_models import Analysis, SkillResult, SubskillResult
from app.services.kb_loader import kb
from app.services.scoring_engine import ScoringEngine
from app.services.evidence_detector import SubskillEvidenceResult, EvidenceSignal
from app.services.role_filter import FilteredRepo
from app.routers.analyze import _save_analysis
import asyncio

async def async_setup():
    await create_tables()

def main():
    if os.path.exists("test_stage1.db"):
        try:
            os.remove("test_stage1.db")
        except OSError:
            pass
    print("=" * 80)
    print("STAGE 1 VERIFICATION: Backend Data Integrity & Multi-Source Fusion")
    print("=" * 80)

    kb.load()
    asyncio.run(async_setup())

    with TestClient(app) as client:
        # Step 1: Create an analysis with genuine GitHub evidence signals in DB
        print("\n[*] Step 1: Creating Analysis with GitHub evidence signals in DB...")
        role_id = "backend"
        level = "mid"
        target_ck = "be_api_design.restful_principles"

        engine = ScoringEngine(kb, role_id, level)
        
        # Build genuine GitHub evidence signal
        gh_signal = EvidenceSignal(
            source="github",
            file_path="app/routers/items.py",
            matched_text="class APIRouter: @router.get('/items')",
            strength=0.70,
        )
        sub_evidence = SubskillEvidenceResult(
            composite_key=target_ck,
            subskill_name="RESTful API Design & Best Practices",
            status="evidence_found",
            signals=[gh_signal],
            contributing_sources=[{
                "source": "github",
                "strength": 0.70,
                "signal": "class APIRouter: @router.get('/items')",
                "file_path": "app/routers/items.py",
            }],
            ceiling_applied="github_present",
            calculation_trace="Primary source: github (0.70)",
        )

        all_evidence = {target_ck: sub_evidence}
        # Fill other subskills as empty for scoring
        for s_id, s_data in kb.get_skills_for_role(role_id).items():
            for sub in s_data.get("subskills", []):
                ck = f"{s_id}.{sub['id']}"
                if ck != target_ck:
                    all_evidence[ck] = SubskillEvidenceResult(
                        composite_key=ck,
                        subskill_name=sub.get("name", sub["id"]),
                        status="not_yet_evidenced",
                        signals=[],
                        contributing_sources=[],
                    )

        scoring_result = engine.calculate_all(all_evidence)
        dummy_repo = FilteredRepo(
            repo_name="demo-repo",
            full_name="test/demo-repo",
            url="https://github.com/test/demo-repo",
            stars=10,
            forks=2,
            primary_language="Python",
            languages={"Python": 1000},
            topics=["api", "fastapi"],
            is_relevant=True,
            relevant_files=["app/routers/items.py"],
            file_contents={"app/routers/items.py": "class APIRouter: @router.get('/items')"},
            dependency_files={"requirements.txt": "fastapi"},
            readme_content="API service",
        )

        # Save via _save_analysis (the exact function modified in analyze.py)
        async def save():
            async with async_session() as session:
                analysis = await _save_analysis(
                    db=session,
                    user_id=None,
                    username="test_candidate",
                    role_id=role_id,
                    level=level,
                    use_ai=False,
                    scoring_result=scoring_result,
                    filtered_repos=[dummy_repo],
                    scoring_evidence=all_evidence,
                )
                await session.commit()
                return str(analysis.id)

        analysis_id = asyncio.run(save())
        print(f"    [+] Created Analysis ID: {analysis_id}")

        # Step 2: Verify that contributing_sources is actually stored in DB!
        async def check_db():
            async with async_session() as session:
                stmt = (
                    select(SubskillResult)
                    .where(SubskillResult.composite_key == target_ck)
                )
                res = await session.execute(stmt)
                sub_rec = res.scalars().first()
                return {
                    "confidence": sub_rec.confidence,
                    "contributing_sources": sub_rec.contributing_sources,
                    "ceiling_applied": sub_rec.ceiling_applied,
                    "calculation_trace": sub_rec.calculation_trace,
                }

        initial_db = asyncio.run(check_db())
        print(f"\n[*] Step 2: Verifying Initial Database Persistence for '{target_ck}':")
        print(f"    Confidence: {initial_db['confidence']}")
        print(f"    Contributing Sources in DB: {initial_db['contributing_sources']}")
        print(f"    Ceiling Applied: {initial_db['ceiling_applied']}")
        assert initial_db['contributing_sources'] is not None and len(initial_db['contributing_sources']) > 0, "FAILED: contributing_sources not persisted!"
        assert initial_db['contributing_sources'][0]["source"] == "github", "FAILED: source is not github!"
        print("    [PASSED] contributing_sources persisted as structured JSON in DB!")

        # Step 3: Start assessment on this analysis for this subskill
        print(f"\n[*] Step 3: Starting Assessment for '{target_ck}' on analysis {analysis_id}...")
        start_res = client.post(
            "/api/assessment/start",
            json={
                "analysis_id": analysis_id,
                "voluntary_composite_keys": [target_ck],
                "max_questions": 1,
            },
        )
        assert start_res.status_code == 200, f"Start failed: {start_res.text}"
        start_data = start_res.json()
        session_id = start_data["assessment_session_id"]
        q = start_data["questions"][0]
        print(f"    [+] Assessment Session ID: {session_id}")
        print(f"    [+] Question: {q['question']}")

        # Step 4: Submit a high-quality answer that will match keywords
        print(f"\n[*] Step 4: Submitting correct answer to assessment...")
        answer_text = (
            "PUT full replacement idempotent ensures complete state replacement without side effects on repeat calls. "
            "PATCH partial update modifies only specified fields. "
            "DELETE can return 204 No Content when nothing to return or 200 OK with status. "
            "We adhere to idempotency semantics across endpoints and maintain clean URI resource identification."
        )

        sub_res = client.post(
            "/api/assessment/submit",
            json={
                "assessment_session_id": session_id,
                "answers": {target_ck: answer_text},
            },
        )
        assert sub_res.status_code == 200, f"Submit failed: {sub_res.text}"
        sub_data = sub_res.json()
        eval_item = sub_data["evaluations"][0]
        print(f"    [+] Assessment Verdict: {eval_item['verdict']}")
        print(f"    [+] Assessment Score: {eval_item['score']} (Strength: {eval_item['strength']})")
        print(f"    [+] Assessment Feedback: {eval_item['feedback']}")

        # Step 5: Check resulting subskill in DB & updated_analysis
        updated_analysis = sub_data["updated_analysis"]
        target_sub_updated = None
        for sk in updated_analysis["skills"]:
            for sub in sk["subskills"]:
                if sub["composite_key"] == target_ck:
                    target_sub_updated = sub
                    break

        print("\n[*] Step 5: Multi-Source Fusion Evidence Check:")
        print(f"    Baseline Confidence: {initial_db['confidence']}")
        print(f"    Updated Confidence:  {target_sub_updated['confidence']}")
        print(f"    Updated Contributing Sources count: {len(target_sub_updated.get('contributing_sources', []))}")
        for i, src in enumerate(target_sub_updated.get('contributing_sources', []), 1):
            print(f"      Source {i}: {src['source']} (strength: {src['strength']}, signal: {src['signal'][:50]}...)")

        # ASSERTIONS FOR STAGE 1 SUCCESS:
        sources = target_sub_updated.get("contributing_sources", [])
        source_types = [s["source"] for s in sources]
        
        print("\n[*] STAGE 1 INTEGRITY ASSERTIONS:")
        assert "github" in source_types, "CRITICAL FAILURE: GitHub evidence was wiped out during assessment submission!"
        print("    [PASSED] GitHub evidence was NOT wiped out; preserved in contributing_sources!")
        
        assert "assessment" in source_types, "CRITICAL FAILURE: Assessment evidence was not ingested into contributing_sources!"
        print("    [PASSED] Assessment evidence was successfully ingested alongside GitHub evidence!")
        
        assert target_sub_updated["confidence"] >= initial_db["confidence"], (
            f"CRITICAL FAILURE: Confidence decreased from {initial_db['confidence']} to {target_sub_updated['confidence']}!"
        )
        print(f"    [PASSED] Multi-source confidence maintained/increased: {initial_db['confidence']} -> {target_sub_updated['confidence']}")
        
        print("\n" + "=" * 80)
        print("STAGE 1 COMPLETED SUCCESSFULLY: BACKEND DATA INTEGRITY PROVEN!")
        print("=" * 80)

if __name__ == "__main__":
    main()
