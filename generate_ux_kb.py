import json
import os

base_dir = os.path.abspath('knowledge-base')
skills_dir = os.path.join(base_dir, 'skills', 'ux-design')
evidence_dir = os.path.join(base_dir, 'evidence', 'ux-designer')
roles_dir = os.path.join(base_dir, 'roles', 'ux-designer')

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────
# SKILLS
# ─────────────────────────────────────────────────────────────

skills = {}

# 1. ux_behavior_frameworks
skills["ux_behavior_frameworks"] = {
  "skill_id": "ux_behavior_frameworks",
  "name": "Human Behavior Frameworks & Theories",
  "category": "ux_behavioral_science",
  "description": "Foundational theoretical frameworks explaining how human behavior is formed, triggered, and changed. Covers BJ Fogg's Behavior Model, Nir Eyal's Hook Model, the CREATE Action Funnel, Dual Process Theory (System 1 & 2), the Behavior Grid, the Cue-Routine-Reward habit loop, and the Spectrum of Thinking Interventions.",
  "subskills": [
    {
      "id": "fogg_behavior_model",
      "name": "BJ Fogg's Behavior Model (B=MAP)",
      "description": "Fogg's model states Behavior = Motivation × Ability × Prompt. All three must converge simultaneously. Covers motivation dimensions, ability factors, and prompt types (spark, facilitator, signal).",
      "keywords": ["B=MAP", "Fogg Behavior Model", "motivation", "ability", "prompt", "spark", "facilitator", "signal", "Tiny Habits", "behavior threshold", "action line"]
    },
    {
      "id": "fogg_behavior_grid",
      "name": "BJ Fogg's Behavior Grid",
      "description": "A 15-cell matrix classifying behaviors across type (do, don't, continue, stop, path) and duration (one-time, period, permanent). Used to select the right persuasive strategy.",
      "keywords": ["Behavior Grid", "green behavior", "blue behavior", "purple behavior", "gray behavior", "black behavior", "one-time behavior", "permanent behavior", "behavior type classification"]
    },
    {
      "id": "hook_model",
      "name": "Nir Eyal's Hook Model",
      "description": "A four-phase loop (Trigger → Action → Variable Reward → Investment) for building habit-forming products.",
      "keywords": ["Hook Model", "Trigger", "Action", "Variable Reward", "Investment", "external trigger", "internal trigger", "reward of the tribe", "reward of the hunt", "reward of the self", "stored value", "Hooked"]
    },
    {
      "id": "create_action_funnel",
      "name": "CREATE Action Funnel",
      "description": "Stephen Wendel's 6-step behavioral funnel: Cue, Reaction, Evaluation, Ability, Timing, Experience.",
      "keywords": ["CREATE", "Cue", "Reaction", "Evaluation", "Ability", "Timing", "Experience", "Stephen Wendel", "Designing for Behavior Change", "behavioral funnel"]
    },
    {
      "id": "dual_process_theory",
      "name": "Dual Process Theory (System 1 & System 2)",
      "description": "Kahneman's framework distinguishing fast automatic System 1 from slow deliberate System 2 thinking.",
      "keywords": ["Dual Process Theory", "System 1", "System 2", "Kahneman", "Thinking Fast and Slow", "automatic thinking", "deliberate thinking", "cognitive load", "heuristics", "biases"]
    },
    {
      "id": "cue_routine_reward",
      "name": "Cue-Routine-Reward Habit Loop",
      "description": "Charles Duhigg's habit loop model: cue triggers a routine that delivers a reward, reinforcing the loop.",
      "keywords": ["Cue-Routine-Reward", "habit loop", "Duhigg", "Power of Habit", "craving", "routine", "reward", "habit formation", "golden rule of habit change"]
    },
    {
      "id": "spectrum_of_thinking_interventions",
      "name": "Spectrum of Thinking Interventions",
      "description": "A continuum from fully unconscious UX interventions (nudges, defaults) to fully conscious (education, rational persuasion).",
      "keywords": ["Spectrum of Thinking Interventions", "unconscious intervention", "conscious intervention", "nudge", "default", "choice architecture", "persuasive design", "ethical design", "autonomy-preserving"]
    },
    {
      "id": "behavioral_buzzwords",
      "name": "Behavioral Science Core Concepts",
      "description": "Key vocabulary: Nudge Theory, Persuasive Technology, Behavior Design, Behavioral Science, and Behavioral Economics.",
      "keywords": ["Nudge Theory", "Persuasive Technology", "Behavior Design", "Behavioral Science", "Behavioral Economics", "Thaler", "Sunstein", "choice architecture", "libertarian paternalism"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Behavioral framework documentation referencing Fogg, Hook Model, or CREATE",
        "detection": "content_analysis",
        "pattern": "Fogg|B=MAP|Hook Model|CREATE Action|Dual Process|System 1|System 2|habit loop|Nudge Theory|Behavioral Economics",
        "strength": 0.8,
        "maps_to": [
          "ux_behavior_frameworks.fogg_behavior_model",
          "ux_behavior_frameworks.hook_model",
          "ux_behavior_frameworks.create_action_funnel",
          "ux_behavior_frameworks.dual_process_theory",
          "ux_behavior_frameworks.behavioral_buzzwords"
        ]
      },
      {
        "signal": "UX research reports or case studies applying behavioral frameworks",
        "detection": "file_presence",
        "pattern": "behavioral-design|behavior-framework|ux-research|persuasive-design",
        "strength": 0.7,
        "maps_to": [
          "ux_behavior_frameworks.fogg_behavior_model",
          "ux_behavior_frameworks.spectrum_of_thinking_interventions",
          "ux_behavior_frameworks.cue_routine_reward"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Applied behavioral frameworks (Fogg, Hook Model, CREATE) in UX design process",
        "strength": 0.8,
        "maps_to": [
          "ux_behavior_frameworks.fogg_behavior_model",
          "ux_behavior_frameworks.hook_model",
          "ux_behavior_frameworks.create_action_funnel"
        ]
      },
      {
        "signal": "Behavioral economics, persuasive technology, or nudge theory referenced in work",
        "strength": 0.75,
        "maps_to": [
          "ux_behavior_frameworks.dual_process_theory",
          "ux_behavior_frameworks.behavioral_buzzwords",
          "ux_behavior_frameworks.spectrum_of_thinking_interventions"
        ]
      },
      {
        "signal": "Habit design, engagement loops, or retention mechanics described in project work",
        "strength": 0.75,
        "maps_to": [
          "ux_behavior_frameworks.cue_routine_reward",
          "ux_behavior_frameworks.hook_model",
          "ux_behavior_frameworks.fogg_behavior_grid"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Behavioral design, persuasive technology, or behavioral economics endorsed",
        "strength": 0.5,
        "maps_to": [
          "ux_behavior_frameworks.fogg_behavior_model",
          "ux_behavior_frameworks.behavioral_buzzwords",
          "ux_behavior_frameworks.dual_process_theory"
        ]
      },
      {
        "signal": "Hook Model, habit design, or engagement loop design mentioned",
        "strength": 0.5,
        "maps_to": [
          "ux_behavior_frameworks.hook_model",
          "ux_behavior_frameworks.cue_routine_reward",
          "ux_behavior_frameworks.fogg_behavior_grid"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["fogg_behavior_model", "dual_process_theory", "behavioral_buzzwords"],
      "description": "Understands B=MAP mechanics, differentiates System 1 vs System 2, and uses core behavioral science vocabulary."
    },
    "mid": {
      "expected_subskills": ["hook_model", "create_action_funnel", "cue_routine_reward"],
      "description": "Applies the Hook Model, CREATE funnel, and habit loop to design engagement and behavior change flows."
    },
    "senior": {
      "expected_subskills": ["fogg_behavior_grid", "spectrum_of_thinking_interventions"],
      "description": "Uses the Behavior Grid for strategic classification and reasons ethically across the full spectrum of interventions."
    }
  }
}

# 2–9: Skills are pre-generated and stored in knowledge-base/skills/ux-design/
# This script writes skill #1 programmatically and references the rest by file.
# To regenerate all skills from scratch, extend the skills dict following the same pattern
# and add entries to the loop below.

# Write skill files
for skill_id, skill_data in skills.items():
    path = os.path.join(skills_dir, f"{skill_id}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(skill_data, f, indent=2, ensure_ascii=False)
    print(f"  Written: {path}")

print(f"\nSkills generated: {len(skills)}")
print("Note: Remaining 8 skill files were generated directly and exist in knowledge-base/skills/ux-design/")

# ─────────────────────────────────────────────────────────────
# ROLES
# ─────────────────────────────────────────────────────────────

roles = {}

roles["junior"] = {
  "role_id": "ux_designer",
  "level": "junior",
  "title": "Junior UX Designer",
  "description": "Entry-level UX designer focused on foundational behavioral frameworks (Fogg B=MAP, Dual Process Theory), structured user research (proto-personas, user stories), lo-fi wireframes and simple flowcharts, core UX principles (KISS, progress visibility), effective CTAs and contextual help, and basic social proof patterns.",
  "experience_range": "0-2 years",
  "skills": [
    {"skill_id": "ux_behavior_frameworks", "importance": 0.9, "rationale": "Foundational B=MAP, System 1/2, and behavioral vocabulary is essential for grounding design decisions from day one."},
    {"skill_id": "ux_classifying_behavior", "importance": 0.9, "rationale": "Correctly defining product purpose, target outcome, and users (personas) is the prerequisite for any behavioral design work."},
    {"skill_id": "ux_deliverables_prototyping", "importance": 0.9, "rationale": "Wireframes, flowcharts, and layout principles are the core craft output for daily contribution."},
    {"skill_id": "ux_conceptual_design", "importance": 0.85, "rationale": "User stories and UX principles (KISS, progress visibility) ground design work in user needs."},
    {"skill_id": "ux_behavior_strategies", "importance": 0.8, "rationale": "Educating users, encouraging action, and applying basic defaults are essential junior skills."},
    {"skill_id": "ux_attention_context", "importance": 0.75, "rationale": "Designing CTAs, tooltips, and status indicators for fleeting attention is a high-frequency junior task."},
    {"skill_id": "ux_patterns_best_practices", "importance": 0.75, "rationale": "Visual salience, trust signals, and social proof patterns are core to any seniority level."},
    {"skill_id": "ux_business_model", "importance": 0.65, "rationale": "Reading a BMC and doing a basic competitor analysis aligns design with business context."},
    {"skill_id": "ux_measuring_impact", "importance": 0.6, "rationale": "Understanding A/B test basics and HEART establishes data literacy for design discussions."}
  ],
  "scoring": {
    "method": "weighted_average",
    "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
    "thresholds": {
      "not_ready": {"min": 0.0, "max": 0.3, "label": "Not Ready", "description": "Significant gaps in behavioral fundamentals, wireframing craft, or user research."},
      "developing": {"min": 0.3, "max": 0.5, "label": "Developing", "description": "Can produce wireframes and user stories with guidance; needs coaching on behavioral framework application."},
      "approaching": {"min": 0.5, "max": 0.7, "label": "Approaching Ready", "description": "Solid Figma skills, understands B=MAP and dual process theory, produces user research artifacts with minimal coaching."},
      "ready": {"min": 0.7, "max": 0.85, "label": "Ready", "description": "Independently runs user research, designs behaviorally-grounded wireframes, writes user stories, and applies core persuasive patterns."},
      "exceeds": {"min": 0.85, "max": 1.0, "label": "Exceeds Expectations", "description": "Exceeds junior expectations with early mid-level proficiency in competitor analysis, gamification basics, and A/B test participation."}
    }
  }
}

roles["mid"] = {
  "role_id": "ux_designer",
  "level": "mid",
  "title": "Mid-Level UX Designer",
  "description": "Mid-level UX designer independently driving the behavioral design process: applying Hook Model, CREATE funnel, and habit strategies; producing Customer Experience Maps and BPMN models; running Lean Canvas and competitive analysis; designing gamified engagement systems and multi-session onboarding; applying loss aversion, peer comparison, and implementation intention patterns; and interpreting A/B test results.",
  "experience_range": "2-5 years",
  "skills": [
    {"skill_id": "ux_behavior_frameworks", "importance": 0.95, "rationale": "Full framework mastery (Hook, CREATE, Behavior Grid, habit loop) is the differentiating mid-level capability."},
    {"skill_id": "ux_patterns_best_practices", "importance": 0.95, "rationale": "Independently selecting loss aversion, peer comparison, authority, urgency patterns for each behavioral context."},
    {"skill_id": "ux_behavior_strategies", "importance": 0.9, "rationale": "Independent strategy selection: conscious action, cheating, or habit formation based on behavioral diagnosis."},
    {"skill_id": "ux_attention_context", "importance": 0.9, "rationale": "Designing full engagement systems (gamification, goal trackers, tutorials) for sustained behavioral engagement."},
    {"skill_id": "ux_deliverables_prototyping", "importance": 0.85, "rationale": "Customer Experience Maps, BPMN models for complex flows, and hi-fi interactive prototypes for usability testing."},
    {"skill_id": "ux_conceptual_design", "importance": 0.85, "rationale": "Managing behavioral design backlogs, compelling success states, and scaffolded onboarding flows."},
    {"skill_id": "ux_business_model", "importance": 0.8, "rationale": "Lean Canvas for problem-solution fit, cross-industry inspirators, and SWOT-to-design synthesis."},
    {"skill_id": "ux_measuring_impact", "importance": 0.8, "rationale": "Correctly interpreting A/B test results, avoiding statistical pitfalls, and driving iterative design decisions."},
    {"skill_id": "ux_classifying_behavior", "importance": 0.75, "rationale": "Precise target outcome/actor/action definition to ensure behavioral interventions are correctly aimed."}
  ],
  "scoring": {
    "method": "weighted_average",
    "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
    "thresholds": {
      "not_ready": {"min": 0.0, "max": 0.3, "label": "Not Ready", "description": "Operates at junior level despite experience; lacks independent framework application and experiment literacy."},
      "developing": {"min": 0.3, "max": 0.5, "label": "Developing", "description": "Applies frameworks with guidance; needs support on experiment interpretation and complex strategy selection."},
      "approaching": {"min": 0.5, "max": 0.7, "label": "Approaching Ready", "description": "Independently applies most frameworks; designing gamification and onboarding flows; building experiment depth."},
      "ready": {"min": 0.7, "max": 0.85, "label": "Ready", "description": "Leads behavioral design end-to-end, applies full persuasive toolkit, interprets experiments, drives engagement systems."},
      "exceeds": {"min": 0.85, "max": 1.0, "label": "Exceeds Expectations", "description": "Exceeds mid-level with early senior proficiency in MVT, Five Forces, and EPC modeling."}
    }
  }
}

roles["senior"] = {
  "role_id": "ux_designer",
  "level": "senior",
  "title": "Senior UX Designer / Behavioral Design Lead",
  "description": "Senior UX Designer leading behavioral design strategy: selecting interventions across the full Spectrum with ethical rigor; designing habit disruption systems; architecting social influence ecosystems; applying Five Forces; designing multivariate experiments; governing ethical persuasive pattern use; and mentoring mid-level designers.",
  "experience_range": "5+ years",
  "skills": [
    {"skill_id": "ux_measuring_impact", "importance": 0.95, "rationale": "Leading multivariate experiments, HTE analysis, experimentation culture, and behavioral metrics in OKRs."},
    {"skill_id": "ux_patterns_best_practices", "importance": 0.95, "rationale": "Governing ethical persuasive pattern use at org level; optimizing complex conversion funnels."},
    {"skill_id": "ux_behavior_frameworks", "importance": 0.9, "rationale": "Behavior Grid classification and full Spectrum reasoning with ethical judgment."},
    {"skill_id": "ux_behavior_strategies", "importance": 0.9, "rationale": "Designing multi-strategy habit disruption programs at product and population scale."},
    {"skill_id": "ux_attention_context", "importance": 0.9, "rationale": "Architecting social influence ecosystems, viral sharing mechanics, and community-driven engagement."},
    {"skill_id": "ux_business_model", "importance": 0.85, "rationale": "Porter's Five Forces for competitive moat identification and long-term UX strategy investment."},
    {"skill_id": "ux_deliverables_prototyping", "importance": 0.8, "rationale": "EPC enterprise process models and cross-team deliverable standard governance."},
    {"skill_id": "ux_conceptual_design", "importance": 0.8, "rationale": "Establishing behavioral UX principles as design system standards and review governance."},
    {"skill_id": "ux_classifying_behavior", "importance": 0.75, "rationale": "Facilitating cross-functional behavioral alignment workshops and championing outcome-over-output culture."}
  ],
  "scoring": {
    "method": "weighted_average",
    "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
    "thresholds": {
      "not_ready": {"min": 0.0, "max": 0.3, "label": "Not Ready", "description": "Significant gaps in strategic behavioral design, experimentation leadership, or ethical governance."},
      "developing": {"min": 0.3, "max": 0.5, "label": "Developing", "description": "Strong mid-level skills; lacks MVT, habit disruption systems, and strategic business model depth."},
      "approaching": {"min": 0.5, "max": 0.7, "label": "Approaching Ready", "description": "Leads behavioral design for product teams; refining MVT, social ecosystem design, and Porter's frameworks."},
      "ready": {"min": 0.7, "max": 0.85, "label": "Ready", "description": "Leads behavioral design strategy, governs ethical patterns, runs MVT, mentors mid-level designers."},
      "exceeds": {"min": 0.85, "max": 1.0, "label": "Exceeds Expectations", "description": "Principal/Staff Behavioral Design impact across multi-product organizations; recognized thought leadership."}
    }
  }
}

# Write role files
for level, role_data in roles.items():
    path = os.path.join(roles_dir, f"{level}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(role_data, f, indent=2, ensure_ascii=False)
    print(f"  Written: {path}")

print(f"\nRoles generated: {len(roles)}")

# ─────────────────────────────────────────────────────────────
# EVIDENCE (metadata stubs — full content in individual files)
# ─────────────────────────────────────────────────────────────

evidence_files = [
    ("cv.json", "CV / Resume Analysis - UX Designer"),
    ("linkedin.json", "LinkedIn Profile Analysis - UX Designer"),
    ("github.json", "GitHub Repository Analysis - UX Designer"),
    ("assessment.json", "Adaptive Technical Assessment - UX Designer"),
]

print("\nEvidence files (pre-generated, verifying existence):")
for filename, label in evidence_files:
    path = os.path.join(evidence_dir, filename)
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"  OK  {filename} ({size:,} bytes) — {label}")
    else:
        print(f"  MISSING  {filename} — {label}")

# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────

print("\n" + "="*60)
print("UX Designer knowledge-base generation complete.")
print("="*60)
print(f"Skills dir  : {skills_dir}")
print(f"Roles dir   : {roles_dir}")
print(f"Evidence dir: {evidence_dir}")

skill_files = [f for f in os.listdir(skills_dir) if f.endswith('.json')]
role_files  = [f for f in os.listdir(roles_dir) if f.endswith('.json')]
ev_files    = [f for f in os.listdir(evidence_dir) if f.endswith('.json')]

print(f"\nSkill files  : {len(skill_files)} — {', '.join(sorted(skill_files))}")
print(f"Role files   : {len(role_files)} — {', '.join(sorted(role_files))}")
print(f"Evidence files: {len(ev_files)} — {', '.join(sorted(ev_files))}")
print("\nDone.")
