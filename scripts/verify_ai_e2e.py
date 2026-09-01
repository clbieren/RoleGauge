"""
RoleGauge AI Integration E2E Verification Script.

Prerequisites:
  - Backend running at localhost:8000
  - OPENAI_API_KEY set in .env
  - AI_PROVIDER=openai in .env

Usage:
  python scripts/verify_ai_e2e.py
"""

import json
import sys
import time
import httpx

BASE_URL = "http://localhost:8000"
TIMEOUT = 120  # Analysis can take a while with AI


def check_health():
    """Verify backend is running and AI provider is configured."""
    print("=" * 60)
    print("Step 1: Health Check")
    print("=" * 60)
    try:
        r = httpx.get(f"{BASE_URL}/api/health", timeout=10)
        r.raise_for_status()
        data = r.json()
        print(f"  Status:       {data['status']}")
        print(f"  Version:      {data['version']}")
        print(f"  Roles loaded: {data['roles_loaded']}")
        print(f"  AI provider:  {data['ai_provider']}")

        if data["ai_provider"] == "none":
            print("\n  ⚠ WARNING: AI_PROVIDER is 'none'. Set AI_PROVIDER=openai in .env")
            print("  This script requires an active AI provider.")
            return False
        return True
    except Exception as e:
        print(f"  ✗ Backend not reachable: {e}")
        return False


def run_analysis_comparison():
    """Run same analysis with and without AI, compare results."""
    print("\n" + "=" * 60)
    print("Step 2: Analysis Comparison (keyword-only vs AI-enriched)")
    print("=" * 60)

    payload_base = {
        "github_username": "tiangolo",
        "role_id": "backend",
        "level": "mid",
    }

    # Run 1: keyword-only
    print("\n  [1/2] Running keyword-only analysis...")
    t0 = time.time()
    try:
        r1 = httpx.post(
            f"{BASE_URL}/api/analyze",
            json={**payload_base, "use_ai": False},
            timeout=TIMEOUT,
        )
        r1.raise_for_status()
        result_kw = r1.json()
        t1 = time.time()
        print(f"        Done in {t1 - t0:.1f}s")
    except Exception as e:
        print(f"        ✗ Failed: {e}")
        return

    # Run 2: AI-enriched
    print("  [2/2] Running AI-enriched analysis...")
    t0 = time.time()
    try:
        r2 = httpx.post(
            f"{BASE_URL}/api/analyze",
            json={**payload_base, "use_ai": True},
            timeout=TIMEOUT,
        )
        r2.raise_for_status()
        result_ai = r2.json()
        t1 = time.time()
        print(f"        Done in {t1 - t0:.1f}s")
    except Exception as e:
        print(f"        ✗ Failed: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"        Response: {e.response.text[:500]}")
        return

    # Compare
    print("\n" + "-" * 60)
    print("  Comparison Results:")
    print("-" * 60)

    kw_score = result_kw["readiness_score"]
    ai_score = result_ai["readiness_score"]
    kw_tier = result_kw["readiness_tier"]
    ai_tier = result_ai["readiness_tier"]

    print(f"  {'Metric':<35} {'Keyword-Only':>15} {'AI-Enriched':>15}")
    print(f"  {'─' * 35} {'─' * 15} {'─' * 15}")
    print(f"  {'Readiness Score':<35} {kw_score:>15.4f} {ai_score:>15.4f}")
    print(f"  {'Readiness Tier':<35} {kw_tier:>15} {ai_tier:>15}")

    # Count evidenced subskills
    kw_evidenced = 0
    ai_evidenced = 0
    ai_exclusive = []

    kw_subskills = {}
    for skill in result_kw.get("skills", []):
        for sub in skill.get("subskills", []):
            kw_subskills[sub["composite_key"]] = sub["status"]
            if sub["status"] == "evidence_found":
                kw_evidenced += 1

    for skill in result_ai.get("skills", []):
        for sub in skill.get("subskills", []):
            if sub["status"] == "evidence_found":
                ai_evidenced += 1
                # Check if AI found evidence that keywords missed
                if kw_subskills.get(sub["composite_key"]) != "evidence_found":
                    ai_exclusive.append(sub["composite_key"])

    total_subskills = sum(len(s.get("subskills", [])) for s in result_kw.get("skills", []))
    print(f"  {'Total Subskills':<35} {total_subskills:>15} {total_subskills:>15}")
    print(f"  {'Evidenced Subskills':<35} {kw_evidenced:>15} {ai_evidenced:>15}")
    print(f"  {'AI-Exclusive Detections':<35} {'—':>15} {len(ai_exclusive):>15}")

    if ai_exclusive:
        print(f"\n  AI found {len(ai_exclusive)} additional subskills:")
        for ck in ai_exclusive[:10]:
            print(f"    + {ck}")
        if len(ai_exclusive) > 10:
            print(f"    ... and {len(ai_exclusive) - 10} more")

    # Score improvement
    if ai_score > kw_score:
        improvement = ((ai_score - kw_score) / max(kw_score, 0.001)) * 100
        print(f"\n  ✓ AI improved score by {improvement:.1f}%")
    elif ai_score == kw_score:
        print("\n  ≈ AI did not change the score (keywords already comprehensive)")
    else:
        print(f"\n  ⚠ AI score is lower (unexpected — check evidence ceiling rules)")

    print("\n  ✓ E2E verification complete")


def main():
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║   RoleGauge AI Integration — E2E Verification           ║")
    print("╚══════════════════════════════════════════════════════════╝\n")

    if not check_health():
        sys.exit(1)

    run_analysis_comparison()


if __name__ == "__main__":
    main()
