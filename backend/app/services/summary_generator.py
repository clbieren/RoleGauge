"""
Summary Generator.
Produces a human-readable, tier-based summary sentence from ScoringEngine output.

Design constraints:
  - ZERO AI calls — deterministic template substitution only.
  - Works for both free (standard) and premium tiers.
  - When analysis_tier == "premium" (not yet active), a TODO placeholder is returned
    so that a future AI call can be swapped in without touching other modules.

Output contract:
  generate_summary() → (summary_text: str, summary_type: str)
    summary_type: "template" | "ai_generated"
"""

import logging
from typing import Any

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────
# Turkish Templates (one per readiness tier)
# Variables: {role_name}, {score}, {top_skill}, {second_skill}, {weak_skill}
# ──────────────────────────────────────────────

TEMPLATES: dict[str, str] = {
    "not_ready": (
        "{role_name} rolü için hazırlık seviyeniz henüz başlangıç aşamasında (%{score}). "
        "En güçlü olduğunuz alan {top_skill}; "
        "{weak_skill} alanında belirgin bir gelişim fırsatı var."
    ),
    "developing": (
        "{role_name} rolüne doğru ilerliyorsunuz (%{score}). "
        "{top_skill} konusunda güçlüsünüz; "
        "{weak_skill} üzerine odaklanmanız skorunuzu belirgin şekilde artırabilir."
    ),
    "approaching": (
        "{role_name} rolü için hazırlığınız olgunlaşıyor (%{score}). "
        "{top_skill} net bir güç alanı; "
        "birkaç eksik kanıtı tamamlayarak 'Ready' seviyesine yaklaşabilirsiniz."
    ),
    "ready": (
        "{role_name} rolü için güçlü bir profil sergiliyorsunuz (%{score}). "
        "{top_skill} ve {second_skill} alanlarında kanıtlanmış yetkinliğiniz var."
    ),
    "exceeds": (
        "{role_name} rolü beklentilerinin üzerinde bir profil (%{score}). "
        "{top_skill} alanında uzmanlık düzeyinde kanıt bulunuyor; "
        "{second_skill} de güçlü bir tamamlayıcı yetkinlik."
    ),
}

# English equivalents — returned when locale hint is "en" (future use)
TEMPLATES_EN: dict[str, str] = {
    "not_ready": (
        "Your readiness for the {role_name} role is still at an early stage ({score}%). "
        "Your strongest area is {top_skill}; "
        "{weak_skill} shows a clear opportunity for growth."
    ),
    "developing": (
        "You are progressing toward the {role_name} role ({score}%). "
        "You are strong in {top_skill}; "
        "focusing on {weak_skill} could meaningfully improve your score."
    ),
    "approaching": (
        "Your readiness for the {role_name} role is maturing ({score}%). "
        "{top_skill} is a clear strength; "
        "completing a few missing evidence items could bring you to the 'Ready' level."
    ),
    "ready": (
        "You demonstrate a strong profile for the {role_name} role ({score}%). "
        "You have proven competency in {top_skill} and {second_skill}."
    ),
    "exceeds": (
        "You exceed expectations for the {role_name} role ({score}%). "
        "Expert-level evidence exists for {top_skill}; "
        "{second_skill} is a strong complementary skill."
    ),
}

# Fallback tier — used when scoring returns an unexpected tier string
_FALLBACK_TIER = "developing"


def _rank_skills(skills: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Rank skills by composite strength: score × importance.
    Returns a list sorted descending (strongest first).
    """
    return sorted(
        skills,
        key=lambda s: s.get("score", 0.0) * s.get("importance", 0.5),
        reverse=True,
    )


def _skill_label(skill: dict[str, Any]) -> str:
    """Return the display name of a skill, falling back to skill_id."""
    return skill.get("skill_name") or skill.get("skill_id") or "Unknown Skill"


def generate_summary(
    tier: str,
    role_name: str,
    readiness_score: float,
    skills: list[dict[str, Any]],
    analysis_tier: str = "standard",
    locale: str = "tr",
) -> tuple[str, str]:
    """
    Generate a tier-appropriate summary sentence.

    Args:
        tier:            Readiness tier key (e.g. "approaching", "ready").
        role_name:       Human-readable role title (e.g. "Senior Backend Developer").
        readiness_score: Float 0.0–1.0 from ScoringEngine.
        skills:          List of skill dicts from ScoringEngine.calculate_all()["skills"].
        analysis_tier:   "standard" (always) or "premium" (future — placeholder only).
        locale:          "tr" (default) or "en".

    Returns:
        (summary_text, summary_type)
        summary_type is "template" for free/standard tier.
        summary_type will be "ai_generated" for premium (once AI is re-enabled) — TODO.
    """
    # ── Future premium hook (AI disabled globally — placeholder only) ──
    if analysis_tier == "premium":
        # TODO: When AI is re-enabled for premium users, replace this block with
        #       an async call to ai_provider.generate_summary(...) and return
        #       (ai_text, "ai_generated"). For now, fall through to template.
        logger.debug("[SummaryGenerator] Premium tier detected — AI disabled, falling back to template.")

    # ── Select template bank ──
    template_bank = TEMPLATES if locale == "tr" else TEMPLATES_EN
    template = template_bank.get(tier, template_bank.get(_FALLBACK_TIER, ""))

    if not template:
        logger.warning(f"[SummaryGenerator] No template for tier='{tier}', locale='{locale}'.")
        return ("", "template")

    # ── Rank skills & extract named slots ──
    ranked = _rank_skills(skills) if skills else []

    # Ensure we always have safe fallback strings
    top_skill = _skill_label(ranked[0]) if len(ranked) >= 1 else "core skills"
    second_skill = _skill_label(ranked[1]) if len(ranked) >= 2 else top_skill
    # Weakest = bottom of ranked list (lowest composite score)
    weak_skill = _skill_label(ranked[-1]) if ranked else "foundational areas"

    # Avoid weak == top when there is only one skill
    if weak_skill == top_skill and len(ranked) > 1:
        weak_skill = _skill_label(ranked[-2])

    # Score as rounded integer percentage
    score_pct = round(readiness_score * 100)

    # Strip level prefix from role name for brevity (e.g. "Senior Backend Developer" → keep as-is)
    display_role = role_name.strip() or "Hedef"

    # ── Fill template ──
    try:
        summary_text = template.format(
            role_name=display_role,
            score=score_pct,
            top_skill=top_skill,
            second_skill=second_skill,
            weak_skill=weak_skill,
        )
    except KeyError as e:
        logger.error(f"[SummaryGenerator] Template key error for tier='{tier}': {e}")
        return ("", "template")

    logger.info(
        f"[SummaryGenerator] tier={tier}, score={score_pct}%, "
        f"top={top_skill}, weak={weak_skill} → {len(summary_text)} chars"
    )
    return (summary_text, "template")
