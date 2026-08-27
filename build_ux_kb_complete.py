import os
import json

base_dir = os.path.abspath('knowledge-base')
skills_dir = os.path.join(base_dir, 'skills', 'ux-design')
evidence_dir = os.path.join(base_dir, 'evidence', 'ux-designer')
roles_dir = os.path.join(base_dir, 'roles', 'ux-designer')

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

skills = {}

# 1. ux_attention_context
skills["ux_attention_context"] = {
  "skill_id": "ux_attention_context",
  "name": "Attention Management & Contextual Design",
  "category": "ux_behavioral_science",
  "description": "Strategies for capturing and maintaining user attention across fleeting and extended contexts, gamification, status reporting, notifications, multi-device continuity, and cognitive load mitigation.",
  "subskills": [
    {
      "id": "fleeting_attention_cta",
      "name": "Fleeting Attention & Call-to-Action Design",
      "description": "Designing high-visibility, single-focus CTAs for low-attention contexts.",
      "keywords": ["fleeting attention", "CTA", "call to action", "visual contrast", "single action", "above the fold", "glanceable UI"]
    },
    {
      "id": "fleeting_attention_status_reports",
      "name": "Status Reports & Progress Snapshots",
      "description": "Providing lightweight status updates that communicate progress in seconds.",
      "keywords": ["status reports", "progress update", "dashboard widget", "glanceable", "digest", "summary card"]
    },
    {
      "id": "fleeting_attention_tips",
      "name": "Contextual Micro-Tips & Prompt Injection",
      "description": "Delivering timely, contextual micro-tips without breaking primary task flow.",
      "keywords": ["micro-tips", "contextual help", "tooltips", "just-in-time info", "onboarding tip", "inline help"]
    },
    {
      "id": "many_chances_gamification",
      "name": "Gamification & Progressive Challenges",
      "description": "Engaging users with repeated interaction loops through gamification, badges, streaks, and progress bars.",
      "keywords": ["gamification", "streaks", "badges", "progress bar", "points", "leaderboard", "reward schedule"]
    },
    {
      "id": "many_chances_planners",
      "name": "Planners, Scheduling & Habit Trackers",
      "description": "Designing interactive planning tools, calendar integrations, and scheduling helpers.",
      "keywords": ["planners", "scheduling", "habit tracker", "goal setting", "calendar sync", "task list"]
    },
    {
      "id": "many_chances_tutorials",
      "name": "Interactive Onboarding & Progressive Tutorials",
      "description": "Structuring multi-step walkthroughs, sandboxes, and interactive product tours.",
      "keywords": ["interactive tutorials", "walkthrough", "product tour", "progressive onboarding", "sandbox"]
    },
    {
      "id": "many_chances_social_sharing",
      "name": "Social Proof & Achievement Sharing Loops",
      "description": "Designing shareable milestone artifacts and peer comparison features.",
      "keywords": ["social sharing", "milestone card", "peer comparison", "viral loop", "achievement share"]
    },
    {
      "id": "multi_device_attention_continuity",
      "name": "Cross-Device State & Attention Continuity",
      "description": "Preserving user context across mobile, web, and wearable transitions with state persistence.",
      "keywords": ["cross-device continuity", "state handoff", "context preservation", "interruption recovery", "responsive attention"]
    },
    {
      "id": "cognitive_overload_mitigation_calm_tech",
      "name": "Calm Technology & Attention Budgeting",
      "description": "Mitigating notification fatigue, progressive disclosure of dense enterprise data, and ambient UX.",
      "keywords": ["calm technology", "attention budget", "notification triage", "cognitive load reduction", "ambient UX", "information density"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "CTA components, notification badge managers, and gamified streak counters",
        "detection": "content_analysis",
        "pattern": "StreakCounter|BadgeProgress|Gamification|NotificationBell|CallToAction",
        "strength": 0.85,
        "maps_to": [
          "ux_attention_context.fleeting_attention_cta",
          "ux_attention_context.many_chances_gamification",
          "ux_attention_context.fleeting_attention_status_reports",
          "ux_attention_context.fleeting_attention_tips"
        ]
      },
      {
        "signal": "Cross-device state sync hooks, planner scheduling tools, and onboarding walkthroughs",
        "detection": "content_analysis",
        "pattern": "ProductTour|OnboardingTutorial|useDeviceSync|HabitTracker|AttentionManager",
        "strength": 0.9,
        "maps_to": [
          "ux_attention_context.many_chances_planners",
          "ux_attention_context.many_chances_tutorials",
          "ux_attention_context.many_chances_social_sharing",
          "ux_attention_context.multi_device_attention_continuity",
          "ux_attention_context.cognitive_overload_mitigation_calm_tech"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Designed gamification loops, habit-tracking planners, and reduced notification dropoff by 35%",
        "strength": 0.6,
        "maps_to": [
          "ux_attention_context.fleeting_attention_cta",
          "ux_attention_context.many_chances_gamification",
          "ux_attention_context.many_chances_planners",
          "ux_attention_context.many_chances_tutorials"
        ]
      },
      {
        "signal": "Architected calm tech notification systems and cross-device contextual continuity for enterprise SaaS",
        "strength": 0.6,
        "maps_to": [
          "ux_attention_context.many_chances_social_sharing",
          "ux_attention_context.multi_device_attention_continuity",
          "ux_attention_context.cognitive_overload_mitigation_calm_tech",
          "ux_attention_context.fleeting_attention_status_reports",
          "ux_attention_context.fleeting_attention_tips"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in Behavioral UX, Gamification Design, User Attention Management, and Onboarding UX",
        "strength": 0.4,
        "maps_to": [
          "ux_attention_context.fleeting_attention_cta",
          "ux_attention_context.fleeting_attention_status_reports",
          "ux_attention_context.fleeting_attention_tips",
          "ux_attention_context.many_chances_gamification",
          "ux_attention_context.many_chances_planners",
          "ux_attention_context.many_chances_tutorials",
          "ux_attention_context.many_chances_social_sharing",
          "ux_attention_context.multi_device_attention_continuity",
          "ux_attention_context.cognitive_overload_mitigation_calm_tech"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes attention management and contextual UX assessment covering glanceable CTAs, gamification, cross-device state, and calm tech",
        "strength": 1.0,
        "maps_to": [
          "ux_attention_context.fleeting_attention_cta",
          "ux_attention_context.fleeting_attention_status_reports",
          "ux_attention_context.fleeting_attention_tips",
          "ux_attention_context.many_chances_gamification",
          "ux_attention_context.many_chances_planners",
          "ux_attention_context.many_chances_tutorials",
          "ux_attention_context.many_chances_social_sharing",
          "ux_attention_context.multi_device_attention_continuity",
          "ux_attention_context.cognitive_overload_mitigation_calm_tech"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "fleeting_attention_cta",
        "fleeting_attention_tips",
        "fleeting_attention_status_reports"
      ],
      "description": "Designs high-contrast glanceable CTAs, contextual micro-tips, and lightweight status summary widgets."
    },
    "mid": {
      "expected_subskills": [
        "many_chances_gamification",
        "many_chances_planners",
        "many_chances_tutorials"
      ],
      "description": "Builds interactive onboarding walkthroughs, gamification streak systems, and goal planners."
    },
    "senior": {
      "expected_subskills": [
        "many_chances_social_sharing",
        "multi_device_attention_continuity",
        "cognitive_overload_mitigation_calm_tech"
      ],
      "description": "Architects cross-device attention preservation, designs calm tech notification hierarchies, and optimizes social sharing loops."
    }
  }
}

# 2. ux_behavior_frameworks
skills["ux_behavior_frameworks"] = {
  "skill_id": "ux_behavior_frameworks",
  "name": "Human Behavior Frameworks & Theories",
  "category": "ux_behavioral_science",
  "description": "Theoretical behavioral models: BJ Fogg's B=MAP, Hook Model, CREATE Funnel, Dual Process Theory, Cue-Routine-Reward, Spectrum of Interventions, and Behavioral Ethics.",
  "subskills": [
    {
      "id": "fogg_behavior_model",
      "name": "BJ Fogg's Behavior Model (B=MAP)",
      "description": "Behavior = Motivation x Ability x Prompt. Convergence above the action line.",
      "keywords": ["B=MAP", "Fogg Behavior Model", "motivation", "ability", "prompt", "action line", "Tiny Habits"]
    },
    {
      "id": "dual_process_theory",
      "name": "Dual Process Theory (System 1 & System 2)",
      "description": "Kahneman's cognitive framework distinguishing fast automatic from slow deliberative thinking.",
      "keywords": ["Dual Process Theory", "System 1", "System 2", "Kahneman", "heuristics", "cognitive biases", "fast thinking"]
    },
    {
      "id": "behavioral_buzzwords",
      "name": "Behavioral Science Foundations & Heuristics",
      "description": "Anchoring, availability heuristic, framing effects, endowment effect, and cognitive fluency.",
      "keywords": ["anchoring", "availability heuristic", "framing", "endowment effect", "cognitive fluency", "nudge"]
    },
    {
      "id": "hook_model",
      "name": "Nir Eyal's Hook Model",
      "description": "Four-phase habit loop: Trigger -> Action -> Variable Reward -> Investment.",
      "keywords": ["Hook Model", "Trigger", "Action", "Variable Reward", "Investment", "internal trigger", "stored value"]
    },
    {
      "id": "create_action_funnel",
      "name": "CREATE Action Funnel (Stephen Wendel)",
      "description": "Six-stage behavioral funnel: Cue, Reaction, Evaluation, Ability, Timing, Experience.",
      "keywords": ["CREATE", "Cue", "Reaction", "Evaluation", "Ability", "Timing", "Experience", "Wendel", "behavioral funnel"]
    },
    {
      "id": "cue_routine_reward",
      "name": "Cue-Routine-Reward Habit Loop (Duhigg)",
      "description": "Charles Duhigg's habit loop: cue triggers a routine that delivers a craving-satisfying reward.",
      "keywords": ["Cue-Routine-Reward", "habit loop", "Duhigg", "Power of Habit", "craving", "routine", "habit change"]
    },
    {
      "id": "fogg_behavior_grid",
      "name": "BJ Fogg's Behavior Grid (15 Behavior Types)",
      "description": "Classifying behaviors across 15 types (Green, Blue, Purple, Gray, Black x Dot, Span, Path).",
      "keywords": ["Behavior Grid", "green behavior", "blue behavior", "purple behavior", "gray behavior", "black behavior", "one-time behavior"]
    },
    {
      "id": "spectrum_of_thinking_interventions",
      "name": "Spectrum of Thinking Interventions",
      "description": "Graduating interventions from unconscious nudges to conscious deliberation tools.",
      "keywords": ["spectrum of thinking", "conscious vs unconscious", "nudge spectrum", "educational intervention", "persuasive UX"]
    },
    {
      "id": "behavioral_ethics_dark_patterns_defense",
      "name": "Behavioral Ethics & Deceptive Design Defense",
      "description": "Auditing behavioral loops for ethical compliance, avoiding manipulative dark patterns and sludge.",
      "keywords": ["dark patterns", "deceptive design", "sludge", "confirmshaming", "roach motel", "ethical nudge", "user agency"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Design documentation analyzing B=MAP, Hook Model loops, or dark pattern defense audits",
        "detection": "content_analysis",
        "pattern": "Fogg|B=MAP|HookModel|VariableReward|DarkPatterns|CREATEFunnel",
        "strength": 0.85,
        "maps_to": [
          "ux_behavior_frameworks.fogg_behavior_model",
          "ux_behavior_frameworks.hook_model",
          "ux_behavior_frameworks.create_action_funnel",
          "ux_behavior_frameworks.dual_process_theory",
          "ux_behavior_frameworks.behavioral_buzzwords",
          "ux_behavior_frameworks.cue_routine_reward",
          "ux_behavior_frameworks.fogg_behavior_grid",
          "ux_behavior_frameworks.spectrum_of_thinking_interventions",
          "ux_behavior_frameworks.behavioral_ethics_dark_patterns_defense"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Applied Fogg B=MAP, Hook Model, and CREATE funnels to improve activation and retention metrics",
        "strength": 0.6,
        "maps_to": [
          "ux_behavior_frameworks.fogg_behavior_model",
          "ux_behavior_frameworks.hook_model",
          "ux_behavior_frameworks.create_action_funnel",
          "ux_behavior_frameworks.dual_process_theory",
          "ux_behavior_frameworks.behavioral_buzzwords"
        ]
      },
      {
        "signal": "Conducted behavioral ethics audits eliminating dark patterns and mapped Fogg Behavior Grid interventions",
        "strength": 0.6,
        "maps_to": [
          "ux_behavior_frameworks.cue_routine_reward",
          "ux_behavior_frameworks.fogg_behavior_grid",
          "ux_behavior_frameworks.spectrum_of_thinking_interventions",
          "ux_behavior_frameworks.behavioral_ethics_dark_patterns_defense"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in Behavioral Design, Cognitive Psychology, Hook Model, and Behavioral Economics",
        "strength": 0.4,
        "maps_to": [
          "ux_behavior_frameworks.fogg_behavior_model",
          "ux_behavior_frameworks.dual_process_theory",
          "ux_behavior_frameworks.behavioral_buzzwords",
          "ux_behavior_frameworks.hook_model",
          "ux_behavior_frameworks.create_action_funnel",
          "ux_behavior_frameworks.cue_routine_reward",
          "ux_behavior_frameworks.fogg_behavior_grid",
          "ux_behavior_frameworks.spectrum_of_thinking_interventions",
          "ux_behavior_frameworks.behavioral_ethics_dark_patterns_defense"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes behavioral frameworks assessment covering B=MAP, CREATE funnel, Hook Model, Fogg Grid, and Dark Pattern audits",
        "strength": 1.0,
        "maps_to": [
          "ux_behavior_frameworks.fogg_behavior_model",
          "ux_behavior_frameworks.dual_process_theory",
          "ux_behavior_frameworks.behavioral_buzzwords",
          "ux_behavior_frameworks.hook_model",
          "ux_behavior_frameworks.create_action_funnel",
          "ux_behavior_frameworks.cue_routine_reward",
          "ux_behavior_frameworks.fogg_behavior_grid",
          "ux_behavior_frameworks.spectrum_of_thinking_interventions",
          "ux_behavior_frameworks.behavioral_ethics_dark_patterns_defense"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "fogg_behavior_model",
        "dual_process_theory",
        "behavioral_buzzwords"
      ],
      "description": "Applies Fogg B=MAP motivation/ability/prompt concepts and accounts for System 1 heuristics."
    },
    "mid": {
      "expected_subskills": [
        "hook_model",
        "create_action_funnel",
        "cue_routine_reward"
      ],
      "description": "Designs variable reward loops in the Hook Model and diagnoses drop-offs with the CREATE action funnel."
    },
    "senior": {
      "expected_subskills": [
        "fogg_behavior_grid",
        "spectrum_of_thinking_interventions",
        "behavioral_ethics_dark_patterns_defense"
      ],
      "description": "Selects strategic interventions across the 15-cell Fogg Grid, audits dark patterns, and enforces ethical user agency."
    }
  }
}

# 3. ux_behavior_strategies
skills["ux_behavior_strategies"] = {
  "skill_id": "ux_behavior_strategies",
  "name": "Behavioral Intervention & Nudge Strategies",
  "category": "ux_behavioral_science",
  "description": "Selecting and implementing behavioral strategies: defaulting, educational nudges, habit disruption, automation, choice architecture framing, and constructive friction.",
  "subskills": [
    {
      "id": "educate_encourage",
      "name": "Educational Framing & Encouragement Nudges",
      "description": "Using informative framing, micro-copy, and timely encouragement to guide user action.",
      "keywords": ["educate and encourage", "positive framing", "encouragement", "micro-copy", "behavioral nudge"]
    },
    {
      "id": "defaulting",
      "name": "Defaulting & Opt-In/Opt-Out Architecture",
      "description": "Setting smart, ethical pre-selected defaults to harness status quo bias.",
      "keywords": ["defaulting", "status quo bias", "opt-in", "opt-out", "smart default", "pre-selected choice"]
    },
    {
      "id": "choice_architecture_framing",
      "name": "Choice Architecture & Decoy Effects",
      "description": "Structuring option sets, decoy effects, tier pricing tables, and reducing choice overload.",
      "keywords": ["choice architecture", "decoy effect", "choice overload", "loss framing", "tier comparison", "anchoring option"]
    },
    {
      "id": "help_think_about_action",
      "name": "Reflective Prompting & Cognitive Pauses",
      "description": "Injecting prompts that encourage users to consciously evaluate options before committing.",
      "keywords": ["help think about action", "reflective prompt", "cognitive pause", "commitment device", "decision support"]
    },
    {
      "id": "making_it_incidental",
      "name": "Incidental Action Pairing & Piggybacking",
      "description": "Attaching the desired target behavior to an action the user is already routinely performing.",
      "keywords": ["incidental action", "piggybacking", "habit stacking", "adjacent action", "seamless integration"]
    },
    {
      "id": "automate_new_behavior",
      "name": "Automation & Recurring Rules",
      "description": "Automating recurring behaviors (auto-invest, recurring orders, background sync).",
      "keywords": ["automate behavior", "recurring rule", "auto-save", "smart automation", "set-and-forget"]
    },
    {
      "id": "disrupt_existing_habit",
      "name": "Habit Disruption & Friction Insertion",
      "description": "Breaking unwanted automatic routines by introducing physical or cognitive friction.",
      "keywords": ["disrupt existing habit", "break habit", "friction insertion", "habit loop interruption", "pattern interrupt"]
    },
    {
      "id": "systemic_habit_ecosystem_design",
      "name": "Systemic Habit Ecosystems & Long-Term Retention",
      "description": "Designing multi-touchpoint behavioral feedback loops that sustain long-term engagement across lifecycles.",
      "keywords": ["habit ecosystem", "long-term retention", "multi-touchpoint UX", "behavioral retention", "lifecycle engagement"]
    },
    {
      "id": "friction_engineering_intentional_friction",
      "name": "Constructive Friction & High-Stakes Decision UX",
      "description": "Strategically introducing constructive friction for high-stakes decisions (security, financial confirmation, data deletion).",
      "keywords": ["constructive friction", "intentional friction", "destructive action confirmation", "speed bump UX", "error prevention"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Smart default form configurations, pricing tier selectors, and confirmation modal speed bumps",
        "detection": "content_analysis",
        "pattern": "PricingTier|SmartDefault|ConfirmModal|SpeedBump|HabitLoop|ChoiceArchitecture",
        "strength": 0.85,
        "maps_to": [
          "ux_behavior_strategies.educate_encourage",
          "ux_behavior_strategies.defaulting",
          "ux_behavior_strategies.choice_architecture_framing",
          "ux_behavior_strategies.help_think_about_action",
          "ux_behavior_strategies.making_it_incidental",
          "ux_behavior_strategies.automate_new_behavior",
          "ux_behavior_strategies.disrupt_existing_habit",
          "ux_behavior_strategies.systemic_habit_ecosystem_design",
          "ux_behavior_strategies.friction_engineering_intentional_friction"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Designed smart defaults and choice architecture increasing conversion by 28% while reducing checkout errors",
        "strength": 0.6,
        "maps_to": [
          "ux_behavior_strategies.educate_encourage",
          "ux_behavior_strategies.defaulting",
          "ux_behavior_strategies.choice_architecture_framing",
          "ux_behavior_strategies.help_think_about_action"
        ]
      },
      {
        "signal": "Engineered constructive friction for financial transfers and designed automated recurring habit ecosystems",
        "strength": 0.6,
        "maps_to": [
          "ux_behavior_strategies.making_it_incidental",
          "ux_behavior_strategies.automate_new_behavior",
          "ux_behavior_strategies.disrupt_existing_habit",
          "ux_behavior_strategies.systemic_habit_ecosystem_design",
          "ux_behavior_strategies.friction_engineering_intentional_friction"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Expertise in Behavioral Nudges, Choice Architecture, Friction Engineering, and Habit Design",
        "strength": 0.4,
        "maps_to": [
          "ux_behavior_strategies.educate_encourage",
          "ux_behavior_strategies.defaulting",
          "ux_behavior_strategies.choice_architecture_framing",
          "ux_behavior_strategies.help_think_about_action",
          "ux_behavior_strategies.making_it_incidental",
          "ux_behavior_strategies.automate_new_behavior",
          "ux_behavior_strategies.disrupt_existing_habit",
          "ux_behavior_strategies.systemic_habit_ecosystem_design",
          "ux_behavior_strategies.friction_engineering_intentional_friction"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes behavioral intervention assessment covering defaulting, choice architecture, habit disruption, and constructive friction",
        "strength": 1.0,
        "maps_to": [
          "ux_behavior_strategies.educate_encourage",
          "ux_behavior_strategies.defaulting",
          "ux_behavior_strategies.choice_architecture_framing",
          "ux_behavior_strategies.help_think_about_action",
          "ux_behavior_strategies.making_it_incidental",
          "ux_behavior_strategies.automate_new_behavior",
          "ux_behavior_strategies.disrupt_existing_habit",
          "ux_behavior_strategies.systemic_habit_ecosystem_design",
          "ux_behavior_strategies.friction_engineering_intentional_friction"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "educate_encourage",
        "defaulting",
        "choice_architecture_framing"
      ],
      "description": "Applies smart defaults, educational framing, and structures basic pricing/option comparisons."
    },
    "mid": {
      "expected_subskills": [
        "help_think_about_action",
        "making_it_incidental",
        "automate_new_behavior"
      ],
      "description": "Designs reflective decision prompts, pairs actions via habit stacking, and sets up automated recurring user rules."
    },
    "senior": {
      "expected_subskills": [
        "disrupt_existing_habit",
        "systemic_habit_ecosystem_design",
        "friction_engineering_intentional_friction"
      ],
      "description": "Architects long-term habit ecosystems, engineers constructive friction for high-risk operations, and disrupts unwanted routines."
    }
  }
}

# 4. ux_business_model
skills["ux_business_model"] = {
  "skill_id": "ux_business_model",
  "name": "UX Business Modeling & Product Strategy",
  "category": "ux_business_strategy",
  "description": "Aligning user experience with business models: Business Model Canvas, Lean Canvas, Value Proposition Canvas, competitor analysis, unit economics, and Product-Led Growth (PLG).",
  "subskills": [
    {
      "id": "business_model_canvas",
      "name": "Business Model Canvas (Osterwalder)",
      "description": "Mapping product vision across 9 building blocks: value propositions, customer segments, channels, revenue streams, and cost structures.",
      "keywords": ["Business Model Canvas", "Osterwalder", "value proposition", "customer segments", "revenue streams", "channels", "cost structure"]
    },
    {
      "id": "competitor_analysis",
      "name": "Competitive UX Benchmarking & Feature Matrix",
      "description": "Analyzing competitor flows, heuristic benchmarking, and feature differentiation matrices.",
      "keywords": ["competitor analysis", "competitive UX", "benchmarking", "feature matrix", "direct competitors", "indirect competitors"]
    },
    {
      "id": "value_proposition_design_canvas",
      "name": "Value Proposition Design & Customer Profile Mapping",
      "description": "Mapping customer jobs, pains, and gains to product pain relievers and gain creators.",
      "keywords": ["Value Proposition Canvas", "customer jobs", "pains and gains", "pain relievers", "gain creators", "problem-solution fit"]
    },
    {
      "id": "lean_canvas",
      "name": "Lean Canvas (Ash Maurya)",
      "description": "Fast-iteration canvas focusing on problem, solution, unique value proposition, unfair advantage, and early adopters.",
      "keywords": ["Lean Canvas", "Ash Maurya", "unfair advantage", "early adopters", "UVP", "lean startup"]
    },
    {
      "id": "inspirator_analysis",
      "name": "Inspirator Analysis & Cross-Industry Analogues",
      "description": "Drawing analog UX patterns from non-competing industries (e.g. applying gaming onboarding to fintech).",
      "keywords": ["inspirator analysis", "cross-industry analogues", "analogous design", "inspirational benchmarks", "pattern borrowing"]
    },
    {
      "id": "swot_analysis",
      "name": "UX SWOT Analysis",
      "description": "Assessing product experience Strengths, Weaknesses, Opportunities, and Threats against market trends.",
      "keywords": ["SWOT analysis", "strengths", "weaknesses", "opportunities", "threats", "strategic UX"]
    },
    {
      "id": "five_forces",
      "name": "Porter's Five Forces & Industry UX Defensibility",
      "description": "Evaluating industry competitiveness, buyer power, substitution threat, and switching costs in UX design.",
      "keywords": ["Five Forces", "Porter", "switching costs", "buyer power", "threat of substitution", "defensibility"]
    },
    {
      "id": "unit_economics_ux_monetization",
      "name": "SaaS Unit Economics & Monetization UX",
      "description": "Aligning UX design with SaaS unit economics: Customer Acquisition Cost (CAC), Lifetime Value (LTV), payback period, and churn reduction.",
      "keywords": ["unit economics", "CAC", "LTV", "payback period", "churn reduction", "monetization UX", "pricing psychology"]
    },
    {
      "id": "product_led_growth_ux_mechanics",
      "name": "Product-Led Growth (PLG) & Time-to-Value (TTV)",
      "description": "Designing frictionless self-service onboarding, virality loops, freemium-to-paid conversion thresholds, and minimizing TTV.",
      "keywords": ["Product-Led Growth", "PLG", "Time-to-Value", "TTV", "freemium conversion", "viral loop", "self-service onboarding"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Product strategy docs, Value Proposition Canvas files, and pricing tier UX components",
        "detection": "content_analysis",
        "pattern": "LeanCanvas|ValueProposition|PLG|TimeToValue|PricingTable|CompetitorMatrix",
        "strength": 0.85,
        "maps_to": [
          "ux_business_model.business_model_canvas",
          "ux_business_model.competitor_analysis",
          "ux_business_model.value_proposition_design_canvas",
          "ux_business_model.lean_canvas",
          "ux_business_model.inspirator_analysis",
          "ux_business_model.swot_analysis",
          "ux_business_model.five_forces",
          "ux_business_model.unit_economics_ux_monetization",
          "ux_business_model.product_led_growth_ux_mechanics"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Formulated Lean Canvases and mapped Value Proposition Canvases driving product-market fit for B2B SaaS",
        "strength": 0.6,
        "maps_to": [
          "ux_business_model.business_model_canvas",
          "ux_business_model.competitor_analysis",
          "ux_business_model.value_proposition_design_canvas",
          "ux_business_model.lean_canvas"
        ]
      },
      {
        "signal": "Led Product-Led Growth (PLG) UX redesign decreasing Time-to-Value from 3 days to 8 minutes and boosting LTV/CAC",
        "strength": 0.6,
        "maps_to": [
          "ux_business_model.inspirator_analysis",
          "ux_business_model.swot_analysis",
          "ux_business_model.five_forces",
          "ux_business_model.unit_economics_ux_monetization",
          "ux_business_model.product_led_growth_ux_mechanics"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in Product Strategy, Business Model Innovation, Product-Led Growth, and SaaS Unit Economics",
        "strength": 0.4,
        "maps_to": [
          "ux_business_model.business_model_canvas",
          "ux_business_model.competitor_analysis",
          "ux_business_model.value_proposition_design_canvas",
          "ux_business_model.lean_canvas",
          "ux_business_model.inspirator_analysis",
          "ux_business_model.swot_analysis",
          "ux_business_model.five_forces",
          "ux_business_model.unit_economics_ux_monetization",
          "ux_business_model.product_led_growth_ux_mechanics"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes UX business model assessment covering Osterwalder Canvas, Value Proposition mapping, SaaS unit economics, and PLG onboarding funnels",
        "strength": 1.0,
        "maps_to": [
          "ux_business_model.business_model_canvas",
          "ux_business_model.competitor_analysis",
          "ux_business_model.value_proposition_design_canvas",
          "ux_business_model.lean_canvas",
          "ux_business_model.inspirator_analysis",
          "ux_business_model.swot_analysis",
          "ux_business_model.five_forces",
          "ux_business_model.unit_economics_ux_monetization",
          "ux_business_model.product_led_growth_ux_mechanics"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "business_model_canvas",
        "competitor_analysis",
        "value_proposition_design_canvas"
      ],
      "description": "Maps Osterwalder Business Model Canvases, analyzes competitor flows, and matches pains to gain creators."
    },
    "mid": {
      "expected_subskills": [
        "lean_canvas",
        "inspirator_analysis",
        "swot_analysis"
      ],
      "description": "Builds Lean Canvases for rapid validation, conducts cross-industry inspirator analyses, and executes SWOT assessments."
    },
    "senior": {
      "expected_subskills": [
        "five_forces",
        "unit_economics_ux_monetization",
        "product_led_growth_ux_mechanics"
      ],
      "description": "Aligns product UX with SaaS unit economics (LTV/CAC), optimizes PLG self-service conversion, and builds switching cost defensibility."
    }
  }
}

# 5. ux_classifying_behavior
skills["ux_classifying_behavior"] = {
  "skill_id": "ux_classifying_behavior",
  "name": "Behavioral Discovery & User Segmentation",
  "category": "ux_behavioral_science",
  "description": "Methods for discovering and defining target behaviors: Target Outcome vs Action, Actor profiling, Personas, Jobs-to-be-Done (JTBD), behavioral clustering, and dynamic intent state modeling.",
  "subskills": [
    {
      "id": "clarify_product",
      "name": "Product Clarification & Value Scope",
      "description": "Articulating the core value proposition and boundary scope of the product.",
      "keywords": ["clarify product", "product scope", "value proposition", "core value", "product definition"]
    },
    {
      "id": "user_personas",
      "name": "User Personas & Empathy Mapping",
      "description": "Creating evidence-based personas, empathy maps, and behavioral archetypes.",
      "keywords": ["personas", "empathy map", "user archetype", "behavioral persona", "demographic vs behavioral"]
    },
    {
      "id": "jobs_to_be_done_framework",
      "name": "Jobs-to-be-Done (JTBD) Theory",
      "description": "Formulating JTBD statements: Situation -> Motivation -> Desired Outcome.",
      "keywords": ["Jobs to be Done", "JTBD", "customer jobs", "job statement", "functional job", "emotional job", "social job"]
    },
    {
      "id": "target_outcome",
      "name": "Target Outcome Definition & Metrics",
      "description": "Defining the measurable business and user outcomes the product aims to achieve.",
      "keywords": ["target outcome", "outcome metric", "business goal", "user goal", "success metric"]
    },
    {
      "id": "target_actor",
      "name": "Target Actor & Stakeholder Profiling",
      "description": "Identifying the specific individual or stakeholder who must perform the target action.",
      "keywords": ["target actor", "actor profiling", "stakeholder", "decision maker", "primary actor"]
    },
    {
      "id": "target_action",
      "name": "Target Action Specification & Granularity",
      "description": "Defining specific, observable, and measurable target actions (when, where, how).",
      "keywords": ["target action", "observable action", "action specification", "action granularity", "discrete behavior"]
    },
    {
      "id": "behavioral_segmentation_clustering",
      "name": "Behavioral Segmentation & Quantitative Clustering",
      "description": "Segmenting users by usage patterns, frequency, and friction points rather than purely demographic attributes.",
      "keywords": ["behavioral segmentation", "clustering", "usage frequency", "power users vs casual", "cohort segmentation"]
    },
    {
      "id": "cross_actor_ecosystem_mapping",
      "name": "Multi-Sided Platform Actor Ecosystems",
      "description": "Mapping interconnected behaviors in multi-sided platforms (e.g. buyers, sellers, admins).",
      "keywords": ["multi-sided platform", "ecosystem mapping", "cross-actor interactions", "two-sided marketplace UX"]
    },
    {
      "id": "intent_state_modeling",
      "name": "Dynamic Intent State Modeling",
      "description": "Modeling dynamic user intent transitions (exploratory, goal-directed, transactional, disengaged).",
      "keywords": ["intent states", "dynamic intent", "exploratory intent", "transactional intent", "state transition UX"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Persona profiles, JTBD job maps, and behavioral segmentation models in design docs",
        "detection": "content_analysis",
        "pattern": "Persona|JTBD|JobsToBeDone|TargetAction|BehavioralSegment|IntentState",
        "strength": 0.85,
        "maps_to": [
          "ux_classifying_behavior.clarify_product",
          "ux_classifying_behavior.user_personas",
          "ux_classifying_behavior.jobs_to_be_done_framework",
          "ux_classifying_behavior.target_outcome",
          "ux_classifying_behavior.target_actor",
          "ux_classifying_behavior.target_action",
          "ux_classifying_behavior.behavioral_segmentation_clustering",
          "ux_classifying_behavior.cross_actor_ecosystem_mapping",
          "ux_classifying_behavior.intent_state_modeling"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Conducted user research formulating JTBD frameworks, behavioral personas, and target action specifications",
        "strength": 0.6,
        "maps_to": [
          "ux_classifying_behavior.clarify_product",
          "ux_classifying_behavior.user_personas",
          "ux_classifying_behavior.jobs_to_be_done_framework",
          "ux_classifying_behavior.target_outcome"
        ]
      },
      {
        "signal": "Designed multi-sided platform actor ecosystems and implemented behavioral clustering with dynamic intent modeling",
        "strength": 0.6,
        "maps_to": [
          "ux_classifying_behavior.target_actor",
          "ux_classifying_behavior.target_action",
          "ux_classifying_behavior.behavioral_segmentation_clustering",
          "ux_classifying_behavior.cross_actor_ecosystem_mapping",
          "ux_classifying_behavior.intent_state_modeling"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in User Personas, Jobs-to-be-Done (JTBD), Behavioral Research, and Customer Discovery",
        "strength": 0.4,
        "maps_to": [
          "ux_classifying_behavior.clarify_product",
          "ux_classifying_behavior.user_personas",
          "ux_classifying_behavior.jobs_to_be_done_framework",
          "ux_classifying_behavior.target_outcome",
          "ux_classifying_behavior.target_actor",
          "ux_classifying_behavior.target_action",
          "ux_classifying_behavior.behavioral_segmentation_clustering",
          "ux_classifying_behavior.cross_actor_ecosystem_mapping",
          "ux_classifying_behavior.intent_state_modeling"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes behavioral classification assessment covering JTBD statements, target action definitions, behavioral clustering, and multi-sided actor ecosystems",
        "strength": 1.0,
        "maps_to": [
          "ux_classifying_behavior.clarify_product",
          "ux_classifying_behavior.user_personas",
          "ux_classifying_behavior.jobs_to_be_done_framework",
          "ux_classifying_behavior.target_outcome",
          "ux_classifying_behavior.target_actor",
          "ux_classifying_behavior.target_action",
          "ux_classifying_behavior.behavioral_segmentation_clustering",
          "ux_classifying_behavior.cross_actor_ecosystem_mapping",
          "ux_classifying_behavior.intent_state_modeling"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "clarify_product",
        "user_personas",
        "jobs_to_be_done_framework"
      ],
      "description": "Articulates core product value, creates evidence-based personas, and writes JTBD job statements."
    },
    "mid": {
      "expected_subskills": [
        "target_outcome",
        "target_actor",
        "target_action"
      ],
      "description": "Defines discrete target actions, profiles target actors, and sets measurable outcome metrics."
    },
    "senior": {
      "expected_subskills": [
        "behavioral_segmentation_clustering",
        "cross_actor_ecosystem_mapping",
        "intent_state_modeling"
      ],
      "description": "Executes quantitative behavioral segmentation, maps multi-sided marketplace ecosystems, and models dynamic intent states."
    }
  }
}

# 6. ux_conceptual_design
skills["ux_conceptual_design"] = {
  "skill_id": "ux_conceptual_design",
  "name": "Conceptual Design & Architecture Principles",
  "category": "ux_design_craft",
  "description": "Translating user research into conceptual structures: User Stories, Backlog, Scaffolding, Simplicity principles, Mental Model System Architecture, Design System Tokens, and Service Blueprinting.",
  "subskills": [
    {
      "id": "user_stories",
      "name": "User Stories & Acceptance Criteria",
      "description": "Writing user stories (As a... I want... So that...) with Gherkin acceptance criteria.",
      "keywords": ["user stories", "acceptance criteria", "Gherkin", "Given When Then", "INVEST criteria"]
    },
    {
      "id": "ux_principle_short_simple",
      "name": "Simplicity & Cognitive Load Minimization",
      "description": "Designing short, focused, minimal-step interactions (Hick's Law).",
      "keywords": ["short and simple", "Hick's law", "cognitive load", "minimalism", "step reduction"]
    },
    {
      "id": "ux_principle_progress_visible",
      "name": "Visibility of System Status & Progress",
      "description": "Providing real-time visual progress feedback, steppers, and breadcrumbs.",
      "keywords": ["progress visible", "system status", "steppers", "breadcrumbs", "loading states", "Nielsen heuristic 1"]
    },
    {
      "id": "product_backlog",
      "name": "Product Backlog Prioritization (MoSCoW / RICE)",
      "description": "Prioritizing UX features using MoSCoW, RICE, or Kano models.",
      "keywords": ["product backlog", "MoSCoW", "RICE scoring", "Kano model", "feature prioritization"]
    },
    {
      "id": "ux_principle_success_prominent",
      "name": "Prominent Success Feedback & Celebrations",
      "description": "Making task completion immediately clear with prominent confirmations and positive reinforcement.",
      "keywords": ["success feedback", "confirmation state", "positive reinforcement", "celebration animation", "feedback loop"]
    },
    {
      "id": "ux_principle_scaffolding",
      "name": "Scaffolding & Progressive Skill Building",
      "description": "Providing temporary support structures that fall away as the user gains competence.",
      "keywords": ["scaffolding", "progressive disclosure", "skill building", "onboarding ramp", "advanced mode toggle"]
    },
    {
      "id": "mental_model_system_architecture",
      "name": "Mental Model System Architecture",
      "description": "Aligning product conceptual models with user mental models to eliminate conceptual dissonance.",
      "keywords": ["mental model", "conceptual model", "conceptual dissonance", "system image", "information architecture", "Norman"]
    },
    {
      "id": "design_system_tokens_governance",
      "name": "Design System Tokens & Multi-Brand Governance",
      "description": "Architecting Design Tokens (color, typography, spacing, elevation) in Figma and code, multi-brand theming, and token governance.",
      "keywords": ["Design Tokens", "design system governance", "Style Dictionary", "Figma Variables", "multi-brand theming", "component library"]
    },
    {
      "id": "service_blueprint_orchestration",
      "name": "Service Blueprinting & Cross-Functional Touchpoints",
      "description": "Orchestrating frontstage customer actions with backstage employee processes and supporting technical systems.",
      "keywords": ["Service Blueprint", "frontstage", "backstage", "line of visibility", "support processes", "touchpoint orchestration"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Design token JSON definitions, Service Blueprint schemas, and User Story specifications",
        "detection": "content_analysis",
        "pattern": "design-tokens\\.json|tokens/.*\\.json|ServiceBlueprint|UserStory|AcceptanceCriteria",
        "strength": 0.9,
        "maps_to": [
          "ux_conceptual_design.user_stories",
          "ux_conceptual_design.ux_principle_short_simple",
          "ux_conceptual_design.ux_principle_progress_visible",
          "ux_conceptual_design.product_backlog",
          "ux_conceptual_design.ux_principle_success_prominent",
          "ux_conceptual_design.ux_principle_scaffolding",
          "ux_conceptual_design.mental_model_system_architecture",
          "ux_conceptual_design.design_system_tokens_governance",
          "ux_conceptual_design.service_blueprint_orchestration"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Wrote user stories with Gherkin acceptance criteria and prioritized backlogs with RICE scoring",
        "strength": 0.6,
        "maps_to": [
          "ux_conceptual_design.user_stories",
          "ux_conceptual_design.ux_principle_short_simple",
          "ux_conceptual_design.ux_principle_progress_visible",
          "ux_conceptual_design.product_backlog"
        ]
      },
      {
        "signal": "Architected enterprise Design Tokens in Figma and mapped end-to-end Service Blueprints for omni-channel platforms",
        "strength": 0.6,
        "maps_to": [
          "ux_conceptual_design.ux_principle_success_prominent",
          "ux_conceptual_design.ux_principle_scaffolding",
          "ux_conceptual_design.mental_model_system_architecture",
          "ux_conceptual_design.design_system_tokens_governance",
          "ux_conceptual_design.service_blueprint_orchestration"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in Conceptual Design, Design Systems, Service Design, and Information Architecture",
        "strength": 0.4,
        "maps_to": [
          "ux_conceptual_design.user_stories",
          "ux_conceptual_design.ux_principle_short_simple",
          "ux_conceptual_design.ux_principle_progress_visible",
          "ux_conceptual_design.product_backlog",
          "ux_conceptual_design.ux_principle_success_prominent",
          "ux_conceptual_design.ux_principle_scaffolding",
          "ux_conceptual_design.mental_model_system_architecture",
          "ux_conceptual_design.design_system_tokens_governance",
          "ux_conceptual_design.service_blueprint_orchestration"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes conceptual design assessment covering RICE backlog prioritization, Design Tokens tokenomics, Service Blueprinting, and mental model architecture",
        "strength": 1.0,
        "maps_to": [
          "ux_conceptual_design.user_stories",
          "ux_conceptual_design.ux_principle_short_simple",
          "ux_conceptual_design.ux_principle_progress_visible",
          "ux_conceptual_design.product_backlog",
          "ux_conceptual_design.ux_principle_success_prominent",
          "ux_conceptual_design.ux_principle_scaffolding",
          "ux_conceptual_design.mental_model_system_architecture",
          "ux_conceptual_design.design_system_tokens_governance",
          "ux_conceptual_design.service_blueprint_orchestration"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "user_stories",
        "ux_principle_short_simple",
        "ux_principle_progress_visible"
      ],
      "description": "Writes user stories with acceptance criteria, simplifies complex forms, and integrates progress steppers."
    },
    "mid": {
      "expected_subskills": [
        "product_backlog",
        "ux_principle_success_prominent",
        "ux_principle_scaffolding"
      ],
      "description": "Prioritizes backlogs with RICE/MoSCoW, creates scaffolding for new users, and crafts clear success confirmations."
    },
    "senior": {
      "expected_subskills": [
        "mental_model_system_architecture",
        "design_system_tokens_governance",
        "service_blueprint_orchestration"
      ],
      "description": "Architects enterprise Design Tokens across multi-brand systems, maps comprehensive Service Blueprints, and eliminates mental model dissonance."
    }
  }
}

# 7. ux_deliverables_prototyping
skills["ux_deliverables_prototyping"] = {
  "skill_id": "ux_deliverables_prototyping",
  "name": "Prototyping, Flowcharts & Design Specs",
  "category": "ux_design_craft",
  "description": "Creating UX deliverables: Customer Experience Maps, flowcharts, BPMN, wireframing in Figma, interactive high-fidelity logic prototyping, Design-to-Code handoff, and WCAG accessibility specs.",
  "subskills": [
    {
      "id": "wireframing_tools",
      "name": "Wireframing & Low-Fidelity Layouts",
      "description": "Low-fidelity wireframing in Figma, Balsamiq, or Whimsical to establish structural hierarchy.",
      "keywords": ["wireframing", "Figma", "low-fidelity", "Balsamiq", "Whimsical", "wireframe", "rapid layout"]
    },
    {
      "id": "simple_flowchart",
      "name": "User Flowcharts & Task Flows",
      "description": "Diagramming user decision points, alternate paths, and task flows.",
      "keywords": ["user flow", "flowchart", "decision point", "task flow", "branching logic", "swimlanes"]
    },
    {
      "id": "layout_rules",
      "name": "Grid Systems, Auto-Layout & Visual Hierarchy",
      "description": "Applying 8pt grid systems, auto-layout constraints in Figma, and visual hierarchy principles.",
      "keywords": ["grid system", "8pt grid", "auto-layout", "visual hierarchy", "spacing scale", "Figma constraints"]
    },
    {
      "id": "customer_experience_map",
      "name": "Customer Experience (CX) Journey Maps",
      "description": "End-to-end customer journey mapping including stages, user goals, touchpoints, emotions, and pain points.",
      "keywords": ["Customer Experience Map", "journey map", "touchpoints", "emotional curve", "pain points", "opportunities"]
    },
    {
      "id": "bpmn_diagram",
      "name": "BPMN Process Diagrams",
      "description": "Business Process Model and Notation (BPMN) diagrams for complex business logic workflows.",
      "keywords": ["BPMN", "Business Process Model", "gateway", "subprocess", "swimlanes", "process notation"]
    },
    {
      "id": "interactive_high_fidelity_prototyping",
      "name": "High-Fidelity Interactive Logic Prototyping",
      "description": "Advanced prototyping in Figma using component variants, variables, conditional expressions, and micro-interactions.",
      "keywords": ["Figma Variables", "conditional prototyping", "micro-interactions", "interactive prototype", "high-fidelity", "component variants"]
    },
    {
      "id": "epc_diagram",
      "name": "Event-Driven Process Chains (EPC)",
      "description": "EPC process notation mapping events, functions, and logical connectors (AND, OR, XOR).",
      "keywords": ["EPC diagram", "Event-Driven Process Chain", "logical connectors", "XOR", "event-function flow"]
    },
    {
      "id": "design_to_code_handoff_tokens",
      "name": "Design-to-Code Handoff & Storybook Sync",
      "description": "Preparing design specs for engineering: redlines, auto-layout tokens, Storybook component synchronizations, and zero-defect handoff.",
      "keywords": ["design handoff", "Storybook", "Figma Dev Mode", "redlines", "component props alignment", "zero defect handoff"]
    },
    {
      "id": "accessibility_wcag_design_specs",
      "name": "WCAG 2.1 AAA Accessibility Design Specs",
      "description": "Specifying accessible design: color contrast ratios, focus order annotations, screen reader aria-label notes, and tap target sizes.",
      "keywords": ["WCAG 2.1 AAA", "accessibility specs", "color contrast ratio", "focus order", "aria-label", "tap target size", "screen reader annotations"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Figma design specs, Storybook stories, and WCAG accessibility annotations",
        "detection": "content_analysis",
        "pattern": "\\.storybook/|\\.stories\\.(tsx|jsx|js)|aria-label|contrast-ratio|DesignSpecs",
        "strength": 0.85,
        "maps_to": [
          "ux_deliverables_prototyping.wireframing_tools",
          "ux_deliverables_prototyping.simple_flowchart",
          "ux_deliverables_prototyping.layout_rules",
          "ux_deliverables_prototyping.customer_experience_map",
          "ux_deliverables_prototyping.bpmn_diagram",
          "ux_deliverables_prototyping.interactive_high_fidelity_prototyping",
          "ux_deliverables_prototyping.epc_diagram",
          "ux_deliverables_prototyping.design_to_code_handoff_tokens",
          "ux_deliverables_prototyping.accessibility_wcag_design_specs"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Built wireframes, user flows, and high-fidelity interactive prototypes in Figma with variables and conditional logic",
        "strength": 0.6,
        "maps_to": [
          "ux_deliverables_prototyping.wireframing_tools",
          "ux_deliverables_prototyping.simple_flowchart",
          "ux_deliverables_prototyping.layout_rules",
          "ux_deliverables_prototyping.interactive_high_fidelity_prototyping"
        ]
      },
      {
        "signal": "Created CX journey maps, managed Storybook design-to-code handoffs, and authored WCAG 2.1 AAA accessibility specs",
        "strength": 0.6,
        "maps_to": [
          "ux_deliverables_prototyping.customer_experience_map",
          "ux_deliverables_prototyping.bpmn_diagram",
          "ux_deliverables_prototyping.epc_diagram",
          "ux_deliverables_prototyping.design_to_code_handoff_tokens",
          "ux_deliverables_prototyping.accessibility_wcag_design_specs"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in Prototyping, Figma, User Flows, Design Handoff, and Accessibility (WCAG)",
        "strength": 0.4,
        "maps_to": [
          "ux_deliverables_prototyping.wireframing_tools",
          "ux_deliverables_prototyping.simple_flowchart",
          "ux_deliverables_prototyping.layout_rules",
          "ux_deliverables_prototyping.customer_experience_map",
          "ux_deliverables_prototyping.bpmn_diagram",
          "ux_deliverables_prototyping.interactive_high_fidelity_prototyping",
          "ux_deliverables_prototyping.epc_diagram",
          "ux_deliverables_prototyping.design_to_code_handoff_tokens",
          "ux_deliverables_prototyping.accessibility_wcag_design_specs"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes deliverables and prototyping assessment covering Figma variables, BPMN/EPC diagrams, Storybook handoff, and WCAG AAA accessibility",
        "strength": 1.0,
        "maps_to": [
          "ux_deliverables_prototyping.wireframing_tools",
          "ux_deliverables_prototyping.simple_flowchart",
          "ux_deliverables_prototyping.layout_rules",
          "ux_deliverables_prototyping.customer_experience_map",
          "ux_deliverables_prototyping.bpmn_diagram",
          "ux_deliverables_prototyping.interactive_high_fidelity_prototyping",
          "ux_deliverables_prototyping.epc_diagram",
          "ux_deliverables_prototyping.design_to_code_handoff_tokens",
          "ux_deliverables_prototyping.accessibility_wcag_design_specs"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "wireframing_tools",
        "simple_flowchart",
        "layout_rules"
      ],
      "description": "Creates wireframes, maps user flowcharts, and applies 8pt grid auto-layout in Figma."
    },
    "mid": {
      "expected_subskills": [
        "customer_experience_map",
        "bpmn_diagram",
        "interactive_high_fidelity_prototyping"
      ],
      "description": "Constructs customer journey maps, BPMN process flows, and interactive prototypes with Figma variables/logic."
    },
    "senior": {
      "expected_subskills": [
        "epc_diagram",
        "design_to_code_handoff_tokens",
        "accessibility_wcag_design_specs"
      ],
      "description": "Architects EPC diagrams, establishes seamless Storybook design-to-code pipelines, and enforces WCAG 2.1 AAA accessibility."
    }
  }
}

# 8. ux_measuring_impact
skills["ux_measuring_impact"] = {
  "skill_id": "ux_measuring_impact",
  "name": "UX Analytics, Usability Testing & Impact Measurement",
  "category": "ux_analytics",
  "description": "Quantitative and qualitative UX measurement: A/B testing, multivariate testing, statistical significance, Usability Testing (SUS), funnel drop-off analytics, HEART framework ROI, and algorithmic personalization.",
  "subskills": [
    {
      "id": "ab_testing",
      "name": "A/B Testing Methodology & Hypothesis Formulation",
      "description": "Formulating testable hypotheses, defining primary/secondary metrics, and running A/B experiments.",
      "keywords": ["A/B testing", "hypothesis formulation", "control vs variant", "conversion rate", "experiment design"]
    },
    {
      "id": "ux_metrics",
      "name": "UX KPIs & Core Metrics (CSAT, CES, NPS, TTR)",
      "description": "Tracking Customer Satisfaction (CSAT), Customer Effort Score (CES), Net Promoter Score (NPS), and Time-to-Resolution.",
      "keywords": ["CSAT", "CES", "NPS", "TTR", "Customer Effort Score", "UX KPIs", "task completion rate"]
    },
    {
      "id": "usability_testing_heuristics_sus",
      "name": "Usability Testing Protocols & System Usability Scale (SUS)",
      "description": "Conducting moderated/unmoderated usability tests, Nielsen's 10 heuristics evaluations, and standard SUS scoring.",
      "keywords": ["usability testing", "System Usability Scale", "SUS score", "heuristics evaluation", "Nielsen 10 heuristics", "moderated test"]
    },
    {
      "id": "statistical_interpretation",
      "name": "Statistical Significance, P-Values & Sample Sizing",
      "description": "Calculating statistical significance (p < 0.05), confidence intervals, statistical power (1 - beta), and minimum sample sizes.",
      "keywords": ["statistical significance", "p-value", "confidence interval", "sample size calculator", "MDE", "Type I error", "Type II error"]
    },
    {
      "id": "integrating_test_results",
      "name": "Synthesizing Test Results & Iterative UX Roadmaps",
      "description": "Triangulating qualitative feedback with quantitative test metrics to drive iterative design roadmaps.",
      "keywords": ["test synthesis", "qual-quant triangulation", "iterative design", "design recommendations", "insight report"]
    },
    {
      "id": "funnel_dropoff_cohort_analytics",
      "name": "Funnel Drop-Off Analytics & Behavioral Cohorts",
      "description": "Analyzing conversion funnels, drop-off milestones, cohort retention curves (Mixpanel, Amplitude, PostHog), and session replay insights.",
      "keywords": ["funnel analytics", "drop-off analysis", "cohort retention", "Mixpanel", "Amplitude", "PostHog", "session recording"]
    },
    {
      "id": "multivariate_testing",
      "name": "Multivariate (MVT) & Fractional Factorial Testing",
      "description": "Testing multiple element combinations simultaneously using fractional factorial experimental design.",
      "keywords": ["multivariate testing", "MVT", "fractional factorial", "interaction effects", "high-traffic optimization"]
    },
    {
      "id": "longitudinal_ux_impact_heart_framework",
      "name": "Google HEART Framework & UX ROI Attribution",
      "description": "Measuring long-term impact with Google HEART (Happiness, Engagement, Adoption, Retention, Task Success) and calculating UX ROI.",
      "keywords": ["HEART framework", "Google HEART", "Happiness", "Engagement", "Adoption", "Retention", "Task Success", "UX ROI"]
    },
    {
      "id": "algorithmic_personalization_impact",
      "name": "Algorithmic & Adaptive UX Impact Measurement",
      "description": "Measuring the user impact of ML-driven adaptive UI personalization, recommendation algorithms, and algorithmic bias testing.",
      "keywords": ["adaptive UX", "personalization impact", "recommendation algorithm UX", "algorithmic bias", "dynamic personalization"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Experimentation configs (LaunchDarkly, Statsig), PostHog/Mixpanel tracking events, and usability test plans",
        "detection": "content_analysis",
        "pattern": "Statsig|LaunchDarkly|mixpanel\\.track|posthog\\.capture|ABTest|HEARTFramework",
        "strength": 0.85,
        "maps_to": [
          "ux_measuring_impact.ab_testing",
          "ux_measuring_impact.ux_metrics",
          "ux_measuring_impact.usability_testing_heuristics_sus",
          "ux_measuring_impact.statistical_interpretation",
          "ux_measuring_impact.integrating_test_results",
          "ux_measuring_impact.funnel_dropoff_cohort_analytics",
          "ux_measuring_impact.multivariate_testing",
          "ux_measuring_impact.longitudinal_ux_impact_heart_framework",
          "ux_measuring_impact.algorithmic_personalization_impact"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Formulated A/B test hypotheses and conducted SUS usability evaluations improving task completion rate from 62% to 91%",
        "strength": 0.6,
        "maps_to": [
          "ux_measuring_impact.ab_testing",
          "ux_measuring_impact.ux_metrics",
          "ux_measuring_impact.usability_testing_heuristics_sus",
          "ux_measuring_impact.statistical_interpretation"
        ]
      },
      {
        "signal": "Implemented Google HEART framework tracking longitudinal retention and analyzed funnel cohorts in Amplitude/Mixpanel",
        "strength": 0.6,
        "maps_to": [
          "ux_measuring_impact.integrating_test_results",
          "ux_measuring_impact.funnel_dropoff_cohort_analytics",
          "ux_measuring_impact.multivariate_testing",
          "ux_measuring_impact.longitudinal_ux_impact_heart_framework",
          "ux_measuring_impact.algorithmic_personalization_impact"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in UX Research, A/B Testing, Usability Testing (SUS), Product Analytics, and HEART Framework",
        "strength": 0.4,
        "maps_to": [
          "ux_measuring_impact.ab_testing",
          "ux_measuring_impact.ux_metrics",
          "ux_measuring_impact.usability_testing_heuristics_sus",
          "ux_measuring_impact.statistical_interpretation",
          "ux_measuring_impact.integrating_test_results",
          "ux_measuring_impact.funnel_dropoff_cohort_analytics",
          "ux_measuring_impact.multivariate_testing",
          "ux_measuring_impact.longitudinal_ux_impact_heart_framework",
          "ux_measuring_impact.algorithmic_personalization_impact"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes UX analytics assessment covering sample size calculations, SUS usability scoring, funnel cohort retention, and HEART framework ROI",
        "strength": 1.0,
        "maps_to": [
          "ux_measuring_impact.ab_testing",
          "ux_measuring_impact.ux_metrics",
          "ux_measuring_impact.usability_testing_heuristics_sus",
          "ux_measuring_impact.statistical_interpretation",
          "ux_measuring_impact.integrating_test_results",
          "ux_measuring_impact.funnel_dropoff_cohort_analytics",
          "ux_measuring_impact.multivariate_testing",
          "ux_measuring_impact.longitudinal_ux_impact_heart_framework",
          "ux_measuring_impact.algorithmic_personalization_impact"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "ab_testing",
        "ux_metrics",
        "usability_testing_heuristics_sus"
      ],
      "description": "Formulates testable A/B hypotheses, tracks CSAT/NPS KPIs, and conducts SUS usability tests."
    },
    "mid": {
      "expected_subskills": [
        "statistical_interpretation",
        "integrating_test_results",
        "funnel_dropoff_cohort_analytics"
      ],
      "description": "Calculates statistical significance/p-values, analyzes funnel drop-off cohorts, and synthesizes qualitative/quantitative insights."
    },
    "senior": {
      "expected_subskills": [
        "multivariate_testing",
        "longitudinal_ux_impact_heart_framework",
        "algorithmic_personalization_impact"
      ],
      "description": "Directs multivariate testing, establishes Google HEART framework tracking, and measures adaptive ML personalization impact."
    }
  }
}

# 9. ux_patterns_best_practices
skills["ux_patterns_best_practices"] = {
  "skill_id": "ux_patterns_best_practices",
  "name": "Persuasive UX Patterns & Behavioral Best Practices",
  "category": "ux_patterns",
  "description": "Evidence-backed persuasive UX patterns: social proof, authority, loss aversion, peer comparisons, urgency/scarcity, implementation intentions, and friction reduction.",
  "subskills": [
    {
      "id": "get_attention_patterns",
      "name": "Attention-Grabbing Patterns & Visual Saliency",
      "description": "Using contrast, motion, directional cues, and faces to guide gaze to key interaction points.",
      "keywords": ["visual saliency", "directional cues", "eye tracking", "motion in UI", "visual contrast", "focal point"]
    },
    {
      "id": "positive_impression_patterns",
      "name": "First Impression & Aesthetic-Usability Patterns",
      "description": "Harnessing the aesthetic-usability effect, micro-animations, and polished visual design for immediate trust.",
      "keywords": ["aesthetic usability effect", "first impression", "visual polish", "micro-animation", "trust building"]
    },
    {
      "id": "social_proof",
      "name": "Social Proof & Testimonial Integration",
      "description": "Integrating customer testimonials, user counts, real-time activity feeds, and reviews to reduce uncertainty.",
      "keywords": ["social proof", "testimonials", "user ratings", "reviews", "activity feed", "wisdom of crowds"]
    },
    {
      "id": "authority",
      "name": "Authority & Trust Signaling",
      "description": "Displaying expert endorsements, security badges, certifications, and compliance credentials.",
      "keywords": ["authority bias", "trust badges", "security certificates", "expert endorsements", "compliance logos"]
    },
    {
      "id": "loss_aversion",
      "name": "Loss Aversion & Sunk Cost Framing",
      "description": "Framing value in terms of what the user stands to lose or save rather than merely gain.",
      "keywords": ["loss aversion", "sunk cost", "Kahneman Tversky", "loss framing", "protect progress", "streak loss"]
    },
    {
      "id": "peer_comparison",
      "name": "Peer Comparison & Social Norms (Cialdini)",
      "description": "Showing how a user's behavior compares to similar peers (e.g. Opower energy usage comparisons).",
      "keywords": ["peer comparison", "social norms", "Cialdini", "normative feedback", "descriptive norms", "benchmark against peers"]
    },
    {
      "id": "urgency_scarcity",
      "name": "Ethical Urgency & Scarcity Signals",
      "description": "Authentic, non-deceptive scarcity and deadline indicators that motivate timely completion.",
      "keywords": ["urgency", "scarcity", "countdown timer", "limited inventory", "deadline", "ethical urgency"]
    },
    {
      "id": "implementation_intentions",
      "name": "Implementation Intentions (If-Then Planning)",
      "description": "Guiding users to pre-commit to exact when/where/how action plans ('When X happens, I will do Y').",
      "keywords": ["implementation intentions", "if-then planning", "Gollwitzer", "pre-commitment", "action trigger", "behavioral plan"]
    },
    {
      "id": "friction_reduction_defaulting",
      "name": "Radical Friction Elimination & 1-Click Flows",
      "description": "Eliminating every non-essential input field, implementing autocomplete, biometric auth, and 1-click checkout.",
      "keywords": ["friction reduction", "1-click checkout", "biometric auth", "form auto-fill", "minimal input", "effortless UX"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Social proof carousels, trust badges, urgency countdowns, and 1-click checkout components",
        "detection": "content_analysis",
        "pattern": "SocialProof|TrustBadges|CountdownTimer|OneClickCheckout|IfThenPlanner",
        "strength": 0.85,
        "maps_to": [
          "ux_patterns_best_practices.get_attention_patterns",
          "ux_patterns_best_practices.positive_impression_patterns",
          "ux_patterns_best_practices.social_proof",
          "ux_patterns_best_practices.authority",
          "ux_patterns_best_practices.loss_aversion",
          "ux_patterns_best_practices.peer_comparison",
          "ux_patterns_best_practices.urgency_scarcity",
          "ux_patterns_best_practices.implementation_intentions",
          "ux_patterns_best_practices.friction_reduction_defaulting"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Implemented social proof and peer comparison patterns increasing conversion rates by 22%",
        "strength": 0.6,
        "maps_to": [
          "ux_patterns_best_practices.get_attention_patterns",
          "ux_patterns_best_practices.positive_impression_patterns",
          "ux_patterns_best_practices.social_proof",
          "ux_patterns_best_practices.authority"
        ]
      },
      {
        "signal": "Designed Gollwitzer implementation intention if-then flows and 1-click checkout experiences",
        "strength": 0.6,
        "maps_to": [
          "ux_patterns_best_practices.loss_aversion",
          "ux_patterns_best_practices.peer_comparison",
          "ux_patterns_best_practices.urgency_scarcity",
          "ux_patterns_best_practices.implementation_intentions",
          "ux_patterns_best_practices.friction_reduction_defaulting"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in Persuasive Design, Social Proof, Conversion Rate Optimization (CRO), and UX Patterns",
        "strength": 0.4,
        "maps_to": [
          "ux_patterns_best_practices.get_attention_patterns",
          "ux_patterns_best_practices.positive_impression_patterns",
          "ux_patterns_best_practices.social_proof",
          "ux_patterns_best_practices.authority",
          "ux_patterns_best_practices.loss_aversion",
          "ux_patterns_best_practices.peer_comparison",
          "ux_patterns_best_practices.urgency_scarcity",
          "ux_patterns_best_practices.implementation_intentions",
          "ux_patterns_best_practices.friction_reduction_defaulting"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes persuasive UX patterns assessment covering visual saliency, ethical urgency, social proof, and implementation intentions",
        "strength": 1.0,
        "maps_to": [
          "ux_patterns_best_practices.get_attention_patterns",
          "ux_patterns_best_practices.positive_impression_patterns",
          "ux_patterns_best_practices.social_proof",
          "ux_patterns_best_practices.authority",
          "ux_patterns_best_practices.loss_aversion",
          "ux_patterns_best_practices.peer_comparison",
          "ux_patterns_best_practices.urgency_scarcity",
          "ux_patterns_best_practices.implementation_intentions",
          "ux_patterns_best_practices.friction_reduction_defaulting"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "get_attention_patterns",
        "positive_impression_patterns",
        "social_proof"
      ],
      "description": "Applies visual saliency, integrates customer reviews/social proof, and crafts polished first impressions."
    },
    "mid": {
      "expected_subskills": [
        "authority",
        "loss_aversion",
        "peer_comparison",
        "urgency_scarcity"
      ],
      "description": "Deploys trust authority badges, frames loss aversion, builds peer benchmarks, and adds ethical scarcity indicators."
    },
    "senior": {
      "expected_subskills": [
        "implementation_intentions",
        "friction_reduction_defaulting"
      ],
      "description": "Designs Gollwitzer if-then planning commitment devices and re-engineers complex forms into effortless 1-click flows."
    }
  }
}

# Write all 9 skill files
for skill_id, skill_data in skills.items():
    file_path = os.path.join(skills_dir, f"{skill_id}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(skill_data, f, indent=2, ensure_ascii=False)
    print(f"Generated UX skill file: {file_path}")

print("\nUX Design Skills Generated!")
