import os
import json

base_dir = os.path.abspath('knowledge-base')
skills_dir = os.path.join(base_dir, 'skills', 'qa-engineer')
evidence_dir = os.path.join(base_dir, 'evidence', 'qa-engineer')
roles_dir = os.path.join(base_dir, 'roles', 'qa-engineer')

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

skills = {}

# 1. qa_fundamentals_methodology
skills["qa_fundamentals_methodology"] = {
  "skill_id": "qa_fundamentals_methodology",
  "name": "QA Mindset, Test Design & STLC",
  "category": "testing_methodology",
  "description": "Core Quality Assurance fundamentals, testing mindset, test levels, STLC lifecycle models, test design techniques, and quality governance. Covers how quality is planned, designed, and measured across the software lifecycle.",
  "subskills": [
    {
      "id": "qa_mindset_principles",
      "name": "QA Mindset & Core Testing Principles",
      "description": "Seven principles of testing, defect prevention vs detection, cost of quality, verification vs validation, and quality culture.",
      "keywords": ["Seven principles of testing", "defect prevention", "cost of quality", "verification vs validation", "quality culture", "exhaustive testing is impossible", "pesticide paradox"]
    },
    {
      "id": "test_levels_types",
      "name": "Test Levels & Black/White/Gray Box",
      "description": "Black-box, white-box, gray-box testing, unit, integration, system, and acceptance testing levels.",
      "keywords": ["Black-box testing", "White-box testing", "Gray-box testing", "System testing", "Integration testing", "Acceptance testing", "functional vs non-functional"]
    },
    {
      "id": "sdlc_stlc_models",
      "name": "SDLC & STLC Methodologies",
      "description": "V-Model, Agile/Scrum/Kanban testing, Shift-Left testing, Shift-Right testing, and Continuous Testing in modern release cycles.",
      "keywords": ["V-Model", "STLC", "Shift-Left", "Shift-Right", "Continuous Testing", "Agile testing", "Sprint testing cycle", "Definition of Done"]
    },
    {
      "id": "test_planning_estimation",
      "name": "Test Planning & Estimation",
      "description": "Test Strategy vs Test Plan, test scope definition, Work Breakdown Structure (WBS), estimation techniques (3-point, planning poker).",
      "keywords": ["Test Plan", "Test Strategy", "test scope", "test estimation", "WBS", "Three-point estimation", "Planning Poker", "entry and exit criteria"]
    },
    {
      "id": "test_design_techniques",
      "name": "Black-Box Test Design Techniques",
      "description": "Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Decision Table Testing, State Transition Testing, and Use Case Testing.",
      "keywords": ["Boundary Value Analysis", "Equivalence Partitioning", "BVA", "Decision Table", "State Transition Testing", "Use Case Testing", "pairwise testing"]
    },
    {
      "id": "test_oracles_heuristics",
      "name": "Test Oracles & Heuristics",
      "description": "Heuristic test evaluation (FEW HICCUPS mnemonic), test oracle determination, expected outcome formulation, and recognizing subtle bugs.",
      "keywords": ["Test oracle", "FEW HICCUPS", "testing heuristics", "consistency heuristics", "expected outcome", "oracle problem"]
    },
    {
      "id": "risk_based_testing",
      "name": "Risk-Based Testing (RBT)",
      "description": "Risk assessment matrix, product risk analysis, failure likelihood vs impact, and prioritizing high-risk business flows.",
      "keywords": ["Risk-Based Testing", "RBT", "risk matrix", "likelihood vs impact", "risk mitigation", "failure mode", "test prioritization"]
    },
    {
      "id": "quality_metrics_governance",
      "name": "Quality Metrics & QA Governance",
      "description": "Defect Removal Efficiency (DRE), defect density, test execution velocity, MTTR, QA sign-off criteria, and quality audit gates.",
      "keywords": ["Defect Removal Efficiency", "DRE", "defect density", "QA sign-off", "quality gates", "MTTR", "test execution velocity", "pass rate"]
    },
    {
      "id": "exploratory_session_management",
      "name": "Session-Based Test Management (SBTM)",
      "description": "Session-Based Test Management (SBTM), charter authoring, timeboxed exploratory coverage, and debriefing sessions.",
      "keywords": ["SBTM", "Session-Based Testing", "test charter", "timeboxing", "exploratory debrief", "opportunity vs bug reporting"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Test plans, test matrices, or test strategy documentation in markdown",
        "detection": "content_analysis",
        "pattern": "Test Strategy|Test Plan|test-plan\\.md|test-strategy\\.md|RBT matrix",
        "strength": 0.7,
        "maps_to": ["qa_fundamentals_methodology.test_planning_estimation", "qa_fundamentals_methodology.risk_based_testing"]
      },
      {
        "signal": "Test design documentation applying EP, BVA, or Decision Tables",
        "detection": "content_analysis",
        "pattern": "Boundary Value Analysis|Equivalence Partition|Decision Table|State Transition",
        "strength": 0.8,
        "maps_to": ["qa_fundamentals_methodology.test_design_techniques", "qa_fundamentals_methodology.test_oracles_heuristics"]
      },
      {
        "signal": "Session-based exploratory test charters or quality metrics reports",
        "detection": "content_analysis",
        "pattern": "test charter|SBTM|DRE|Defect Removal Efficiency|Quality Gate",
        "strength": 0.8,
        "maps_to": ["qa_fundamentals_methodology.exploratory_session_management", "qa_fundamentals_methodology.quality_metrics_governance", "qa_fundamentals_methodology.qa_mindset_principles"]
      }
    ],
    "cv": [
      {
        "signal": "QA testing methodologies, STLC, Agile testing, or test design techniques described",
        "strength": 0.8,
        "maps_to": ["qa_fundamentals_methodology.qa_mindset_principles", "qa_fundamentals_methodology.test_levels_types", "qa_fundamentals_methodology.sdlc_stlc_models", "qa_fundamentals_methodology.test_design_techniques"]
      },
      {
        "signal": "Test planning, test strategy, risk-based testing, or QA governance experience",
        "strength": 0.8,
        "maps_to": ["qa_fundamentals_methodology.test_planning_estimation", "qa_fundamentals_methodology.risk_based_testing", "qa_fundamentals_methodology.quality_metrics_governance", "qa_fundamentals_methodology.exploratory_session_management"]
      }
    ],
    "linkedin": [
      {
        "signal": "Quality Assurance, Test Planning, or STLC endorsed",
        "strength": 0.5,
        "maps_to": ["qa_fundamentals_methodology.qa_mindset_principles", "qa_fundamentals_methodology.test_levels_types", "qa_fundamentals_methodology.sdlc_stlc_models"]
      },
      {
        "signal": "Test Strategy, Risk-Based Testing, or QA Metrics mentioned",
        "strength": 0.5,
        "maps_to": ["qa_fundamentals_methodology.test_planning_estimation", "qa_fundamentals_methodology.risk_based_testing", "qa_fundamentals_methodology.quality_metrics_governance", "qa_fundamentals_methodology.test_oracles_heuristics"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["qa_mindset_principles", "test_levels_types", "sdlc_stlc_models"],
      "description": "Understands fundamental testing principles, applies black-box test types, and works effectively within Agile STLC cycles."
    },
    "mid": {
      "expected_subskills": ["test_planning_estimation", "test_design_techniques", "test_oracles_heuristics"],
      "description": "Designs rigorous test cases using BVA, EP, and decision tables, formulates test plans with accurate estimates, and applies heuristic test oracles."
    },
    "senior": {
      "expected_subskills": ["risk_based_testing", "quality_metrics_governance", "exploratory_session_management"],
      "description": "Architects risk-based testing strategies, enforces quality gate metrics (DRE, MTTR), and leads session-based exploratory test initiatives across teams."
    }
  }
}

# 2. qa_manual_testing
skills["qa_manual_testing"] = {
  "skill_id": "qa_manual_testing",
  "name": "Manual, Exploratory & Functional Testing",
  "category": "manual_testing",
  "description": "Hands-on functional testing, test case authoring, comprehensive defect lifecycle management, exploratory testing execution, cross-browser validation, and user acceptance testing.",
  "subskills": [
    {
      "id": "test_case_authoring",
      "name": "Structured Test Case Authoring",
      "description": "Writing structured test cases with clear preconditions, unambiguous steps, test data, and precise expected results.",
      "keywords": ["Test Case", "preconditions", "test steps", "expected result", "actual result", "test data", "acceptance criteria"]
    },
    {
      "id": "bug_reporting_lifecycle",
      "name": "Defect Reporting & Bug Lifecycle",
      "description": "Writing detailed defect reports (steps to reproduce, environment, logs, severity vs priority, expected vs actual).",
      "keywords": ["Bug report", "defect lifecycle", "severity vs priority", "steps to reproduce", "root cause", "bug triaging", "defect status"]
    },
    {
      "id": "smoke_sanity_testing",
      "name": "Smoke & Sanity Testing",
      "description": "Build acceptance testing, fast sanity verification of core functionality after deployments and hotfixes.",
      "keywords": ["Smoke testing", "Sanity testing", "build verification test", "BVT", "hotfix validation", "critical path testing"]
    },
    {
      "id": "regression_testing_strategy",
      "name": "Regression Testing & Impact Analysis",
      "description": "Impact analysis, regression test suite maintenance, selecting test subsets for release candidate builds.",
      "keywords": ["Regression testing", "impact analysis", "regression suite", "selective regression", "release candidate", "change impact"]
    },
    {
      "id": "exploratory_testing_execution",
      "name": "Exploratory & Ad-hoc Testing",
      "description": "Unscripted bug hunting, edge-case probing, tour-based exploratory testing, persona-based scenarios.",
      "keywords": ["Exploratory testing", "Ad-hoc testing", "tour testing", "edge-case probing", "persona-based testing", "bug hunting"]
    },
    {
      "id": "cross_browser_compatibility",
      "name": "Cross-Browser & Device Compatibility",
      "description": "Cross-browser matrix testing (Chrome, Safari, Firefox, Edge) and cross-OS rendering checks.",
      "keywords": ["Cross-browser testing", "BrowserStack", "SauceLabs", "Safari rendering", "Edge compatibility", "responsive layout checks"]
    },
    {
      "id": "user_acceptance_testing_uat",
      "name": "User Acceptance Testing (UAT) & Sign-Off",
      "description": "Facilitating UAT with business stakeholders, alpha/beta testing coordination, production readiness sign-off.",
      "keywords": ["UAT", "User Acceptance Testing", "alpha testing", "beta testing", "business stakeholder sign-off", "production readiness"]
    },
    {
      "id": "localization_internationalization_testing",
      "name": "Localization (L10n) & i18n Testing",
      "description": "L10n/i18n testing, RTL languages, character encodings (UTF-8), date/time format verifications.",
      "keywords": ["Localization testing", "L10n", "i18n", "RTL layout", "UTF-8 encoding", "currency formatting", "date/time format"]
    },
    {
      "id": "usability_heuristic_evaluation",
      "name": "Usability & Heuristic Evaluation",
      "description": "Nielsen’s usability heuristics, UX anomaly identification, accessibility workflow evaluation.",
      "keywords": ["Usability testing", "Nielsen heuristics", "UX defect", "user experience evaluation", "cognitive walkthrough", "workflow friction"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Test case spreadsheets, markdown matrices, or defect templates in repository",
        "detection": "content_analysis",
        "pattern": "test-cases|test_cases\\.md|defect-template|bug_report\\.md|smoke_checklist",
        "strength": 0.7,
        "maps_to": ["qa_manual_testing.test_case_authoring", "qa_manual_testing.bug_reporting_lifecycle", "qa_manual_testing.smoke_sanity_testing"]
      },
      {
        "signal": "Regression test checklists or cross-browser compatibility matrices",
        "detection": "content_analysis",
        "pattern": "regression_suite|cross_browser_matrix|BrowserStack|SauceLabs",
        "strength": 0.8,
        "maps_to": ["qa_manual_testing.regression_testing_strategy", "qa_manual_testing.cross_browser_compatibility", "qa_manual_testing.exploratory_testing_execution"]
      },
      {
        "signal": "UAT sign-off documentation or localization/usability test logs",
        "detection": "content_analysis",
        "pattern": "UAT_signoff|localization_test|i18n_checklist|usability_heuristics",
        "strength": 0.8,
        "maps_to": ["qa_manual_testing.user_acceptance_testing_uat", "qa_manual_testing.localization_internationalization_testing", "qa_manual_testing.usability_heuristic_evaluation"]
      }
    ],
    "cv": [
      {
        "signal": "Manual testing, test case authoring, bug reporting, or smoke testing described",
        "strength": 0.8,
        "maps_to": ["qa_manual_testing.test_case_authoring", "qa_manual_testing.bug_reporting_lifecycle", "qa_manual_testing.smoke_sanity_testing"]
      },
      {
        "signal": "Regression testing, exploratory testing, UAT, or cross-browser testing leadership",
        "strength": 0.8,
        "maps_to": ["qa_manual_testing.regression_testing_strategy", "qa_manual_testing.exploratory_testing_execution", "qa_manual_testing.cross_browser_compatibility", "qa_manual_testing.user_acceptance_testing_uat"]
      }
    ],
    "linkedin": [
      {
        "signal": "Manual Testing, Bug Tracking, or Test Case Execution endorsed",
        "strength": 0.5,
        "maps_to": ["qa_manual_testing.test_case_authoring", "qa_manual_testing.bug_reporting_lifecycle", "qa_manual_testing.smoke_sanity_testing"]
      },
      {
        "signal": "Regression Testing, Exploratory Testing, or UAT mentioned",
        "strength": 0.5,
        "maps_to": ["qa_manual_testing.regression_testing_strategy", "qa_manual_testing.exploratory_testing_execution", "qa_manual_testing.cross_browser_compatibility", "qa_manual_testing.user_acceptance_testing_uat", "qa_manual_testing.localization_internationalization_testing", "qa_manual_testing.usability_heuristic_evaluation"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["test_case_authoring", "bug_reporting_lifecycle", "smoke_sanity_testing"],
      "description": "Writes clear, reproducible test cases, logs comprehensive bug reports with logs, and executes smoke/sanity testing."
    },
    "mid": {
      "expected_subskills": ["regression_testing_strategy", "exploratory_testing_execution", "cross_browser_compatibility"],
      "description": "Maintains regression suites through impact analysis, uncovers edge cases with exploratory testing, and validates cross-browser matrices."
    },
    "senior": {
      "expected_subskills": ["user_acceptance_testing_uat", "localization_internationalization_testing", "usability_heuristic_evaluation"],
      "description": "Coordinates UAT with business stakeholders, leads L10n/i18n validation across multiple locales, and conducts usability heuristic audits."
    }
  }
}

# 3. qa_web_fundamentals_for_qa
skills["qa_web_fundamentals_for_qa"] = {
  "skill_id": "qa_web_fundamentals_for_qa",
  "name": "Web Fundamentals & Browser DevTools for QA",
  "category": "web_fundamentals",
  "description": "Web technologies and browser architecture from a QA and test automation perspective. Covers HTML DOM inspection, crafting robust locators, browser DevTools debugging, network inspection, and understanding client/server rendering differences.",
  "subskills": [
    {
      "id": "html_dom_inspection",
      "name": "HTML & DOM Tree Inspection",
      "description": "Inspecting HTML elements, semantic tags, accessibility tree, DOM node hierarchy in DevTools.",
      "keywords": ["DOM tree", "HTML elements", "accessibility tree", "node hierarchy", "DevTools Elements tab", "shadow DOM", "iframe inspection"]
    },
    {
      "id": "css_xpath_selectors",
      "name": "CSS & XPath Locators for Automation",
      "description": "Crafting robust CSS selectors and XPath queries (relative, text(), contains(), axis navigation) for automation locators.",
      "keywords": ["XPath", "CSS selector", "relative XPath", "contains()", "ancestor axis", "robust locator", "data-testid selector"]
    },
    {
      "id": "browser_devtools_debugging",
      "name": "Browser DevTools & Console Debugging",
      "description": "Using DevTools Elements, Console, Network, and Application tabs to inspect runtime state and JavaScript exceptions.",
      "keywords": ["DevTools Console", "JavaScript error", "unhandled rejection", "stack trace", "Console logging", "DOM breakpoint"]
    },
    {
      "id": "http_network_inspection",
      "name": "Network Tab & HTTP Request Inspection",
      "description": "Analyzing HTTP requests, status codes (2xx, 4xx, 5xx), request/response headers, payloads, and cookies in DevTools Network tab.",
      "keywords": ["Network tab", "HTTP status code", "request headers", "response payload", "timing waterfall", "XHR/Fetch filter", "HAR file"]
    },
    {
      "id": "client_side_storage_inspection",
      "name": "Client-Side Storage & Cookies Inspection",
      "description": "Inspecting and manipulating LocalStorage, SessionStorage, Cookies, and IndexedDB during test execution.",
      "keywords": ["LocalStorage", "SessionStorage", "Cookies", "IndexedDB", "Application tab", "clear session state", "auth token storage"]
    },
    {
      "id": "rendering_architectures_qa",
      "name": "CSR vs SSR & Hydration Impacts",
      "description": "Understanding CSR (Client-Side Rendering) vs SSR (Server-Side Rendering) impacts on locator readiness and hydration delays.",
      "keywords": ["CSR vs SSR", "hydration delay", "client-side rendering", "server-side rendering", "DOM ready vs load", "locator readiness"]
    },
    {
      "id": "responsive_viewport_testing",
      "name": "Responsive Viewports & Device Emulation",
      "description": "Testing mobile viewports, CSS media queries, and responsive breakpoint behavior via device emulation.",
      "keywords": ["Device emulation", "responsive breakpoints", "viewport dimensions", "touch simulation", "CSS media queries", "mobile emulation"]
    },
    {
      "id": "web_performance_profiling_qa",
      "name": "Lighthouse & Core Web Vitals Auditing",
      "description": "Using Lighthouse and Core Web Vitals (LCP, FID, CLS, INP) to detect front-end performance regressions.",
      "keywords": ["Lighthouse audit", "Core Web Vitals", "LCP", "CLS", "FID", "INP", "performance score", "speed index"]
    },
    {
      "id": "websocket_sse_event_inspection",
      "name": "WebSocket & Streaming Event Inspection",
      "description": "Inspecting real-time WebSocket frames, Server-Sent Events, and streaming responses in browser networks.",
      "keywords": ["WebSocket frames", "Server-Sent Events", "SSE", "real-time events", "socket connection", "streaming payload"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Custom XPath/CSS helper functions or locator utility classes",
        "detection": "content_analysis",
        "pattern": "xpath|querySelector|getByTestId|//div\\[|data-test",
        "strength": 0.7,
        "maps_to": ["qa_web_fundamentals_for_qa.html_dom_inspection", "qa_web_fundamentals_for_qa.css_xpath_selectors"]
      },
      {
        "signal": "Browser storage manipulation or HAR network analysis scripts",
        "detection": "content_analysis",
        "pattern": "localStorage\\.getItem|sessionStorage|document\\.cookie|\\.har|HAR",
        "strength": 0.8,
        "maps_to": ["qa_web_fundamentals_for_qa.http_network_inspection", "qa_web_fundamentals_for_qa.client_side_storage_inspection", "qa_web_fundamentals_for_qa.browser_devtools_debugging"]
      },
      {
        "signal": "Lighthouse CI audit configuration or responsive emulation fixtures",
        "detection": "content_analysis",
        "pattern": "lighthouse|lighthouserc|viewport:.*width|setViewportSize|core-web-vitals",
        "strength": 0.8,
        "maps_to": ["qa_web_fundamentals_for_qa.web_performance_profiling_qa", "qa_web_fundamentals_for_qa.responsive_viewport_testing", "qa_web_fundamentals_for_qa.rendering_architectures_qa", "qa_web_fundamentals_for_qa.websocket_sse_event_inspection"]
      }
    ],
    "cv": [
      {
        "signal": "DevTools debugging, XPath/CSS locator creation, or Network traffic inspection",
        "strength": 0.8,
        "maps_to": ["qa_web_fundamentals_for_qa.html_dom_inspection", "qa_web_fundamentals_for_qa.css_xpath_selectors", "qa_web_fundamentals_for_qa.browser_devtools_debugging", "qa_web_fundamentals_for_qa.http_network_inspection"]
      },
      {
        "signal": "Lighthouse performance audits, responsive testing, or browser storage management",
        "strength": 0.8,
        "maps_to": ["qa_web_fundamentals_for_qa.client_side_storage_inspection", "qa_web_fundamentals_for_qa.rendering_architectures_qa", "qa_web_fundamentals_for_qa.responsive_viewport_testing", "qa_web_fundamentals_for_qa.web_performance_profiling_qa", "qa_web_fundamentals_for_qa.websocket_sse_event_inspection"]
      }
    ],
    "linkedin": [
      {
        "signal": "Browser DevTools, HTML/CSS, or XPath endorsed",
        "strength": 0.5,
        "maps_to": ["qa_web_fundamentals_for_qa.html_dom_inspection", "qa_web_fundamentals_for_qa.css_xpath_selectors", "qa_web_fundamentals_for_qa.browser_devtools_debugging"]
      },
      {
        "signal": "Web Performance, Lighthouse, or Network Debugging mentioned",
        "strength": 0.5,
        "maps_to": ["qa_web_fundamentals_for_qa.http_network_inspection", "qa_web_fundamentals_for_qa.client_side_storage_inspection", "qa_web_fundamentals_for_qa.web_performance_profiling_qa", "qa_web_fundamentals_for_qa.responsive_viewport_testing", "qa_web_fundamentals_for_qa.rendering_architectures_qa", "qa_web_fundamentals_for_qa.websocket_sse_event_inspection"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["html_dom_inspection", "css_xpath_selectors", "browser_devtools_debugging"],
      "description": "Inspects DOM trees in DevTools, crafts robust XPath/CSS selectors for automation, and debugs console errors."
    },
    "mid": {
      "expected_subskills": ["http_network_inspection", "client_side_storage_inspection", "rendering_architectures_qa", "responsive_viewport_testing"],
      "description": "Analyzes HTTP network traffic and cookies/storage in tests, handles CSR/SSR timing differences, and validates responsive viewports."
    },
    "senior": {
      "expected_subskills": ["web_performance_profiling_qa", "websocket_sse_event_inspection"],
      "description": "Audits Core Web Vitals and Lighthouse metrics in CI, and inspects real-time WebSocket/SSE streaming events."
    }
  }
}

# 4. qa_frontend_automation
skills["qa_frontend_automation"] = {
  "skill_id": "qa_frontend_automation",
  "name": "E2E Web & UI Test Automation",
  "category": "frontend_automation",
  "description": "End-to-end (E2E) web and user interface test automation using modern frameworks (Playwright, Cypress, Selenium). IMPORTANT DISTINCTION: This skill is fundamentally different from Frontend's fe_testing. In fe_testing, the frontend developer writes isolated unit and component tests (Jest, Vitest, React Testing Library) to verify their own code logic. In qa_frontend_automation, the QA engineer automates full, end-to-end user journeys across multiple pages, services, and realistic network conditions to validate the complete integrated application.",
  "subskills": [
    {
      "id": "cypress_basics",
      "name": "Cypress E2E Testing",
      "description": "Writing end-to-end user tests in Cypress, cy commands, fixtures, assertions, and test runner execution.",
      "keywords": ["Cypress", "cy.visit", "cy.get", "cy.intercept", "cypress.config.js", "cypress run", "Chai assertions"]
    },
    {
      "id": "playwright_basics",
      "name": "Playwright E2E Testing",
      "description": "Playwright test setup, page fixtures, locators, auto-waiting, and cross-browser test runs.",
      "keywords": ["Playwright", "page.goto", "page.locator", "expect(page)", "playwright.config.ts", "test.describe", "auto-waiting"]
    },
    {
      "id": "locator_strategies_best_practices",
      "name": "Resilient Locator Strategies",
      "description": "Using resilient user-facing locators (getByRole, getByTestId, getByLabel) over brittle DOM-coupled selectors.",
      "keywords": ["getByRole", "getByTestId", "getByLabel", "getByText", "user-centric locators", "avoiding brittle selectors"]
    },
    {
      "id": "page_object_model_pom",
      "name": "Page Object Model (POM) Architecture",
      "description": "Structuring test code with Page Object Model (POM) and Page Component encapsulation.",
      "keywords": ["Page Object Model", "POM", "page class", "component object", "reusable page actions", "locators encapsulation"]
    },
    {
      "id": "handling_async_waits_flakiness",
      "name": "Async Handling & Flakiness Mitigation",
      "description": "Mitigating test flakiness, explicit waits, network idle assertions, retry strategies, and avoiding hardcoded sleeps.",
      "keywords": ["Test flakiness", "explicit wait", "waitForURL", "waitForResponse", "networkidle", "retry mechanism", "avoiding sleep"]
    },
    {
      "id": "mocking_network_interception",
      "name": "Network Interception & API Mocking in E2E",
      "description": "Intercepting and stubbing network requests (cy.intercept, page.route) for deterministic front-end state testing.",
      "keywords": ["cy.intercept", "page.route", "network stubbing", "mocking API response", "simulating 500 error", "deterministic testing"]
    },
    {
      "id": "cross_browser_device_automation",
      "name": "Cross-Browser & Emulated Execution",
      "description": "Running automated suites across Chromium, Firefox, WebKit, and emulated mobile devices.",
      "keywords": ["Chromium", "WebKit", "Firefox", "device emulation in Playwright", "cross-browser automation", "headless execution"]
    },
    {
      "id": "visual_regression_testing",
      "name": "Visual Regression Testing",
      "description": "Pixel-by-pixel and DOM snapshot diffing using tools like Applitools, Percy, or Playwright toHaveScreenshot.",
      "keywords": ["Visual regression", "toHaveScreenshot", "Percy", "Applitools", "pixel diff", "visual baseline", "snapshot comparison"]
    },
    {
      "id": "parallel_distributed_test_execution",
      "name": "Parallel Execution & Test Sharding",
      "description": "Sharding test suites across CI matrix workers, parallel execution in Docker, Playwright sharding.",
      "keywords": ["Playwright shard", "parallel test execution", "CI matrix workers", "test execution optimization", "dockerized test runners"]
    },
    {
      "id": "custom_framework_architecture",
      "name": "Custom Test Framework Architecture",
      "description": "Building extensible TypeScript test frameworks with custom reporters, test fixtures, and data-driven engines.",
      "keywords": ["Custom test framework", "custom fixtures", "custom reporter", "data-driven automation", "test hooks", "test architecture"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Cypress test suites and configuration files",
        "detection": "content_analysis",
        "pattern": "cypress\\.config\\.|cypress/e2e/|cy\\.visit|cy\\.intercept",
        "strength": 0.9,
        "maps_to": ["qa_frontend_automation.cypress_basics", "qa_frontend_automation.mocking_network_interception"]
      },
      {
        "signal": "Playwright test suites, page objects, and configuration",
        "detection": "content_analysis",
        "pattern": "playwright\\.config\\.|@playwright/test|page\\.locator|page\\.route|getByRole",
        "strength": 0.9,
        "maps_to": ["qa_frontend_automation.playwright_basics", "qa_frontend_automation.locator_strategies_best_practices", "qa_frontend_automation.page_object_model_pom"]
      },
      {
        "signal": "Visual regression comparisons or snapshot assertions",
        "detection": "content_analysis",
        "pattern": "toHaveScreenshot|percySnapshot|applitools|eyes\\.check",
        "strength": 0.8,
        "maps_to": ["qa_frontend_automation.visual_regression_testing"]
      },
      {
        "signal": "Parallel sharding configurations or custom test fixture frameworks",
        "detection": "content_analysis",
        "pattern": "--shard=|workers:\\s*[0-9]+|test\\.extend\\<|customReporter",
        "strength": 0.8,
        "maps_to": ["qa_frontend_automation.parallel_distributed_test_execution", "qa_frontend_automation.custom_framework_architecture", "qa_frontend_automation.handling_async_waits_flakiness", "qa_frontend_automation.cross_browser_device_automation"]
      }
    ],
    "cv": [
      {
        "signal": "E2E automation with Cypress, Playwright, or Selenium using Page Object Model",
        "strength": 0.8,
        "maps_to": ["qa_frontend_automation.cypress_basics", "qa_frontend_automation.playwright_basics", "qa_frontend_automation.page_object_model_pom", "qa_frontend_automation.locator_strategies_best_practices"]
      },
      {
        "signal": "Visual regression testing, framework architecture, or CI test parallelization",
        "strength": 0.8,
        "maps_to": ["qa_frontend_automation.handling_async_waits_flakiness", "qa_frontend_automation.mocking_network_interception", "qa_frontend_automation.visual_regression_testing", "qa_frontend_automation.parallel_distributed_test_execution", "qa_frontend_automation.custom_framework_architecture", "qa_frontend_automation.cross_browser_device_automation"]
      }
    ],
    "linkedin": [
      {
        "signal": "Playwright, Cypress, or Test Automation endorsed",
        "strength": 0.5,
        "maps_to": ["qa_frontend_automation.cypress_basics", "qa_frontend_automation.playwright_basics", "qa_frontend_automation.locator_strategies_best_practices"]
      },
      {
        "signal": "Page Object Model, Visual Testing, or Test Architecture mentioned",
        "strength": 0.5,
        "maps_to": ["qa_frontend_automation.page_object_model_pom", "qa_frontend_automation.visual_regression_testing", "qa_frontend_automation.parallel_distributed_test_execution", "qa_frontend_automation.custom_framework_architecture", "qa_frontend_automation.mocking_network_interception", "qa_frontend_automation.handling_async_waits_flakiness", "qa_frontend_automation.cross_browser_device_automation"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["cypress_basics", "playwright_basics", "locator_strategies_best_practices"],
      "description": "Writes automated UI tests using Cypress and Playwright using resilient locator strategies (getByRole/getByTestId)."
    },
    "mid": {
      "expected_subskills": ["page_object_model_pom", "handling_async_waits_flakiness", "mocking_network_interception", "cross_browser_device_automation"],
      "description": "Architects Page Object Model suites, intercepts network traffic, eliminates flakiness with explicit waiting, and runs cross-browser tests."
    },
    "senior": {
      "expected_subskills": ["visual_regression_testing", "parallel_distributed_test_execution", "custom_framework_architecture"],
      "description": "Builds extensible TypeScript automation frameworks, implements visual regression testing, and shards parallel test runs across CI nodes."
    }
  }
}

# 5. qa_backend_api_automation
skills["qa_backend_api_automation"] = {
  "skill_id": "qa_backend_api_automation",
  "name": "API & Backend Integration Test Automation",
  "category": "api_automation",
  "description": "Automated API testing, contract validation, and backend service verification using Postman, REST Assured, and Pact. IMPORTANT DISTINCTION: This skill is fundamentally different from Backend's be_testing_quality. In be_testing_quality, backend developers write unit tests and internal service integration tests for their own controllers/services. In qa_backend_api_automation, the QA engineer validates published API endpoints over HTTP, chains multi-service workflows, enforces schema contracts, and inspects database state solely as a test oracle after API operations (checking inserted/updated rows match expected test assertions — NOT database schema design or indexing optimization, which belongs to be_databases).",
  "subskills": [
    {
      "id": "postman_newman_testing",
      "name": "Postman & Newman Automation",
      "description": "Writing JavaScript assertions in Postman test scripts, environment variables, and CLI execution via Newman.",
      "keywords": ["Postman", "Newman", "pm.test", "pm.expect", "postman_collection.json", "environment variables", "CLI test run"]
    },
    {
      "id": "http_api_test_authoring",
      "name": "REST API Endpoint Validation",
      "description": "Testing RESTful endpoints (GET, POST, PUT, DELETE, PATCH), validating JSON response schemas and HTTP status codes.",
      "keywords": ["REST API testing", "HTTP methods", "status codes", "JSON response validation", "request payload", "header verification"]
    },
    {
      "id": "rest_assured_framework",
      "name": "REST Assured Framework (Java/JVM)",
      "description": "Building Java/JVM-based API test automation suites using REST Assured (given-when-then syntax, Hamcrest matchers).",
      "keywords": ["REST Assured", "given().when().then()", "Hamcrest matchers", "Java API testing", "body validation", "request specification"]
    },
    {
      "id": "api_test_chaining_state",
      "name": "API State Management & Request Chaining",
      "description": "Extracting response tokens/IDs to dynamically parameterize subsequent downstream API requests.",
      "keywords": ["Request chaining", "token extraction", "dynamic test data", "OAuth bearer token reuse", "session state propagation"]
    },
    {
      "id": "json_xml_schema_validation",
      "name": "JSON Schema & Contract Validation",
      "description": "Validating JSON Schema / XML DTD compliance against OpenAPI specifications to catch contract breaking changes.",
      "keywords": ["JSON Schema validation", "schema validator", "OpenAPI contract check", "breaking change detection", "XML DTD validation"]
    },
    {
      "id": "graphql_grpc_api_testing",
      "name": "GraphQL & gRPC API Testing",
      "description": "Testing GraphQL queries/mutations with variables and testing gRPC endpoints with Protobuf payloads.",
      "keywords": ["GraphQL testing", "GraphQL query/mutation", "gRPC testing", "Protobuf payload", "grpcurl", "GraphQL variables"]
    },
    {
      "id": "mock_servers_service_virtualization",
      "name": "Service Virtualization & WireMock",
      "description": "Setting up WireMock, Mockoon, or Prism mock servers for third-party dependency isolation in integration suites.",
      "keywords": ["WireMock", "Mockoon", "Prism", "service virtualization", "third-party API stubbing", "mock server"]
    },
    {
      "id": "contract_testing_pact_qa",
      "name": "Consumer-Driven Contract Testing (Pact)",
      "description": "Consumer-Driven Contract Testing from a QA perspective using Pact and Pact Broker.",
      "keywords": ["Pact", "Pact Broker", "consumer-driven contract", "provider verification", "contract testing", "can-i-deploy"]
    },
    {
      "id": "database_validation_in_automation",
      "name": "Database State Validation (Test Oracle)",
      "description": "Querying PostgreSQL/MySQL/MongoDB from test code to verify that API operations resulted in the correct persisted database state (using DB strictly as a test oracle).",
      "keywords": ["Database state verification", "DB test oracle", "SQL query in test", "persistence check", "data integrity assertion", "cleaning test records"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Postman collections with test scripts (.postman_collection.json)",
        "detection": "file_presence",
        "pattern": "*\\.postman_collection\\.json|*\\.postman_environment\\.json",
        "strength": 0.8,
        "maps_to": ["qa_backend_api_automation.postman_newman_testing", "qa_backend_api_automation.http_api_test_authoring"]
      },
      {
        "signal": "REST Assured or Supertest API automation code",
        "detection": "content_analysis",
        "pattern": "RestAssured\\.given|\\.statusCode\\(|given\\(\\)\\.when\\(\\)|pm\\.test\\(",
        "strength": 0.9,
        "maps_to": ["qa_backend_api_automation.rest_assured_framework", "qa_backend_api_automation.api_test_chaining_state", "qa_backend_api_automation.json_xml_schema_validation"]
      },
      {
        "signal": "Pact contract files, WireMock stubs, or GraphQL/gRPC test clients",
        "detection": "content_analysis",
        "pattern": "pact-jvm|PactBuilder|wiremock|Mockoon|grpcurl|graphql-request",
        "strength": 0.8,
        "maps_to": ["qa_backend_api_automation.contract_testing_pact_qa", "qa_backend_api_automation.mock_servers_service_virtualization", "qa_backend_api_automation.graphql_grpc_api_testing", "qa_backend_api_automation.database_validation_in_automation"]
      }
    ],
    "cv": [
      {
        "signal": "API test automation with Postman, REST Assured, or Newman",
        "strength": 0.8,
        "maps_to": ["qa_backend_api_automation.postman_newman_testing", "qa_backend_api_automation.http_api_test_authoring", "qa_backend_api_automation.rest_assured_framework"]
      },
      {
        "signal": "Contract testing with Pact, service virtualization with WireMock, or GraphQL testing",
        "strength": 0.8,
        "maps_to": ["qa_backend_api_automation.api_test_chaining_state", "qa_backend_api_automation.json_xml_schema_validation", "qa_backend_api_automation.graphql_grpc_api_testing", "qa_backend_api_automation.mock_servers_service_virtualization", "qa_backend_api_automation.contract_testing_pact_qa", "qa_backend_api_automation.database_validation_in_automation"]
      }
    ],
    "linkedin": [
      {
        "signal": "API Testing, Postman, or REST Assured endorsed",
        "strength": 0.5,
        "maps_to": ["qa_backend_api_automation.postman_newman_testing", "qa_backend_api_automation.http_api_test_authoring", "qa_backend_api_automation.rest_assured_framework"]
      },
      {
        "signal": "Contract Testing, WireMock, or GraphQL Testing mentioned",
        "strength": 0.5,
        "maps_to": ["qa_backend_api_automation.api_test_chaining_state", "qa_backend_api_automation.json_xml_schema_validation", "qa_backend_api_automation.graphql_grpc_api_testing", "qa_backend_api_automation.mock_servers_service_virtualization", "qa_backend_api_automation.contract_testing_pact_qa", "qa_backend_api_automation.database_validation_in_automation"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["postman_newman_testing", "http_api_test_authoring"],
      "description": "Writes REST API tests in Postman with JavaScript assertions and executes test collections using Newman."
    },
    "mid": {
      "expected_subskills": ["rest_assured_framework", "api_test_chaining_state", "json_xml_schema_validation", "graphql_grpc_api_testing"],
      "description": "Builds REST Assured automated suites, handles dynamic request token chaining, validates JSON schemas, and tests GraphQL/gRPC endpoints."
    },
    "senior": {
      "expected_subskills": ["mock_servers_service_virtualization", "contract_testing_pact_qa", "database_validation_in_automation"],
      "description": "Establishes Consumer-Driven Contract Testing with Pact, configures WireMock virtualization for third-party isolation, and validates database state as a test oracle."
    }
  }
}

# 6. qa_non_functional_testing
skills["qa_non_functional_testing"] = {
  "skill_id": "qa_non_functional_testing",
  "name": "Performance, Accessibility & Security Verification",
  "category": "non_functional_testing",
  "description": "Non-functional quality verification including load/stress testing (k6, JMeter), accessibility compliance (WCAG, axe-core), and basic application security validation. IMPORTANT DISTINCTION: In security testing, the QA engineer verifies that known vulnerability classes (OWASP Top 10 like SQLi, XSS, CSRF, missing auth headers, IDOR) are checked and blocked during quality gates; this is fundamentally different from Cyber Security's cs_threats_and_attacks where security analysts develop exploit payloads, conduct penetration testing, and analyze attacker TTPs.",
  "subskills": [
    {
      "id": "jmeter_load_testing",
      "name": "Apache JMeter Load Testing",
      "description": "Creating Thread Groups, HTTP Request Samplers, View Results Tree, and basic throughput assertions in Apache JMeter.",
      "keywords": ["JMeter", "Thread Group", "HTTP Sampler", "View Results Tree", "Aggregate Report", "JMeter assertion", "Throughput"]
    },
    {
      "id": "accessibility_testing_axe_wave",
      "name": "Automated Accessibility Testing (WCAG/axe)",
      "description": "Running automated WCAG 2.1 AA audits using axe-core, WAVE, and Lighthouse Accessibility.",
      "keywords": ["axe-core", "WAVE", "WCAG 2.1 AA", "color contrast", "aria-label", "alt attributes", "accessibility audit"]
    },
    {
      "id": "k6_performance_as_code",
      "name": "k6 Performance as Code",
      "description": "Writing JavaScript load testing scripts in k6 (virtual users, stages, thresholds for p95/p99 latency).",
      "keywords": ["k6", "Virtual Users", "k6 thresholds", "p95 latency", "p99 latency", "k6 stages", "k6 load script"]
    },
    {
      "id": "performance_test_types_scenarios",
      "name": "Load, Stress, Spike & Soak Testing",
      "description": "Designing Load, Stress, Spike, Soak (Endurance), and Breakpoint testing profiles.",
      "keywords": ["Load testing", "Stress testing", "Spike testing", "Soak testing", "Endurance testing", "Breakpoint testing", "throughput target"]
    },
    {
      "id": "server_resource_monitoring_during_load",
      "name": "Resource Monitoring During Load Tests",
      "description": "Correlating load generation with CPU/Memory/I/O bottlenecks and database connection pool saturation.",
      "keywords": ["Server monitoring under load", "CPU bottleneck", "memory leak under load", "connection pool saturation", "I/O wait"]
    },
    {
      "id": "app_security_verification_owasp",
      "name": "OWASP Top 10 Quality Gate Verification",
      "description": "Verifying defensive controls against OWASP Top 10 (SQLi, XSS, CSRF, insecure direct object references, missing auth headers).",
      "keywords": ["OWASP Top 10 testing", "XSS input check", "SQLi parameter check", "CSRF token verification", "security headers check", "IDOR verification"]
    },
    {
      "id": "distributed_load_generation",
      "name": "Distributed Load Testing at Scale",
      "description": "Orchestrating distributed load generators across multi-node clusters in Kubernetes / cloud for high RPS.",
      "keywords": ["Distributed load testing", "distributed k6", "JMeter Master-Slave", "Kubernetes load generator", "high RPS generation"]
    },
    {
      "id": "advanced_accessibility_screen_readers",
      "name": "Screen Reader & Assistive Tech Auditing",
      "description": "Manual assistive technology verification (NVDA, VoiceOver, keyboard navigation traps).",
      "keywords": ["NVDA", "VoiceOver", "keyboard navigation", "focus trap", "screen reader testing", "tabindex audit"]
    },
    {
      "id": "performance_bottleneck_rca",
      "name": "Performance Root Cause Analysis (RCA)",
      "description": "Conducting Root Cause Analysis (RCA) on performance test failures (identifying thread locks, slow DB queries, memory leaks).",
      "keywords": ["Performance RCA", "Root Cause Analysis", "thread lock", "slow query analysis", "GC pauses in load", "latency breakdown"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "JMeter test plans (.jmx) or k6 performance test scripts",
        "detection": "file_presence",
        "pattern": "*\\.jmx|k6/|*\\.k6\\.js|load-test.*\\.js",
        "strength": 0.9,
        "maps_to": ["qa_non_functional_testing.jmeter_load_testing", "qa_non_functional_testing.k6_performance_as_code", "qa_non_functional_testing.performance_test_types_scenarios"]
      },
      {
        "signal": "axe-core or accessibility test assertions in Playwright/Cypress",
        "detection": "content_analysis",
        "pattern": "@axe-core/playwright|cypress-axe|axe\\.run|checkA11y",
        "strength": 0.8,
        "maps_to": ["qa_non_functional_testing.accessibility_testing_axe_wave", "qa_non_functional_testing.advanced_accessibility_screen_readers"]
      },
      {
        "signal": "Security test checks for OWASP or distributed load configs",
        "detection": "content_analysis",
        "pattern": "owasp|security_check|distributed-k6|jmeter-master|thresholds:.*p\\(95\\)",
        "strength": 0.8,
        "maps_to": ["qa_non_functional_testing.app_security_verification_owasp", "qa_non_functional_testing.distributed_load_generation", "qa_non_functional_testing.server_resource_monitoring_during_load", "qa_non_functional_testing.performance_bottleneck_rca"]
      }
    ],
    "cv": [
      {
        "signal": "Performance testing with JMeter or k6, or accessibility testing with axe/WCAG",
        "strength": 0.8,
        "maps_to": ["qa_non_functional_testing.jmeter_load_testing", "qa_non_functional_testing.accessibility_testing_axe_wave", "qa_non_functional_testing.k6_performance_as_code", "qa_non_functional_testing.performance_test_types_scenarios"]
      },
      {
        "signal": "Distributed load testing, performance RCA, or OWASP security testing in QA",
        "strength": 0.8,
        "maps_to": ["qa_non_functional_testing.server_resource_monitoring_during_load", "qa_non_functional_testing.app_security_verification_owasp", "qa_non_functional_testing.distributed_load_generation", "qa_non_functional_testing.advanced_accessibility_screen_readers", "qa_non_functional_testing.performance_bottleneck_rca"]
      }
    ],
    "linkedin": [
      {
        "signal": "JMeter, k6, or Performance Testing endorsed",
        "strength": 0.5,
        "maps_to": ["qa_non_functional_testing.jmeter_load_testing", "qa_non_functional_testing.k6_performance_as_code", "qa_non_functional_testing.performance_test_types_scenarios"]
      },
      {
        "signal": "Accessibility Testing, WCAG, or OWASP Testing mentioned",
        "strength": 0.5,
        "maps_to": ["qa_non_functional_testing.accessibility_testing_axe_wave", "qa_non_functional_testing.app_security_verification_owasp", "qa_non_functional_testing.distributed_load_generation", "qa_non_functional_testing.server_resource_monitoring_during_load", "qa_non_functional_testing.advanced_accessibility_screen_readers", "qa_non_functional_testing.performance_bottleneck_rca"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["jmeter_load_testing", "accessibility_testing_axe_wave"],
      "description": "Executes basic JMeter load scripts and runs automated accessibility audits using axe-core and WAVE."
    },
    "mid": {
      "expected_subskills": ["k6_performance_as_code", "performance_test_types_scenarios", "server_resource_monitoring_during_load", "app_security_verification_owasp"],
      "description": "Writes k6 load testing scripts, profiles stress/soak scenarios while monitoring server metrics, and verifies OWASP Top 10 defenses."
    },
    "senior": {
      "expected_subskills": ["distributed_load_generation", "advanced_accessibility_screen_readers", "performance_bottleneck_rca"],
      "description": "Orchestrates distributed high-RPS load testing in Kubernetes, conducts deep performance RCA on bottlenecks, and audits screen reader accessibility."
    }
  }
}

# 7. qa_test_management_reporting
skills["qa_test_management_reporting"] = {
  "skill_id": "qa_test_management_reporting",
  "name": "Test Management, CI/CD Integration & Quality Governance",
  "category": "test_management",
  "description": "Test case management systems (TestRail, Zephyr), rich execution reporting (Allure), CI/CD pipeline test integration, flaky test governance, and quality metrics tracking.",
  "subskills": [
    {
      "id": "testrail_zephyr_management",
      "name": "Test Case Management (TestRail/Zephyr)",
      "description": "Creating test runs, mapping test cases to user stories, marking execution results, and tracking test coverage.",
      "keywords": ["TestRail", "Zephyr", "qTest", "test run", "test suite mapping", "traceability matrix", "test execution tracking"]
    },
    {
      "id": "jira_bug_tracking_workflow",
      "name": "Defect Tracking & JIRA Workflow",
      "description": "Managing bug lifecycles in JIRA, linking defects to requirements, tracking bug triaging.",
      "keywords": ["JIRA", "bug tracking", "issue linking", "defect triaging", "JIRA workflow", "resolution status"]
    },
    {
      "id": "allure_reporting_rich_artifacts",
      "name": "Allure & Rich Test Reporting",
      "description": "Generating Allure / JUnit test reports with embedded screenshots, trace recordings, and video attachments.",
      "keywords": ["Allure report", "allure-results", "JUnit XML", "test report artifacts", "embedded screenshot", "trace attachment"]
    },
    {
      "id": "ci_cd_test_pipeline_integration",
      "name": "CI/CD Test Pipeline Integration",
      "description": "Integrating Cypress/Playwright/Postman test suites into GitHub Actions / GitLab CI with exit code gating.",
      "keywords": ["CI/CD test integration", "GitHub Actions test job", "GitLab CI test stage", "test exit code gating", "test pipeline trigger"]
    },
    {
      "id": "test_environment_data_management",
      "name": "Test Environments & Test Data Management",
      "description": "Managing test environments (Staging/QA), seeding test databases, and sanitizing test fixtures.",
      "keywords": ["Test environment management", "test data seeding", "environment provisioning", "synthetic test data", "staging environment"]
    },
    {
      "id": "flaky_test_quarantine_governance",
      "name": "Flaky Test Quarantine & Stabilization",
      "description": "Identifying flaky tests, implementing quarantine/retrying policies, and tracking test stability metrics.",
      "keywords": ["Flaky test quarantine", "flakiness rate", "test retries", "flaky test governance", "test suite stabilization"]
    },
    {
      "id": "quality_dashboards_kpi_tracking",
      "name": "Quality Dashboards & KPI Telemetry",
      "description": "Building QA telemetry dashboards (pass rate, MTTR, defect escape rate, automation ROI).",
      "keywords": ["Quality dashboard", "QA KPIs", "pass rate metric", "defect escape rate", "automation ROI", "test execution trends"]
    },
    {
      "id": "test_strategy_architecture_qa",
      "name": "Enterprise Test Strategy & Pyramid",
      "description": "Architecting organization-wide test strategies, test pyramid balance, and quality engineering standards.",
      "keywords": ["Test pyramid", "enterprise test strategy", "unit vs integration vs e2e ratio", "quality engineering standards", "shift-left strategy"]
    },
    {
      "id": "production_quality_monitoring_sentry",
      "name": "Production Quality Feedback Loops",
      "description": "Monitoring production error rates via Sentry/Datadog to feed back into regression test suites.",
      "keywords": ["Production feedback loop", "Sentry error rate", "Datadog synthetic monitoring", "production incident analysis", "escaped defect root cause"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Allure report configuration or JUnit XML test artifact upload in CI",
        "detection": "content_analysis",
        "pattern": "allure-results|allure-commandline|junit-report|upload-artifact.*allure",
        "strength": 0.8,
        "maps_to": ["qa_test_management_reporting.allure_reporting_rich_artifacts"]
      },
      {
        "signal": "GitHub Actions or GitLab CI workflow running automated test suites",
        "detection": "content_analysis",
        "pattern": "run: npx playwright test|run: npx cypress run|newman run|npm test",
        "strength": 0.8,
        "maps_to": ["qa_test_management_reporting.ci_cd_test_pipeline_integration", "qa_test_management_reporting.test_environment_data_management"]
      },
      {
        "signal": "TestRail API integration scripts, flaky quarantine configs, or quality dashboard metrics",
        "detection": "content_analysis",
        "pattern": "testrail-api|testrail\\.py|quarantine|retries:\\s*[1-9]|sentry.*monitoring",
        "strength": 0.8,
        "maps_to": ["qa_test_management_reporting.testrail_zephyr_management", "qa_test_management_reporting.jira_bug_tracking_workflow", "qa_test_management_reporting.flaky_test_quarantine_governance", "qa_test_management_reporting.quality_dashboards_kpi_tracking", "qa_test_management_reporting.test_strategy_architecture_qa", "qa_test_management_reporting.production_quality_monitoring_sentry"]
      }
    ],
    "cv": [
      {
        "signal": "Test management with TestRail/Zephyr, JIRA defect management, or Allure reporting",
        "strength": 0.8,
        "maps_to": ["qa_test_management_reporting.testrail_zephyr_management", "qa_test_management_reporting.jira_bug_tracking_workflow", "qa_test_management_reporting.allure_reporting_rich_artifacts"]
      },
      {
        "signal": "CI/CD test pipeline integration, test strategy design, or quality KPI tracking",
        "strength": 0.8,
        "maps_to": ["qa_test_management_reporting.ci_cd_test_pipeline_integration", "qa_test_management_reporting.test_environment_data_management", "qa_test_management_reporting.flaky_test_quarantine_governance", "qa_test_management_reporting.quality_dashboards_kpi_tracking", "qa_test_management_reporting.test_strategy_architecture_qa", "qa_test_management_reporting.production_quality_monitoring_sentry"]
      }
    ],
    "linkedin": [
      {
        "signal": "TestRail, JIRA, or Test Management endorsed",
        "strength": 0.5,
        "maps_to": ["qa_test_management_reporting.testrail_zephyr_management", "qa_test_management_reporting.jira_bug_tracking_workflow", "qa_test_management_reporting.allure_reporting_rich_artifacts"]
      },
      {
        "signal": "CI/CD Testing, Test Strategy, or Quality Assurance Leadership mentioned",
        "strength": 0.5,
        "maps_to": ["qa_test_management_reporting.ci_cd_test_pipeline_integration", "qa_test_management_reporting.test_environment_data_management", "qa_test_management_reporting.flaky_test_quarantine_governance", "qa_test_management_reporting.quality_dashboards_kpi_tracking", "qa_test_management_reporting.test_strategy_architecture_qa", "qa_test_management_reporting.production_quality_monitoring_sentry"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["testrail_zephyr_management", "jira_bug_tracking_workflow", "allure_reporting_rich_artifacts"],
      "description": "Manages test runs in TestRail/Zephyr, tracks defects in JIRA, and generates rich Allure test reports."
    },
    "mid": {
      "expected_subskills": ["ci_cd_test_pipeline_integration", "test_environment_data_management", "flaky_test_quarantine_governance"],
      "description": "Integrates test suites into CI/CD pipelines, provisions test data and environments, and quarantines flaky tests."
    },
    "senior": {
      "expected_subskills": ["quality_dashboards_kpi_tracking", "test_strategy_architecture_qa", "production_quality_monitoring_sentry"],
      "description": "Architects enterprise test strategies (Test Pyramid), builds QA KPI dashboards, and integrates production monitoring into test cycles."
    }
  }
}

# Write all skill files
for skill_id, skill_data in skills.items():
    file_path = os.path.join(skills_dir, f"{skill_id}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(skill_data, f, indent=2, ensure_ascii=False)
    print(f"Skill written: {skill_id}.json ({len(skill_data['subskills'])} subskills)")

print("\nAll 7 skill files created successfully.")
