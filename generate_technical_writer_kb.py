import os
import json

base_dir = os.path.abspath('knowledge-base')
skills_dir = os.path.join(base_dir, 'skills', 'technical-writer')
evidence_dir = os.path.join(base_dir, 'evidence', 'technical-writer')
roles_dir = os.path.join(base_dir, 'roles', 'technical-writer')

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

# ==============================================================================
# 1. SKILLS DEFINITIONS (6 Skills, 55 Subskills)
# ==============================================================================
skills = {}

# 1. tw_fundamentals_writing_craft
skills["tw_fundamentals_writing_craft"] = {
  "skill_id": "tw_fundamentals_writing_craft",
  "name": "Technical Writing Fundamentals & Craft",
  "category": "writing_craft",
  "description": "Core writing and editing principles for technical communication: clarity, conciseness, active voice, audience-first framing, style guide adherence (Google/Microsoft), minimalism, readability metrics, and terminology management.",
  "subskills": [
    {
      "id": "clarity_conciseness_active_voice",
      "name": "Clarity, Conciseness & Active Voice",
      "description": "Writing with active voice, direct sentence structures, strong verbs, and eliminating jargon, filler words, and nominalizations.",
      "keywords": ["active voice", "conciseness", "nominalization", "plain language", "direct address", "strong verbs", "readability", "sentence length", "filler words", "clarity"]
    },
    {
      "id": "style_guides_standards",
      "name": "Technical Style Guides & Standards",
      "description": "Adherence and application of major tech style guides such as Google Developer Documentation Style Guide, Microsoft Writing Style Guide, and Chicago Manual of Style.",
      "keywords": ["Google Developer Documentation Style Guide", "Microsoft Writing Style Guide", "Chicago Manual of Style", "Vale style rules", "casing conventions", "UI text formatting", "punctuation rules", "Oxford comma"]
    },
    {
      "id": "audience_persona_analysis",
      "name": "Audience & Developer Persona Analysis",
      "description": "Analyzing audience technical proficiency, mental models, job-to-be-done (JTBD), and tailoring vocabulary, depth, and pacing to developers, admins, or end-users.",
      "keywords": ["audience analysis", "developer persona", "technical proficiency", "mental model", "JTBD", "user empathy", "reader persona", "onboarding path", "cognitive load"]
    },
    {
      "id": "information_architecture_hierarchy",
      "name": "Information Architecture & Document Hierarchy",
      "description": "Structuring complex technical documents using semantic heading hierarchies, progressive disclosure, chunking, breadcrumbs, and scannable layouts.",
      "keywords": ["information architecture", "progressive disclosure", "heading hierarchy", "chunking", "scannability", "parallel construction", "bulleted lists", "visual hierarchy", "table of contents"]
    },
    {
      "id": "dita_topic_based_authoring",
      "name": "Topic-Based Authoring & DITA Paradigms",
      "description": "Topic-based authoring paradigms (Concept, Task, Reference, Troubleshooting) separating procedural instructions from conceptual explanations and reference data.",
      "keywords": ["topic-based authoring", "DITA", "concept topic", "task topic", "reference topic", "troubleshooting topic", "modular documentation", "single sourcing", "information typing"]
    },
    {
      "id": "terminology_glossary_management",
      "name": "Terminology, Taxonomy & Glossary Governance",
      "description": "Creating and governing consistent product taxonomies, controlled vocabularies, enterprise glossaries, and deprecated term tracking.",
      "keywords": ["controlled vocabulary", "glossary", "taxonomy", "termbase", "product nomenclature", "consistency", "synonym management", "deprecation notices", "standardization"]
    },
    {
      "id": "readability_scoring_editing",
      "name": "Readability Scoring & Substantive Editing",
      "description": "Applying formal readability formulas (Flesch-Kincaid, Gunning Fog, Coleman-Liau) and editorial tiers (copyediting, developmental editing, substantive editing).",
      "keywords": ["Flesch-Kincaid", "Gunning Fog", "developmental editing", "copyediting", "substantive editing", "editorial review", "proofreading", "peer review rubric", "sentence complexity"]
    },
    {
      "id": "inclusive_accessible_language",
      "name": "Inclusive, Accessible & Global English",
      "description": "Implementing global English, accessible technical writing (WCAG 2.1 text alternatives, color-agnostic directions), gender-neutral phrasing, and localization-friendly writing.",
      "keywords": ["localization-friendly", "global English", "accessible documentation", "WCAG 2.1", "gender-neutral", "alt text", "screen reader accessibility", "translatability", "plain English"]
    },
    {
      "id": "doc_governance_style_creation",
      "name": "Documentation Governance & Style Creation",
      "description": "Designing organizational style guides, writing tenets, editorial governance workflows, and automated style linting rules (Vale rule definitions).",
      "keywords": ["doc governance", "style guide authoring", "Vale rules", "writing tenets", "doc standards", "editorial workflow", "voice and tone guidelines", "linter customization", "peer review SLA"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Vale style guide configuration and automated prose rule definitions",
        "detection": "content_analysis",
        "pattern": "\\.vale\\.ini|styles/Vocab/.*|BasedOnStyles\\s*=|MinAlertLevel\\s*=",
        "strength": 0.9,
        "maps_to": [
          "tw_fundamentals_writing_craft.style_guides_standards",
          "tw_fundamentals_writing_craft.doc_governance_style_creation"
        ]
      },
      {
        "signal": "Markdown heading hierarchy and structured scannability",
        "detection": "content_analysis",
        "pattern": "^#{1,4}\\s+[A-Z0-9]|<TableOfContents|<toc|sidebar_position:",
        "strength": 0.8,
        "maps_to": [
          "tw_fundamentals_writing_craft.information_architecture_hierarchy",
          "tw_fundamentals_writing_craft.clarity_conciseness_active_voice"
        ]
      },
      {
        "signal": "Topic-based authoring structure (Concept, Task, Reference, Troubleshooting)",
        "detection": "directory_structure",
        "pattern": "docs/(concepts|tasks|reference|troubleshooting|guides)/",
        "strength": 0.85,
        "maps_to": [
          "tw_fundamentals_writing_craft.dita_topic_based_authoring"
        ]
      },
      {
        "signal": "Centralized glossary and taxonomy definition files",
        "detection": "file_presence",
        "pattern": "docs/glossary\\.md|docs/terminology\\.md|docs/taxonomy\\.ya?ml",
        "strength": 0.85,
        "maps_to": [
          "tw_fundamentals_writing_craft.terminology_glossary_management"
        ]
      },
      {
        "signal": "Readability and editorial review checklists in pull request templates",
        "detection": "content_analysis",
        "pattern": "\\.github/PULL_REQUEST_TEMPLATE\\.md|Flesch-Kincaid|readability score|editorial review checklist",
        "strength": 0.75,
        "maps_to": [
          "tw_fundamentals_writing_craft.readability_scoring_editing"
        ]
      },
      {
        "signal": "Accessibility standards in docs (WCAG alt-text, color-neutral markup)",
        "detection": "content_analysis",
        "pattern": "!\\[[^\\]]{10,}\\]\\([^\\)]+\\)|<img\\s+[^>]*alt=\"[^\"]{10,}\"|aria-label=",
        "strength": 0.8,
        "maps_to": [
          "tw_fundamentals_writing_craft.inclusive_accessible_language",
          "tw_fundamentals_writing_craft.audience_persona_analysis"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Authored and maintained enterprise technical style guides and enforced Google/Microsoft developer documentation standards",
        "strength": 0.6,
        "maps_to": [
          "tw_fundamentals_writing_craft.style_guides_standards",
          "tw_fundamentals_writing_craft.doc_governance_style_creation",
          "tw_fundamentals_writing_craft.terminology_glossary_management"
        ]
      },
      {
        "signal": "Improved technical documentation readability scores (Flesch-Kincaid) and restructured information architecture for developer portals",
        "strength": 0.5,
        "maps_to": [
          "tw_fundamentals_writing_craft.clarity_conciseness_active_voice",
          "tw_fundamentals_writing_craft.information_architecture_hierarchy",
          "tw_fundamentals_writing_craft.readability_scoring_editing"
        ]
      },
      {
        "signal": "Implemented topic-based authoring (DITA) and accessibility standards (WCAG) across multi-product technical libraries",
        "strength": 0.5,
        "maps_to": [
          "tw_fundamentals_writing_craft.dita_topic_based_authoring",
          "tw_fundamentals_writing_craft.inclusive_accessible_language",
          "tw_fundamentals_writing_craft.audience_persona_analysis"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements and publications on Technical Writing Craft, Plain Language, DITA, and Information Architecture",
        "strength": 0.4,
        "maps_to": [
          "tw_fundamentals_writing_craft.clarity_conciseness_active_voice",
          "tw_fundamentals_writing_craft.style_guides_standards",
          "tw_fundamentals_writing_craft.audience_persona_analysis",
          "tw_fundamentals_writing_craft.information_architecture_hierarchy",
          "tw_fundamentals_writing_craft.dita_topic_based_authoring",
          "tw_fundamentals_writing_craft.terminology_glossary_management",
          "tw_fundamentals_writing_craft.readability_scoring_editing",
          "tw_fundamentals_writing_craft.inclusive_accessible_language",
          "tw_fundamentals_writing_craft.doc_governance_style_creation"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive technical writing craft assessment covering style guidelines, topic modeling, editorial reviews, and accessibility",
        "strength": 1.0,
        "maps_to": [
          "tw_fundamentals_writing_craft.clarity_conciseness_active_voice",
          "tw_fundamentals_writing_craft.style_guides_standards",
          "tw_fundamentals_writing_craft.audience_persona_analysis",
          "tw_fundamentals_writing_craft.information_architecture_hierarchy",
          "tw_fundamentals_writing_craft.dita_topic_based_authoring",
          "tw_fundamentals_writing_craft.terminology_glossary_management",
          "tw_fundamentals_writing_craft.readability_scoring_editing",
          "tw_fundamentals_writing_craft.inclusive_accessible_language",
          "tw_fundamentals_writing_craft.doc_governance_style_creation"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "clarity_conciseness_active_voice",
        "style_guides_standards",
        "audience_persona_analysis"
      ],
      "description": "Writes clear, concise, active-voice documentation adhering to established Google/Microsoft style guides and basic persona needs."
    },
    "mid": {
      "expected_subskills": [
        "information_architecture_hierarchy",
        "dita_topic_based_authoring",
        "terminology_glossary_management"
      ],
      "description": "Structures multi-page documentation with topic-based authoring (DITA), manages controlled glossaries, and designs scannable information architectures."
    },
    "senior": {
      "expected_subskills": [
        "readability_scoring_editing",
        "inclusive_accessible_language",
        "doc_governance_style_creation"
      ],
      "description": "Establishes enterprise documentation governance, authors custom Vale linting rules, leads editorial reviews, and enforces global WCAG accessibility standards."
    }
  }
}

# 2. tw_content_research_strategy
skills["tw_content_research_strategy"] = {
  "skill_id": "tw_content_research_strategy",
  "name": "Content Strategy & Technical Research",
  "category": "content_strategy",
  "description": "Researching technical subjects through SME interviews, reading source code and PRDs, content auditing, documentation strategy, information mapping, lifecycle management, and content gap analysis.",
  "subskills": [
    {
      "id": "sme_interviewing_elicitation",
      "name": "SME Interviewing & Knowledge Elicitation",
      "description": "Conducting structured interviews with software engineers, product managers, and architects to extract complex technical nuances efficiently.",
      "keywords": ["SME interview", "subject matter expert", "engineering interview", "knowledge elicitation", "question preparation", "technical debrief", "recorded demo transcription", "engineering partnership"]
    },
    {
      "id": "source_code_spec_reading",
      "name": "Source Code, Spec & PRD Analysis",
      "description": "Reading codebase pull requests, Jira tickets, RFCs, PRDs, architecture decision records (ADRs), and protobuf/schema definitions to uncover undocumented features.",
      "keywords": ["PRD analysis", "RFC review", "reading pull requests", "Git diff analysis", "ADR", "architectural specs", "Jira ticket analysis", "schema parsing", "code exploration"]
    },
    {
      "id": "content_gap_analysis",
      "name": "Content Gap Analysis & User Needs Discovery",
      "description": "Auditing existing documentation to identify missing topics, outdated workflows, broken prerequisites, and unanswered user questions.",
      "keywords": ["content gap analysis", "documentation audit", "missing guides", "outdated content identification", "documentation inventory", "user feedback triage", "support ticket analysis"]
    },
    {
      "id": "content_lifecycle_management",
      "name": "Content Lifecycle & Evergreen Maintenance",
      "description": "Managing the end-to-end documentation lifecycle: draft, review, publish, maintain, deprecate, and archive (evergreen content maintenance).",
      "keywords": ["content lifecycle", "deprecation workflow", "doc freshness", "content sunsetting", "archiving", "evergreen documentation", "versioned docs maintenance", "staleness review"]
    },
    {
      "id": "information_mapping_user_journeys",
      "name": "Information Mapping & User Journey Paths",
      "description": "Mapping user onboarding journeys, developer learning paths, task workflows, and decision trees to structured documentation navigation.",
      "keywords": ["user journey mapping", "learning paths", "developer onboarding funnel", "decision tree", "workflow mapping", "task flow", "docs navigation design", "customer onboarding"]
    },
    {
      "id": "docs_as_product_strategy",
      "name": "Docs-as-a-Product Strategy & Roadmapping",
      "description": "Treating documentation as a core product with discovery, backlog grooming, OKRs, sprint planning, and cross-functional release alignment.",
      "keywords": ["docs as a product", "doc roadmap", "documentation OKRs", "sprint backlog", "docs release planning", "cross-functional alignment", "product launch readiness", "KPI tracking"]
    },
    {
      "id": "content_reuse_single_sourcing",
      "name": "Content Reuse & Single-Sourcing Architecture",
      "description": "Designing single-sourcing architectures, snippet reuse, variables/placeholders, conditional content rendering, and componentized doc structures.",
      "keywords": ["single-sourcing", "content reuse", "snippets", "partials", "conditional text", "transclusion", "variables", "reusable admonitions", "modular content"]
    },
    {
      "id": "enterprise_doc_auditing",
      "name": "Enterprise Content Auditing & Rot Analysis",
      "description": "Executing qualitative and quantitative content audits across massive documentation repositories, assessing technical debt, readability, and content rot.",
      "keywords": ["content audit", "content rot", "doc debt", "quantitative audit", "qualitative audit", "inventory matrix", "rot score", "consolidation strategy", "technical debt"]
    },
    {
      "id": "knowledge_base_federation",
      "name": "Knowledge Base Federation & Unification",
      "description": "Architecting unified documentation ecosystems across engineering, internal wikis (Confluence/Notion), public developer docs, and customer support hubs.",
      "keywords": ["federated docs", "knowledge federation", "enterprise search indexing", "Confluence migration", "cross-portal taxonomy", "knowledge base unification", "content ecosystem"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Architectural decision records and RFC review involvement",
        "detection": "file_presence",
        "pattern": "rfcs/.*\\.md|docs/adr/.*\\.md|docs/architecture/.*\\.md",
        "strength": 0.85,
        "maps_to": [
          "tw_content_research_strategy.source_code_spec_reading",
          "tw_content_research_strategy.sme_interviewing_elicitation"
        ]
      },
      {
        "signal": "Single-sourcing component reuse, snippets, and partial imports in docs",
        "detection": "content_analysis",
        "pattern": "import\\s+.*\\s+from\\s+['\"]@site/docs/partials/|import\\s+Snippet|include::|{% include",
        "strength": 0.9,
        "maps_to": [
          "tw_content_research_strategy.content_reuse_single_sourcing"
        ]
      },
      {
        "signal": "Documentation roadmaps, OKR tracking, and content sprint backlogs",
        "detection": "file_presence",
        "pattern": "docs/roadmap\\.md|docs/content-strategy\\.md|docs/backlog\\.md",
        "strength": 0.8,
        "maps_to": [
          "tw_content_research_strategy.docs_as_product_strategy",
          "tw_content_research_strategy.content_gap_analysis"
        ]
      },
      {
        "signal": "User journey maps and guided learning paths",
        "detection": "content_analysis",
        "pattern": "docs/(learning-paths|getting-started|user-journeys)/|learningPath:|sidebar_label:\\s*Step",
        "strength": 0.8,
        "maps_to": [
          "tw_content_research_strategy.information_mapping_user_journeys",
          "tw_content_research_strategy.content_lifecycle_management"
        ]
      },
      {
        "signal": "Content rot audits, deprecation notices, and federated knowledge configs",
        "detection": "content_analysis",
        "pattern": "deprecated:\\s*true|:::caution\\s+Deprecated|docs/audit|sync-docs\\.ya?ml",
        "strength": 0.85,
        "maps_to": [
          "tw_content_research_strategy.enterprise_doc_auditing",
          "tw_content_research_strategy.knowledge_base_federation"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Led content strategy and documentation audits for enterprise SaaS platforms, reducing content rot by 45%",
        "strength": 0.6,
        "maps_to": [
          "tw_content_research_strategy.content_gap_analysis",
          "tw_content_research_strategy.enterprise_doc_auditing",
          "tw_content_research_strategy.docs_as_product_strategy"
        ]
      },
      {
        "signal": "Collaborated directly with engineering SMEs and parsed PRDs/RFCs/codebases to create developer learning journeys",
        "strength": 0.5,
        "maps_to": [
          "tw_content_research_strategy.sme_interviewing_elicitation",
          "tw_content_research_strategy.source_code_spec_reading",
          "tw_content_research_strategy.information_mapping_user_journeys"
        ]
      },
      {
        "signal": "Architected single-sourcing content reuse framework and federated internal knowledge bases with public docs",
        "strength": 0.5,
        "maps_to": [
          "tw_content_research_strategy.content_lifecycle_management",
          "tw_content_research_strategy.content_reuse_single_sourcing",
          "tw_content_research_strategy.knowledge_base_federation"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Proven track record in Content Strategy, Technical Research, Information Architecture, and Knowledge Management",
        "strength": 0.4,
        "maps_to": [
          "tw_content_research_strategy.sme_interviewing_elicitation",
          "tw_content_research_strategy.source_code_spec_reading",
          "tw_content_research_strategy.content_gap_analysis",
          "tw_content_research_strategy.content_lifecycle_management",
          "tw_content_research_strategy.information_mapping_user_journeys",
          "tw_content_research_strategy.docs_as_product_strategy",
          "tw_content_research_strategy.content_reuse_single_sourcing",
          "tw_content_research_strategy.enterprise_doc_auditing",
          "tw_content_research_strategy.knowledge_base_federation"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive content strategy and technical research assessment covering SME elicitation, single sourcing, and doc auditing",
        "strength": 1.0,
        "maps_to": [
          "tw_content_research_strategy.sme_interviewing_elicitation",
          "tw_content_research_strategy.source_code_spec_reading",
          "tw_content_research_strategy.content_gap_analysis",
          "tw_content_research_strategy.content_lifecycle_management",
          "tw_content_research_strategy.information_mapping_user_journeys",
          "tw_content_research_strategy.docs_as_product_strategy",
          "tw_content_research_strategy.content_reuse_single_sourcing",
          "tw_content_research_strategy.enterprise_doc_auditing",
          "tw_content_research_strategy.knowledge_base_federation"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "sme_interviewing_elicitation",
        "source_code_spec_reading",
        "content_gap_analysis"
      ],
      "description": "Conducts initial SME interviews, reads code diffs/PRDs to identify undocumented features, and spots content gaps."
    },
    "mid": {
      "expected_subskills": [
        "content_lifecycle_management",
        "information_mapping_user_journeys",
        "docs_as_product_strategy"
      ],
      "description": "Manages content freshness lifecycles, maps user onboarding journeys, and aligns doc sprints with product launch roadmaps."
    },
    "senior": {
      "expected_subskills": [
        "content_reuse_single_sourcing",
        "enterprise_doc_auditing",
        "knowledge_base_federation"
      ],
      "description": "Architects reusable single-sourcing components, conducts qualitative rot audits across large repos, and federates cross-team knowledge bases."
    }
  }
}

# 3. tw_developer_documentation
skills["tw_developer_documentation"] = {
  "skill_id": "tw_developer_documentation",
  "name": "Developer Documentation & API Reference",
  "category": "developer_docs",
  "description": "Authoring comprehensive developer-facing content: REST/GraphQL/gRPC API references, OpenAPI/Swagger specifications, quickstarts, tutorials, code samples in multiple languages, SDK guides, and CLI references.",
  "subskills": [
    {
      "id": "openapi_swagger_spec_authoring",
      "name": "OpenAPI & Swagger Spec Authoring",
      "description": "Writing and editing OpenAPI Specification (OAS 3.0/3.1) and Swagger YAML/JSON files with schemas, parameters, request bodies, and response codes.",
      "keywords": ["OpenAPI", "OAS 3.0", "OAS 3.1", "Swagger", "openapi.yaml", "swagger.json", "schema definition", "status codes", "requestBody", "response objects"]
    },
    {
      "id": "api_reference_writing",
      "name": "REST API Endpoint Reference Documentation",
      "description": "Crafting accurate REST endpoint documentation: HTTP methods, path/query/header parameters, pagination, rate limits, authentication (Bearer, OAuth2, API Keys), and error models.",
      "keywords": ["REST API reference", "HTTP methods", "query parameters", "path variables", "Bearer token", "OAuth2", "rate limiting", "4xx/5xx status codes", "pagination", "headers"]
    },
    {
      "id": "curl_code_sample_authoring",
      "name": "Multi-Language Code Samples & cURL Snippets",
      "description": "Writing clean, executable code snippets and cURL commands across multiple programming languages (Python, JavaScript/TypeScript, Go, Java, cURL).",
      "keywords": ["cURL command", "code snippets", "request payload", "JSON response", "multi-language samples", "SDK snippet", "executable example", "API request example"]
    },
    {
      "id": "developer_quickstarts_tutorials",
      "name": "Developer Quickstarts & Sandbox Tutorials",
      "description": "Authoring step-by-step developer quickstarts ('Hello World' to first API call in under 5 minutes), interactive tutorials, and sandbox guides.",
      "keywords": ["developer quickstart", "tutorial", "5-minute quickstart", "sandbox environment", "getting started guide", "sample app walkthrough", "API onboarding", "first API call"]
    },
    {
      "id": "sdk_library_documentation",
      "name": "Client SDKs & Package Documentation",
      "description": "Documenting client SDKs, package installation (npm, pip, cargo, maven), client initialization, exception handling, and idiomatic usage patterns.",
      "keywords": ["SDK documentation", "client libraries", "npm package", "pip install", "client initialization", "error handling", "idiomatic code examples", "wrapper library"]
    },
    {
      "id": "graphql_grpc_asyncapi_docs",
      "name": "GraphQL, gRPC & Event-Driven AsyncAPI Docs",
      "description": "Documenting non-REST architectures: GraphQL schemas (queries, mutations, subscriptions), gRPC/Protobuf service definitions, and event-driven AsyncAPI/Webhooks.",
      "keywords": ["GraphQL documentation", "schema", "queries", "mutations", "gRPC", "Protobuf docs", "AsyncAPI", "webhooks", "payload schemas", "event streaming", "subscriptions"]
    },
    {
      "id": "cli_command_reference",
      "name": "CLI Command Reference & Terminal Guides",
      "description": "Writing comprehensive CLI references: commands, subcommands, flags/options, environment variables, exit codes, and shell completion instructions.",
      "keywords": ["CLI reference", "command line docs", "flags", "options", "exit codes", "subcommands", "man pages", "shell completion", "terminal examples", "CLI help"]
    },
    {
      "id": "api_error_handling_troubleshooting",
      "name": "API Error Handling & Diagnostic Catalogs",
      "description": "Documenting comprehensive error catalogs, machine-readable error codes, RFC 7807 Problem Details, root causes, and programmatic resolution steps.",
      "keywords": ["error catalog", "RFC 7807", "problem details", "error codes", "HTTP error matrix", "troubleshooting steps", "debugging guides", "error handling"]
    },
    {
      "id": "devportal_architecture_experience",
      "name": "Developer Portal Architecture & DX Design",
      "description": "Designing developer portal user experience (DX), interactive API consoles (Swagger UI, Redoc, Stoplight, Scalar, ReadMe), and code snippet generators.",
      "keywords": ["developer portal", "DX", "Swagger UI", "Redoc", "Stoplight", "Scalar", "ReadMe.com", "API explorer", "interactive console", "developer hub", "API playground"]
    },
    {
      "id": "versioning_breaking_changes_migration",
      "name": "API Versioning, Deprecation & Migration Guides",
      "description": "Authoring API versioning strategies, deprecation notices, breaking change policies, and step-by-step version migration guides.",
      "keywords": ["API versioning", "deprecation policy", "breaking changes", "migration guide", "semantic versioning", "sunsetting API", "backwards compatibility", "upgrade path"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "OpenAPI / Swagger 3.0/3.1 specification files and schema definitions",
        "detection": "file_presence",
        "pattern": "openapi\\.ya?ml|swagger\\.json|openapi/.*\\.ya?ml",
        "strength": 0.95,
        "maps_to": [
          "tw_developer_documentation.openapi_swagger_spec_authoring"
        ]
      },
      {
        "signal": "REST endpoint reference documentation with HTTP methods and headers",
        "detection": "content_analysis",
        "pattern": "### (GET|POST|PUT|DELETE|PATCH)\\s+/|Authorization:\\s*Bearer|X-RateLimit-|HTTP/1\\.1\\s+[245][0-9]{2}",
        "strength": 0.9,
        "maps_to": [
          "tw_developer_documentation.api_reference_writing"
        ]
      },
      {
        "signal": "Multi-language executable code snippets and cURL commands",
        "detection": "content_analysis",
        "pattern": "```(curl|bash)\\s+curl\\s+-X|```(python|typescript|javascript|go|java)\\s+(import|const|package)",
        "strength": 0.85,
        "maps_to": [
          "tw_developer_documentation.curl_code_sample_authoring"
        ]
      },
      {
        "signal": "5-minute developer quickstart guides and sample onboarding walkthroughs",
        "detection": "content_analysis",
        "pattern": "docs/quickstart\\.md|5-minute quickstart|Send your first|Your First API Call",
        "strength": 0.85,
        "maps_to": [
          "tw_developer_documentation.developer_quickstarts_tutorials"
        ]
      },
      {
        "signal": "Official client SDK package documentation and installation guides",
        "detection": "content_analysis",
        "pattern": "npm install @|pip install|cargo add|new AcmeClient\\(|client = Acme\\(",
        "strength": 0.85,
        "maps_to": [
          "tw_developer_documentation.sdk_library_documentation"
        ]
      },
      {
        "signal": "GraphQL, gRPC, Protobuf, or AsyncAPI webhook documentation",
        "detection": "file_presence",
        "pattern": "schema\\.graphql|.*\\.proto|asyncapi\\.ya?ml|docs/(graphql|grpc|webhooks)/",
        "strength": 0.9,
        "maps_to": [
          "tw_developer_documentation.graphql_grpc_asyncapi_docs"
        ]
      },
      {
        "signal": "CLI command reference pages and terminal options",
        "detection": "content_analysis",
        "pattern": "```bash\\s+[a-z]+ctl\\s+[a-z]+|--[a-z0-9-]+|Exit Codes|Environment Variables",
        "strength": 0.8,
        "maps_to": [
          "tw_developer_documentation.cli_command_reference"
        ]
      },
      {
        "signal": "RFC 7807 problem details and API error troubleshooting catalog",
        "detection": "content_analysis",
        "pattern": "application/problem\\+json|\"type\":\\s*\"https://|\"invalid_params\"|HTTP 429 Too Many Requests",
        "strength": 0.85,
        "maps_to": [
          "tw_developer_documentation.api_error_handling_troubleshooting"
        ]
      },
      {
        "signal": "Developer portal theme customization and interactive API console configs",
        "detection": "content_analysis",
        "pattern": "@scalar/docusaurus|docusaurus-theme-openapi|redoc-express|swagger-ui-react|stoplight/elements",
        "strength": 0.9,
        "maps_to": [
          "tw_developer_documentation.devportal_architecture_experience"
        ]
      },
      {
        "signal": "API migration guides, breaking change policies, and version sunset notices",
        "detection": "content_analysis",
        "pattern": "docs/migrations/|Migrating from v1 to v2|Breaking Changes|Deprecation Policy",
        "strength": 0.85,
        "maps_to": [
          "tw_developer_documentation.versioning_breaking_changes_migration"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Designed and published REST/GraphQL/gRPC developer documentation and OpenAPI 3.0 specs for public developer portals",
        "strength": 0.6,
        "maps_to": [
          "tw_developer_documentation.openapi_swagger_spec_authoring",
          "tw_developer_documentation.api_reference_writing",
          "tw_developer_documentation.graphql_grpc_asyncapi_docs",
          "tw_developer_documentation.devportal_architecture_experience"
        ]
      },
      {
        "signal": "Authored interactive 5-minute quickstarts, client SDK reference guides, and multi-language executable code samples (Python, JS, Go)",
        "strength": 0.6,
        "maps_to": [
          "tw_developer_documentation.curl_code_sample_authoring",
          "tw_developer_documentation.developer_quickstarts_tutorials",
          "tw_developer_documentation.sdk_library_documentation",
          "tw_developer_documentation.cli_command_reference"
        ]
      },
      {
        "signal": "Authored API error catalogs (RFC 7807) and managed major API version migration guides and breaking change policies",
        "strength": 0.5,
        "maps_to": [
          "tw_developer_documentation.api_error_handling_troubleshooting",
          "tw_developer_documentation.versioning_breaking_changes_migration"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Recognized for expertise in Developer Experience (DX), API Documentation, OpenAPI/Swagger, and SDK Documentation",
        "strength": 0.4,
        "maps_to": [
          "tw_developer_documentation.openapi_swagger_spec_authoring",
          "tw_developer_documentation.api_reference_writing",
          "tw_developer_documentation.curl_code_sample_authoring",
          "tw_developer_documentation.developer_quickstarts_tutorials",
          "tw_developer_documentation.sdk_library_documentation",
          "tw_developer_documentation.graphql_grpc_asyncapi_docs",
          "tw_developer_documentation.cli_command_reference",
          "tw_developer_documentation.api_error_handling_troubleshooting",
          "tw_developer_documentation.devportal_architecture_experience",
          "tw_developer_documentation.versioning_breaking_changes_migration"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes technical developer documentation assessment covering OpenAPI schemas, REST reference entries, SDK guides, and migration paths",
        "strength": 1.0,
        "maps_to": [
          "tw_developer_documentation.openapi_swagger_spec_authoring",
          "tw_developer_documentation.api_reference_writing",
          "tw_developer_documentation.curl_code_sample_authoring",
          "tw_developer_documentation.developer_quickstarts_tutorials",
          "tw_developer_documentation.sdk_library_documentation",
          "tw_developer_documentation.graphql_grpc_asyncapi_docs",
          "tw_developer_documentation.cli_command_reference",
          "tw_developer_documentation.api_error_handling_troubleshooting",
          "tw_developer_documentation.devportal_architecture_experience",
          "tw_developer_documentation.versioning_breaking_changes_migration"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "openapi_swagger_spec_authoring",
        "api_reference_writing",
        "curl_code_sample_authoring",
        "developer_quickstarts_tutorials"
      ],
      "description": "Writes OpenAPI YAML specs, REST endpoint reference docs, cURL/code snippets, and 5-minute developer quickstarts."
    },
    "mid": {
      "expected_subskills": [
        "sdk_library_documentation",
        "graphql_grpc_asyncapi_docs",
        "cli_command_reference",
        "api_error_handling_troubleshooting"
      ],
      "description": "Documents client SDKs, GraphQL/gRPC/AsyncAPI schemas, command line tools, and detailed error troubleshooting catalogs."
    },
    "senior": {
      "expected_subskills": [
        "devportal_architecture_experience",
        "versioning_breaking_changes_migration"
      ],
      "description": "Architects developer portal experiences (DX), establishes API deprecation policies, and authors complex breaking change migration guides."
    }
  }
}

# 4. tw_product_support_content
skills["tw_product_support_content"] = {
  "skill_id": "tw_product_support_content",
  "name": "Product Documentation & Support Content",
  "category": "product_support",
  "description": "Writing end-user product documentation, step-by-step how-to guides, administrative manuals, troubleshooting runbooks, changelogs, release notes, and customer support self-service knowledge bases.",
  "subskills": [
    {
      "id": "how_to_procedural_guides",
      "name": "How-To Guides & Procedural Documentation",
      "description": "Writing action-oriented, numbered procedural guides with prerequisite callouts, UI navigation paths, expected outcomes, and verification steps.",
      "keywords": ["how-to guide", "step-by-step instructions", "prerequisites", "expected result", "UI navigation", "procedural steps", "action-oriented", "verification", "task flow"]
    },
    {
      "id": "release_notes_changelogs",
      "name": "Release Notes & Changelog Authoring",
      "description": "Drafting release notes, changelog entries conforming to Keep a Changelog (Added, Changed, Deprecated, Removed, Fixed, Security), and version announcements.",
      "keywords": ["release notes", "Keep a Changelog", "CHANGELOG.md", "semantic versioning", "feature announcements", "patch notes", "bug fixes", "deprecations", "version highlights"]
    },
    {
      "id": "faq_self_service_articles",
      "name": "FAQ Articles & Support Self-Service Content",
      "description": "Authoring concise FAQ articles, knowledge base self-service answers, and deflecting repetitive customer support inquiries.",
      "keywords": ["FAQ", "knowledge base", "support article", "self-service", "ticket deflection", "question and answer", "help center", "Zendesk guide", "Intercom articles"]
    },
    {
      "id": "troubleshooting_root_cause_guides",
      "name": "Troubleshooting & Root Cause Diagnostic Guides",
      "description": "Structuring diagnostic guides: symptoms, root cause explanation, step-by-step remediation, workarounds, and verification commands.",
      "keywords": ["troubleshooting guide", "root cause", "symptoms", "remediation", "workaround", "error diagnostics", "recovery steps", "debug logs", "diagnostic steps"]
    },
    {
      "id": "admin_configuration_manuals",
      "name": "Admin Guides & Enterprise Configuration Manuals",
      "description": "Authoring enterprise administrator guides: SSO/SAML setup, role-based access control (RBAC), audit logging, network allowlisting, and system configurations.",
      "keywords": ["admin guide", "SSO configuration", "SAML", "RBAC", "permission matrix", "system settings", "security configuration", "enterprise setup", "audit logs"]
    },
    {
      "id": "ui_ux_microcopy_in_product_help",
      "name": "In-Product Microcopy & Embedded Assistance",
      "description": "Writing UI microcopy, modal dialogues, tooltip text, empty states, error strings, and embedded in-app onboarding walkthroughs.",
      "keywords": ["microcopy", "UI copy", "tooltips", "empty states", "error messages", "in-app guidance", "WalkMe", "Pendo", "onboarding tours", "button labels"]
    },
    {
      "id": "support_ticket_deflection_strategy",
      "name": "Support Ticket Deflection & KCS Strategy",
      "description": "Analyzing customer support ticket drivers, identifying top deflection opportunities, and structuring knowledge content to reduce MTTR and ticket volume.",
      "keywords": ["ticket deflection", "MTTR", "support analytics", "ticket volume reduction", "self-serve rate", "knowledge-centered service", "KCS", "call reduction", "support ROI"]
    },
    {
      "id": "disaster_recovery_runbooks",
      "name": "Disaster Recovery & Operational Runbooks",
      "description": "Authoring operational runbooks, disaster recovery procedures, incident response playbooks, and high-severity escalation documentation.",
      "keywords": ["runbook", "disaster recovery", "incident playbook", "post-mortem docs", "failover procedure", "SLA escalation", "operational playbook", "on-call guide"]
    },
    {
      "id": "user_feedback_loops_csat",
      "name": "User Feedback Loops & Documentation CSAT",
      "description": "Designing in-doc feedback mechanisms ('Was this helpful?'), analyzing CSAT/DSAT ratings, verbatim comments, and driving continuous document enhancement.",
      "keywords": ["doc CSAT", "DSAT", "in-page feedback", "helpfulness voting", "verbatim comment analysis", "feedback loop", "continuous improvement", "sentiment analysis"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Numbered procedural how-to guides with prerequisite callouts",
        "detection": "content_analysis",
        "pattern": "docs/guides/.*\\.md|:::info\\s+Prerequisites|1\\.\\s+Navigate to|2\\.\\s+Click|\\*\\*Expected Result:\\*\\*",
        "strength": 0.85,
        "maps_to": [
          "tw_product_support_content.how_to_procedural_guides"
        ]
      },
      {
        "signal": "Keep a Changelog formatted CHANGELOG.md file",
        "detection": "file_presence",
        "pattern": "CHANGELOG\\.md",
        "strength": 0.95,
        "maps_to": [
          "tw_product_support_content.release_notes_changelogs"
        ]
      },
      {
        "signal": "Self-service FAQ articles and ticket deflection knowledge bases",
        "detection": "file_presence",
        "pattern": "docs/faq\\.md|docs/support/.*\\.md",
        "strength": 0.8,
        "maps_to": [
          "tw_product_support_content.faq_self_service_articles"
        ]
      },
      {
        "signal": "Root cause troubleshooting guides with diagnostic commands",
        "detection": "content_analysis",
        "pattern": "docs/troubleshooting/.*\\.md|Symptoms|Root Cause|Resolution|Diagnostic Steps",
        "strength": 0.85,
        "maps_to": [
          "tw_product_support_content.troubleshooting_root_cause_guides"
        ]
      },
      {
        "signal": "Enterprise admin guides (SSO, SAML, RBAC, SCIM)",
        "detection": "content_analysis",
        "pattern": "docs/admin/.*\\.md|SAML 2\\.0|Single Sign-On|RBAC|SCIM Provisioning|Audit Logs",
        "strength": 0.85,
        "maps_to": [
          "tw_product_support_content.admin_configuration_manuals"
        ]
      },
      {
        "signal": "In-product UI microcopy, tooltip strings, and error messages",
        "detection": "content_analysis",
        "pattern": "locales/en/.*\\.json|messages\\.json|tooltipText|emptyStateMessage",
        "strength": 0.8,
        "maps_to": [
          "tw_product_support_content.ui_ux_microcopy_in_product_help"
        ]
      },
      {
        "signal": "Disaster recovery runbooks and SEV incident playbooks",
        "detection": "file_presence",
        "pattern": "docs/runbooks/.*\\.md|docs/playbooks/.*\\.md|SEV-1|Incident Response",
        "strength": 0.9,
        "maps_to": [
          "tw_product_support_content.disaster_recovery_runbooks"
        ]
      },
      {
        "signal": "Ticket deflection tracking and documentation CSAT feedback widgets",
        "detection": "content_analysis",
        "pattern": "Was this page helpful|feedbackWidget|dsat_reason|posthog\\.capture\\('doc_feedback'",
        "strength": 0.85,
        "maps_to": [
          "tw_product_support_content.support_ticket_deflection_strategy",
          "tw_product_support_content.user_feedback_loops_csat"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Authored comprehensive product documentation and troubleshooting runbooks, achieving a 35% reduction in support ticket volume",
        "strength": 0.6,
        "maps_to": [
          "tw_product_support_content.how_to_procedural_guides",
          "tw_product_support_content.troubleshooting_root_cause_guides",
          "tw_product_support_content.support_ticket_deflection_strategy"
        ]
      },
      {
        "signal": "Published monthly release notes (Keep a Changelog), admin manuals for SSO/RBAC, and in-product UI microcopy",
        "strength": 0.5,
        "maps_to": [
          "tw_product_support_content.release_notes_changelogs",
          "tw_product_support_content.admin_configuration_manuals",
          "tw_product_support_content.ui_ux_microcopy_in_product_help"
        ]
      },
      {
        "signal": "Implemented Knowledge-Centered Service (KCS), user CSAT feedback loops, and disaster recovery incident playbooks",
        "strength": 0.5,
        "maps_to": [
          "tw_product_support_content.faq_self_service_articles",
          "tw_product_support_content.disaster_recovery_runbooks",
          "tw_product_support_content.user_feedback_loops_csat"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Expertise in Knowledge Management, Technical Support Content, Product Documentation, and User Experience Writing",
        "strength": 0.4,
        "maps_to": [
          "tw_product_support_content.how_to_procedural_guides",
          "tw_product_support_content.release_notes_changelogs",
          "tw_product_support_content.faq_self_service_articles",
          "tw_product_support_content.troubleshooting_root_cause_guides",
          "tw_product_support_content.admin_configuration_manuals",
          "tw_product_support_content.ui_ux_microcopy_in_product_help",
          "tw_product_support_content.support_ticket_deflection_strategy",
          "tw_product_support_content.disaster_recovery_runbooks",
          "tw_product_support_content.user_feedback_loops_csat"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes practical product support assessment covering procedural how-to guides, changelogs, error diagnostic steps, and admin manuals",
        "strength": 1.0,
        "maps_to": [
          "tw_product_support_content.how_to_procedural_guides",
          "tw_product_support_content.release_notes_changelogs",
          "tw_product_support_content.faq_self_service_articles",
          "tw_product_support_content.troubleshooting_root_cause_guides",
          "tw_product_support_content.admin_configuration_manuals",
          "tw_product_support_content.ui_ux_microcopy_in_product_help",
          "tw_product_support_content.support_ticket_deflection_strategy",
          "tw_product_support_content.disaster_recovery_runbooks",
          "tw_product_support_content.user_feedback_loops_csat"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "how_to_procedural_guides",
        "release_notes_changelogs",
        "faq_self_service_articles"
      ],
      "description": "Drafts step-by-step how-to articles, standard Keep a Changelog entries, and self-service FAQ answers."
    },
    "mid": {
      "expected_subskills": [
        "troubleshooting_root_cause_guides",
        "admin_configuration_manuals",
        "ui_ux_microcopy_in_product_help"
      ],
      "description": "Writes diagnostic troubleshooting guides, enterprise admin configuration manuals, and in-product UI microcopy."
    },
    "senior": {
      "expected_subskills": [
        "support_ticket_deflection_strategy",
        "disaster_recovery_runbooks",
        "user_feedback_loops_csat"
      ],
      "description": "Drives support ticket deflection strategy via KCS, authors mission-critical disaster recovery runbooks, and analyzes doc CSAT metrics."
    }
  }
}

# 5. tw_content_marketing_seo
skills["tw_content_marketing_seo"] = {
  "skill_id": "tw_content_marketing_seo",
  "name": "Technical Content Marketing & Technical SEO",
  "category": "content_marketing",
  "description": "Creating high-impact technical blog posts, architectural case studies, whitepapers, thought leadership, developer evangelism content, and optimizing technical documentation for search engines (SEO).",
  "subskills": [
    {
      "id": "technical_blog_post_authoring",
      "name": "Technical Blog Post Authoring & Storytelling",
      "description": "Writing engaging technical blog posts that break down complex engineering concepts, benchmark comparisons, and architectural deep-dives.",
      "keywords": ["technical blog post", "engineering blog", "architectural breakdown", "benchmarks", "technical storytelling", "dev marketing", "Medium", "Dev.to", "Hashnode"]
    },
    {
      "id": "metadata_schema_seo_basics",
      "name": "Doc Metadata, Open Graph & Structured Data",
      "description": "Structuring doc metadata, title tags, meta descriptions, Open Graph tags, canonical URLs, semantic HTML tags, and schema.org markup for technical docs.",
      "keywords": ["meta description", "title tag", "Open Graph", "canonical URL", "schema.org", "TechArticle", "semantic HTML", "breadcrumb markup", "rich snippets"]
    },
    {
      "id": "keyword_research_search_intent",
      "name": "Technical Keyword Research & Search Intent",
      "description": "Conducting technical keyword research, search intent mapping (informational, navigational, transactional), and identifying high-volume developer queries.",
      "keywords": ["keyword research", "search intent", "developer queries", "search volume", "Ahrefs", "Semrush", "Google Search Console", "keyword clustering", "long-tail keywords"]
    },
    {
      "id": "technical_whitepapers_ebooks",
      "name": "Technical Whitepapers & In-Depth Ebooks",
      "description": "Authoring in-depth technical whitepapers, architectural blueprints, enterprise ebooks, and solution briefs for technical decision-makers.",
      "keywords": ["whitepaper", "technical ebook", "solution brief", "architectural blueprint", "executive summary", "benchmark report", "buyer guide", "enterprise whitepaper"]
    },
    {
      "id": "case_studies_customer_stories",
      "name": "Customer Case Studies & Migration Stories",
      "description": "Interviewing enterprise engineering teams and authoring technical customer success stories, migration case studies, and ROI breakdowns.",
      "keywords": ["customer story", "case study", "migration story", "customer testimonial", "ROI analysis", "production scale story", "engineering spotlight", "social proof"]
    },
    {
      "id": "developer_advocacy_community_content",
      "name": "Developer Advocacy & Community Content",
      "description": "Authoring community tutorials, Reddit/Hacker News technical announcements, newsletter issues, and open-source contribution guides.",
      "keywords": ["developer advocacy", "community content", "Hacker News launch", "technical newsletter", "Substack", "open source contributor guide", "evangelism", "Show HN"]
    },
    {
      "id": "technical_seo_information_architecture",
      "name": "Technical SEO Architecture & Crawlability",
      "description": "Architecting docs site SEO: crawl budget optimization, sitemap generation, structured data, indexation strategy, and resolving duplicate content.",
      "keywords": ["technical SEO", "sitemap.xml", "robots.txt", "canonicalization", "indexation", "crawl budget", "duplicate content", "URL slug design", "core web vitals"]
    },
    {
      "id": "organic_traffic_analytics_conversion",
      "name": "Organic Traffic Analytics & Conversion Tracking",
      "description": "Analyzing organic search traffic growth, keyword rankings, bounce rate on docs, time-on-page, and doc-to-signup conversion attribution.",
      "keywords": ["Google Analytics 4", "GA4", "Search Console", "organic traffic", "conversion rate", "doc attribution", "bounce rate", "ranking tracking", "traffic growth"]
    },
    {
      "id": "thought_leadership_industry_reports",
      "name": "Thought Leadership & Industry Benchmark Reports",
      "description": "Writing authoritative industry benchmark reports, state-of-the-industry reports, trend analyses, and keynote scripts for executive engineers.",
      "keywords": ["thought leadership", "industry report", "State of DevOps", "benchmark report", "trend analysis", "keynote script", "whitepaper strategy", "market analysis"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Technical blog posts and architectural deep-dive articles",
        "detection": "file_presence",
        "pattern": "blog/.*\\.md|docs/blog/.*\\.md",
        "strength": 0.9,
        "maps_to": [
          "tw_content_marketing_seo.technical_blog_post_authoring"
        ]
      },
      {
        "signal": "Doc metadata, Open Graph tags, and Schema.org TechArticle markup",
        "detection": "content_analysis",
        "pattern": "description:\\s*['\"][^'\"]{30,}['\"]|image:\\s*/img/og-|type:\\s*['\"]TechArticle['\"]|<Head>|meta name=\"keywords\"",
        "strength": 0.85,
        "maps_to": [
          "tw_content_marketing_seo.metadata_schema_seo_basics"
        ]
      },
      {
        "signal": "Keyword research mapping and search intent targeting",
        "detection": "content_analysis",
        "pattern": "keywords:\\s*\\[|search_intent:|target_query:",
        "strength": 0.75,
        "maps_to": [
          "tw_content_marketing_seo.keyword_research_search_intent"
        ]
      },
      {
        "signal": "Technical whitepapers, architecture blueprints, and solution ebooks",
        "detection": "file_presence",
        "pattern": "whitepapers/.*\\.md|docs/whitepapers/.*\\.md|solution-briefs/",
        "strength": 0.85,
        "maps_to": [
          "tw_content_marketing_seo.technical_whitepapers_ebooks"
        ]
      },
      {
        "signal": "Customer migration case studies with quantifiable ROI metrics",
        "detection": "content_analysis",
        "pattern": "docs/case-studies/.*\\.md|Challenge|Solution|Results|Migration Story",
        "strength": 0.85,
        "maps_to": [
          "tw_content_marketing_seo.case_studies_customer_stories"
        ]
      },
      {
        "signal": "Developer community content, Show HN launch drafts, and newsletters",
        "detection": "file_presence",
        "pattern": "community/.*\\.md|newsletter/.*\\.md|Show HN",
        "strength": 0.8,
        "maps_to": [
          "tw_content_marketing_seo.developer_advocacy_community_content"
        ]
      },
      {
        "signal": "Technical SEO architecture (sitemap, robots.txt, canonicalization)",
        "detection": "file_presence",
        "pattern": "static/robots\\.txt|static/sitemap.*\\.xml|canonicalURL",
        "strength": 0.85,
        "maps_to": [
          "tw_content_marketing_seo.technical_seo_information_architecture"
        ]
      },
      {
        "signal": "Organic traffic conversion attribution and annual benchmark reports",
        "detection": "content_analysis",
        "pattern": "gtag\\('event',\\s*'conversion'|State of|Benchmark Report|Survey Methodology",
        "strength": 0.8,
        "maps_to": [
          "tw_content_marketing_seo.organic_traffic_analytics_conversion",
          "tw_content_marketing_seo.thought_leadership_industry_reports"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Published technical blog posts and whitepapers that drove 150k+ monthly organic visitors to developer documentation portal",
        "strength": 0.6,
        "maps_to": [
          "tw_content_marketing_seo.technical_blog_post_authoring",
          "tw_content_marketing_seo.technical_whitepapers_ebooks",
          "tw_content_marketing_seo.organic_traffic_analytics_conversion"
        ]
      },
      {
        "signal": "Optimized documentation SEO with structured metadata, schema.org markup, and strategic keyword clustering",
        "strength": 0.5,
        "maps_to": [
          "tw_content_marketing_seo.metadata_schema_seo_basics",
          "tw_content_marketing_seo.keyword_research_search_intent",
          "tw_content_marketing_seo.technical_seo_information_architecture"
        ]
      },
      {
        "signal": "Authored high-converting engineering case studies, community launch posts, and annual State of Technology benchmark reports",
        "strength": 0.5,
        "maps_to": [
          "tw_content_marketing_seo.case_studies_customer_stories",
          "tw_content_marketing_seo.developer_advocacy_community_content",
          "tw_content_marketing_seo.thought_leadership_industry_reports"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Demonstrated expertise in Technical Content Marketing, Developer Advocacy, Technical SEO, and Whitepaper Authoring",
        "strength": 0.4,
        "maps_to": [
          "tw_content_marketing_seo.technical_blog_post_authoring",
          "tw_content_marketing_seo.metadata_schema_seo_basics",
          "tw_content_marketing_seo.keyword_research_search_intent",
          "tw_content_marketing_seo.technical_whitepapers_ebooks",
          "tw_content_marketing_seo.case_studies_customer_stories",
          "tw_content_marketing_seo.developer_advocacy_community_content",
          "tw_content_marketing_seo.technical_seo_information_architecture",
          "tw_content_marketing_seo.organic_traffic_analytics_conversion",
          "tw_content_marketing_seo.thought_leadership_industry_reports"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes technical content marketing and SEO assessment covering technical blog writing, metadata optimization, whitepapers, and analytics",
        "strength": 1.0,
        "maps_to": [
          "tw_content_marketing_seo.technical_blog_post_authoring",
          "tw_content_marketing_seo.metadata_schema_seo_basics",
          "tw_content_marketing_seo.keyword_research_search_intent",
          "tw_content_marketing_seo.technical_whitepapers_ebooks",
          "tw_content_marketing_seo.case_studies_customer_stories",
          "tw_content_marketing_seo.developer_advocacy_community_content",
          "tw_content_marketing_seo.technical_seo_information_architecture",
          "tw_content_marketing_seo.organic_traffic_analytics_conversion",
          "tw_content_marketing_seo.thought_leadership_industry_reports"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "technical_blog_post_authoring",
        "metadata_schema_seo_basics",
        "keyword_research_search_intent"
      ],
      "description": "Writes developer-focused technical blog posts, adds structured metadata/title tags, and conducts keyword research."
    },
    "mid": {
      "expected_subskills": [
        "technical_whitepapers_ebooks",
        "case_studies_customer_stories",
        "developer_advocacy_community_content"
      ],
      "description": "Authors technical whitepapers, writes customer architecture migration stories, and drives developer community advocacy."
    },
    "senior": {
      "expected_subskills": [
        "technical_seo_information_architecture",
        "organic_traffic_analytics_conversion",
        "thought_leadership_industry_reports"
      ],
      "description": "Architects technical SEO crawl structures, analyzes organic conversion attribution in GA4, and authors industry benchmark reports."
    }
  }
}

# 6. tw_tooling_analytics_distribution
skills["tw_tooling_analytics_distribution"] = {
  "skill_id": "tw_tooling_analytics_distribution",
  "name": "Docs-as-Code, Tooling & Distribution",
  "category": "tooling_distribution",
  "description": "Operating Docs-as-Code workflows: Git/GitHub version control, static site generators (Docusaurus, MkDocs, Sphinx), Markdown/MDX, automated linting (Vale, markdownlint), CI/CD pipelines, doc search, and documentation analytics.",
  "subskills": [
    {
      "id": "markdown_mdx_mastery",
      "name": "Markdown, MDX & Frontmatter Mastery",
      "description": "Expert authoring in Markdown, CommonMark, GitHub Flavored Markdown (GFM), and MDX components (interactive tabs, code blocks, alerts, callouts).",
      "keywords": ["Markdown", "MDX", "CommonMark", "GFM", "frontmatter", "code blocks", "admonitions", "callouts", "markdown tables", "interactive components"]
    },
    {
      "id": "git_github_docs_workflow",
      "name": "Git, GitHub PR Workflows & Version Control",
      "description": "Managing documentation in Git: branching, pull requests, merge conflict resolution, conventional commits, and collaborative review on GitHub/GitLab.",
      "keywords": ["Git", "GitHub", "pull request", "branching", "PR review", "conventional commits", "git merge", "git rebase", "docs repo", "GitLab MR"]
    },
    {
      "id": "static_site_generators_ssg",
      "name": "Static Site Generators (SSG) Configuration",
      "description": "Configuring and customizing modern documentation SSGs: Docusaurus, MkDocs (Material), Sphinx (reStructuredText), Astro, Nextra, Hugo, and VitePress.",
      "keywords": ["Docusaurus", "MkDocs", "Material for MkDocs", "Sphinx", "conf.py", "docusaurus.config.js", "mkdocs.yml", "Nextra", "VitePress", "Hugo"]
    },
    {
      "id": "automated_style_linting",
      "name": "Automated Style Linting (Vale, markdownlint)",
      "description": "Configuring and running automated prose and markdown linters: Vale (.vale.ini), markdownlint (.markdownlint.json), textlint, and proselint.",
      "keywords": ["Vale", ".vale.ini", "markdownlint", "textlint", "proselint", "prose linter", "style rule automation", "grammar check", "linter config"]
    },
    {
      "id": "ci_cd_docs_pipelines",
      "name": "Docs CI/CD Pipelines & Automated Previews",
      "description": "Building automated CI/CD pipelines (GitHub Actions, GitLab CI) for building docs, running linters, checking broken links (lychee), and deploying preview builds.",
      "keywords": ["GitHub Actions", "CI/CD pipeline", "broken link checker", "lychee", "automated preview", "Vercel preview", "Netlify deploy", "build validation"]
    },
    {
      "id": "site_search_indexing",
      "name": "Documentation Site Search & Algolia Indexing",
      "description": "Integrating and configuring documentation search engines: Algolia DocSearch, Pagefind, Lunr.js, Meilisearch, and search facet indexing.",
      "keywords": ["Algolia DocSearch", "Pagefind", "Lunr.js", "Meilisearch", "site search", "search facets", "indexing hierarchy", "search ranking tuning"]
    },
    {
      "id": "headless_cms_knowledge_tools",
      "name": "Headless CMS & Enterprise Knowledge Platforms",
      "description": "Managing enterprise docs via headless CMS and modern knowledge tools: Contentful, Sanity, Strapi, GitBook, ReadMe, Notion, and Confluence.",
      "keywords": ["headless CMS", "Contentful", "Sanity", "Strapi", "GitBook", "ReadMe.com", "Notion", "Confluence", "structured content platform"]
    },
    {
      "id": "docs_analytics_telemetry",
      "name": "Documentation Analytics & Telemetry Tracking",
      "description": "Setting up documentation telemetry, event tracking, scroll depth tracking, search query analytics (zero-result searches), and heatmaps with GA4 or PostHog.",
      "keywords": ["docs analytics", "PostHog", "GA4 custom events", "zero-result searches", "scroll depth", "search query analysis", "telemetry", "Hotjar", "user engagement"]
    },
    {
      "id": "multi_version_localization_builds",
      "name": "Multi-Version Docs & Translation Pipelines",
      "description": "Architecting multi-version doc release matrices (semver version dropdowns), translation pipelines (Crowdin, Lokalise), and global CDN distribution.",
      "keywords": ["multi-version docs", "version switcher", "i18n", "localization pipeline", "Crowdin", "Lokalise", "PO files", "CDN edge distribution", "docs release matrix"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Markdown and MDX files with frontmatter and component imports",
        "detection": "file_presence",
        "pattern": "docs/.*\\.mdx$",
        "strength": 0.9,
        "maps_to": [
          "tw_tooling_analytics_distribution.markdown_mdx_mastery"
        ]
      },
      {
        "signal": "Git collaborative documentation workflows (PR templates, conventional commits)",
        "detection": "file_presence",
        "pattern": "\\.github/PULL_REQUEST_TEMPLATE/.*\\.md|\\.github/workflows/*doc*\\.ya?ml",
        "strength": 0.85,
        "maps_to": [
          "tw_tooling_analytics_distribution.git_github_docs_workflow"
        ]
      },
      {
        "signal": "Static site generator (SSG) configuration files",
        "detection": "file_presence",
        "pattern": "docusaurus\\.config\\.(js|ts)|mkdocs\\.yml|conf\\.py|astro\\.config\\.(mjs|ts)|nextra\\.config\\.(js|ts)",
        "strength": 0.95,
        "maps_to": [
          "tw_tooling_analytics_distribution.static_site_generators_ssg"
        ]
      },
      {
        "signal": "Automated style and markdown linter configuration files",
        "detection": "file_presence",
        "pattern": "\\.vale\\.ini|\\.markdownlint\\.(json|ya?ml)|\\.textlintrc",
        "strength": 0.9,
        "maps_to": [
          "tw_tooling_analytics_distribution.automated_style_linting"
        ]
      },
      {
        "signal": "Docs CI/CD build, lint, and broken link verification workflows",
        "detection": "content_analysis",
        "pattern": "lychee|vale-action|docusaurus build|mkdocs build|deploy-to-gh-pages",
        "strength": 0.9,
        "maps_to": [
          "tw_tooling_analytics_distribution.ci_cd_docs_pipelines"
        ]
      },
      {
        "signal": "Algolia DocSearch or Pagefind documentation search integration",
        "detection": "content_analysis",
        "pattern": "algolia:\\s*\\{|appId:\\s*['\"][A-Z0-9]+['\"]|apiKey:\\s*['\"][a-f0-9]+['\"]|indexName:|pagefind",
        "strength": 0.85,
        "maps_to": [
          "tw_tooling_analytics_distribution.site_search_indexing"
        ]
      },
      {
        "signal": "Headless CMS and structured knowledge platform integration",
        "detection": "content_analysis",
        "pattern": "contentful|sanity|strapi|gitbook|readme-io",
        "strength": 0.8,
        "maps_to": [
          "tw_tooling_analytics_distribution.headless_cms_knowledge_tools"
        ]
      },
      {
        "signal": "Documentation telemetry and user interaction event tracking",
        "detection": "content_analysis",
        "pattern": "posthog\\.init|googleAnalytics:\\s*\\{|gtag\\('event'|scroll_depth",
        "strength": 0.8,
        "maps_to": [
          "tw_tooling_analytics_distribution.docs_analytics_telemetry"
        ]
      },
      {
        "signal": "Multi-version release matrices and Crowdin translation configs",
        "detection": "file_presence",
        "pattern": "crowdin\\.ya?ml|versions\\.json|i18n/.*\\.json|docusaurus-plugin-content-docs",
        "strength": 0.9,
        "maps_to": [
          "tw_tooling_analytics_distribution.multi_version_localization_builds"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Built and maintained Docs-as-Code CI/CD pipelines using GitHub Actions, Docusaurus, MkDocs, and Vale style linters",
        "strength": 0.6,
        "maps_to": [
          "tw_tooling_analytics_distribution.markdown_mdx_mastery",
          "tw_tooling_analytics_distribution.static_site_generators_ssg",
          "tw_tooling_analytics_distribution.automated_style_linting",
          "tw_tooling_analytics_distribution.ci_cd_docs_pipelines"
        ]
      },
      {
        "signal": "Integrated Algolia DocSearch, configured GitBook/ReadMe hubs, and managed Git versioning workflows",
        "strength": 0.5,
        "maps_to": [
          "tw_tooling_analytics_distribution.git_github_docs_workflow",
          "tw_tooling_analytics_distribution.site_search_indexing",
          "tw_tooling_analytics_distribution.headless_cms_knowledge_tools"
        ]
      },
      {
        "signal": "Implemented documentation telemetry with GA4/PostHog and architected multi-version localization workflows with Crowdin",
        "strength": 0.5,
        "maps_to": [
          "tw_tooling_analytics_distribution.docs_analytics_telemetry",
          "tw_tooling_analytics_distribution.multi_version_localization_builds"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Recognized for Docs-as-Code, Static Site Generators (Docusaurus/MkDocs), GitHub Actions CI/CD, and Documentation Analytics",
        "strength": 0.4,
        "maps_to": [
          "tw_tooling_analytics_distribution.markdown_mdx_mastery",
          "tw_tooling_analytics_distribution.git_github_docs_workflow",
          "tw_tooling_analytics_distribution.static_site_generators_ssg",
          "tw_tooling_analytics_distribution.automated_style_linting",
          "tw_tooling_analytics_distribution.ci_cd_docs_pipelines",
          "tw_tooling_analytics_distribution.site_search_indexing",
          "tw_tooling_analytics_distribution.headless_cms_knowledge_tools",
          "tw_tooling_analytics_distribution.docs_analytics_telemetry",
          "tw_tooling_analytics_distribution.multi_version_localization_builds"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive Docs-as-Code assessment covering Markdown/MDX, SSG configs, CI/CD linters, Algolia search, and multi-version builds",
        "strength": 1.0,
        "maps_to": [
          "tw_tooling_analytics_distribution.markdown_mdx_mastery",
          "tw_tooling_analytics_distribution.git_github_docs_workflow",
          "tw_tooling_analytics_distribution.static_site_generators_ssg",
          "tw_tooling_analytics_distribution.automated_style_linting",
          "tw_tooling_analytics_distribution.ci_cd_docs_pipelines",
          "tw_tooling_analytics_distribution.site_search_indexing",
          "tw_tooling_analytics_distribution.headless_cms_knowledge_tools",
          "tw_tooling_analytics_distribution.docs_analytics_telemetry",
          "tw_tooling_analytics_distribution.multi_version_localization_builds"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "markdown_mdx_mastery",
        "git_github_docs_workflow",
        "static_site_generators_ssg"
      ],
      "description": "Writes MDX/Markdown, uses Git pull request review workflows, and runs local builds on Docusaurus/MkDocs."
    },
    "mid": {
      "expected_subskills": [
        "automated_style_linting",
        "ci_cd_docs_pipelines",
        "site_search_indexing",
        "headless_cms_knowledge_tools"
      ],
      "description": "Configures Vale/markdownlint in CI/CD pipelines, integrates Algolia DocSearch, and manages headless CMS portals."
    },
    "senior": {
      "expected_subskills": [
        "docs_analytics_telemetry",
        "multi_version_localization_builds"
      ],
      "description": "Architects multi-version documentation matrices, translation pipelines (Crowdin), and analyzes search queries / telemetry in GA4/PostHog."
    }
  }
}

# Write individual skill files
for skill_id, skill_data in skills.items():
    file_path = os.path.join(skills_dir, f"{skill_id}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(skill_data, f, indent=2, ensure_ascii=False)
    print(f"Generated skill file: {file_path}")

print("\nSkills generation complete.")
