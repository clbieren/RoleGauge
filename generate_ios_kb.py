import os
import json

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'knowledge-base'))

# Ensure directories
os.makedirs(os.path.join(base_dir, 'skills', 'ios'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'roles', 'ios'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'evidence', 'ios'), exist_ok=True)

CRITICAL_NOTE = "Mobil networking ve credential saklama (Retrofit/URLSession, Keychain/DataStore) istemci tarafında API tüketimi ve güvenli yerel depolamadır; Backend'in be_api_design/be_auth_security'si sunucu tarafında API sunma ve credential doğrulamadır — farklı taraflar, farklı sorumluluklar."

# -------------------------------------------------------------
# 1. iOS Skills Definition
# -------------------------------------------------------------
ios_skills = [
    {
        "skill_id": "ios_fundamentals_swift",
        "name": "Swift Language & Memory Model Fundamentals",
        "category": "mobile_core",
        "description": "Core Swift programming language mastery and Apple runtime memory architecture. Encompasses idiomatic Swift syntax (Optionals, pattern matching, closures), Value vs Reference type semantics (Copy-on-Write / COW), Protocol-Oriented Programming (POP), Generics type constraints, Automatic Reference Counting (ARC retain cycle prevention), Error handling / Result enum, Swift Macros / Metaprogramming, memory layout optimization, and C/Objective-C bridging interoperability.",
        "subskills": [
            {
                "id": "swift_language_fundamentals",
                "name": "Swift Idioms, Optionals & Pattern Matching",
                "description": "Mastering idiomatic Swift syntax — Optionals (optional binding if let / guard let, nil-coalescing ??, optional chaining ?., force unwrapping risks), pattern matching with switch expressions, control flow, functions with argument labels, and closure capture semantics.",
                "keywords": ["Swift Optionals", "guard let / if let", "nil-coalescing operator", "pattern matching switch", "closures", "argument labels", "trailing closure syntax"]
            },
            {
                "id": "value_vs_reference_types",
                "name": "Value vs Reference Types & Copy-on-Write (COW)",
                "description": "Distinguishing value types (Structs, Enums with associated values, Tuples) from reference types (Classes, Functions), understanding Stack vs Heap allocation, implementing custom Copy-on-Write (COW) data structures using isKnownUniquelyReferenced, and mutation semantics.",
                "keywords": ["Struct vs Class", "Value vs Reference types", "Copy-on-Write (COW)", "isKnownUniquelyReferenced", "Stack vs Heap allocation", "Enum with associated values", "mutating keyword"]
            },
            {
                "id": "protocols_extensions_basics",
                "name": "Protocol-Oriented Programming (POP) & Extensions",
                "description": "Designing applications using Protocol-Oriented Programming principles — Protocol composition, default implementations via Protocol Extensions, Delegation pattern, protocol inheritance, and static vs dynamic dispatch in protocols.",
                "keywords": ["Protocol-Oriented Programming (POP)", "Protocol Extensions", "default protocol implementation", "Delegation pattern", "protocol composition", "static vs dynamic dispatch"]
            },
            {
                "id": "generics_type_constraints",
                "name": "Swift Generics, Associated Types & Opaque Types",
                "description": "Building reusable generic algorithms and abstractions — Generic functions/types, associated types (associatedtype in protocols), where clauses for type constraints, Primary Associated Types (some vs any), and opaque return types (some View).",
                "keywords": ["Swift Generics", "associatedtype", "where clause constraints", "opaque return types (`some`)", "existential types (`any`)", "primary associated types (Swift 5.7+)", "generic specialization"]
            },
            {
                "id": "arc_memory_management",
                "name": "Automatic Reference Counting (ARC) & Retain Cycles",
                "description": "Managing memory lifecycle in iOS — Automatic Reference Counting (ARC), resolving strong reference cycles using weak and unowned references, closure capture lists ([weak self, unowned delegate]), delegate memory rules, and analyzing deallocations in deinit.",
                "keywords": ["Automatic Reference Counting (ARC)", "retain cycles", "weak vs unowned references", "closure capture lists (`[weak self]`)", "deinit lifecycle", "strong reference cycles"]
            },
            {
                "id": "error_handling_result",
                "name": "Swift Error Handling & Result Type",
                "description": "Designing robust error recovery mechanisms — Error protocol conformance, throwing functions (throws/rethrows), try / try? / try!, Result<Success, Failure> enum transformations (map, flatMap, get), and custom domain error hierarchies.",
                "keywords": ["Swift Error protocol", "throws / rethrows", "try? / try!", "Result<Success, Failure>", "custom Error enum", "typed throws (Swift 6)", "do-catch error recovery"]
            },
            {
                "id": "advanced_swift_metaprogramming",
                "name": "Swift Macros, Property Wrappers & Result Builders",
                "description": "Metaprogramming in modern Swift — authoring custom Swift Macros (Freestanding and Attached macros via SwiftSyntax), implementing custom Property Wrappers (@propertyWrapper with projectedValue $), and creating Result Builders (@resultBuilder) for declarative DSLs.",
                "keywords": ["Swift Macros (SwiftSyntax)", "@attached / @freestanding macros", "Property Wrappers (@propertyWrapper)", "projectedValue ($)", "Result Builders (@resultBuilder)", "KeyPaths (\.property)", "Mirror reflection"]
            },
            {
                "id": "memory_layout_performance",
                "name": "Swift Memory Layout & Performance Optimization",
                "description": "Analyzing runtime memory layout of Swift types (MemoryLayout<T>.size, stride, alignment), understanding existential container overhead (3-word inline buffer + witness tables), optimizing table/message dispatch, and reducing dynamic heap allocations.",
                "keywords": ["MemoryLayout (size, stride, alignment)", "Existential Containers", "Protocol Witness Table (PWT)", "Value Witness Table (VWT)", "dynamic vs vtable dispatch", "WMO (Whole Module Optimization)"]
            },
            {
                "id": "c_obj_c_interoperability",
                "name": "Objective-C & C Interoperability & Bridging",
                "description": "Bridging Swift with Objective-C and C — @objc attributes, @objcMembers, bridging headers (Project-Bridging-Header.h), nullability annotations (__nonnull/__nullable), NS_SWIFT_NAME, C pointers (UnsafePointer, UnsafeMutableRawPointer), and C function pointers.",
                "keywords": ["Objective-C bridging header", "@objc / @objcMembers", "NS_SWIFT_NAME", "nullability macros", "UnsafePointer / UnsafeMutablePointer", "C function pointers", "dynamic runtime messaging"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Swift source files utilizing protocols, generics, and property wrappers",
                    "detection": "content_analysis",
                    "pattern": "protocol .* :|struct .*<.*>|@propertyWrapper|associatedtype|guard let .* else \\{",
                    "strength": 0.8,
                    "maps_to": ["ios_fundamentals_swift.swift_language_fundamentals", "ios_fundamentals_swift.protocols_extensions_basics", "ios_fundamentals_swift.generics_type_constraints"]
                },
                {
                    "signal": "Closure capture list [weak self] usage for ARC retain cycle prevention",
                    "detection": "content_analysis",
                    "pattern": "\\[weak self\\]|\\[unowned self\\]|guard let self else \\{ return \\}",
                    "strength": 0.8,
                    "maps_to": ["ios_fundamentals_swift.arc_memory_management"]
                },
                {
                    "signal": "Swift Macro implementation using SwiftSyntax",
                    "detection": "content_analysis",
                    "pattern": "import SwiftSyntax|CompilerPlugin|public struct .*: (ExpressionMacro|AttachedMacro)",
                    "strength": 0.9,
                    "maps_to": ["ios_fundamentals_swift.advanced_swift_metaprogramming"]
                },
                {
                    "signal": "Objective-C bridging header or unsafe pointer memory manipulation",
                    "detection": "file_presence",
                    "pattern": ".*-Bridging-Header\\.h|UnsafeMutablePointer|withUnsafeBytes",
                    "strength": 0.8,
                    "maps_to": ["ios_fundamentals_swift.c_obj_c_interoperability", "ios_fundamentals_swift.memory_layout_performance"]
                }
            ],
            "cv": [
                {
                    "signal": "Developed iOS apps using modern Swift, Protocol-Oriented Programming, and ARC",
                    "strength": 0.8,
                    "maps_to": ["ios_fundamentals_swift.swift_language_fundamentals", "ios_fundamentals_swift.protocols_extensions_basics", "ios_fundamentals_swift.arc_memory_management"]
                },
                {
                    "signal": "Built custom Swift Macros or Property Wrappers for declarative architecture",
                    "strength": 0.9,
                    "maps_to": ["ios_fundamentals_swift.advanced_swift_metaprogramming", "ios_fundamentals_swift.generics_type_constraints"]
                },
                {
                    "signal": "Optimized Swift runtime memory layout and eliminated existential container overhead",
                    "strength": 0.9,
                    "maps_to": ["ios_fundamentals_swift.memory_layout_performance", "ios_fundamentals_swift.value_vs_reference_types"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Swift (Programming Language), iOS Development, or Protocol-Oriented Programming endorsed",
                    "strength": 0.5,
                    "maps_to": ["ios_fundamentals_swift.swift_language_fundamentals", "ios_fundamentals_swift.protocols_extensions_basics"]
                },
                {
                    "signal": "Job experience describing Swift macro development, ARC memory optimization, or Obj-C bridging",
                    "strength": 0.8,
                    "maps_to": ["ios_fundamentals_swift.advanced_swift_metaprogramming", "ios_fundamentals_swift.arc_memory_management", "ios_fundamentals_swift.c_obj_c_interoperability"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["swift_language_fundamentals", "value_vs_reference_types", "protocols_extensions_basics"],
                "description": "Writes idiomatic Swift with optionals and pattern matching, understands struct vs class value semantics, and applies protocol extensions."
            },
            "mid": {
                "expected_subskills": ["generics_type_constraints", "arc_memory_management", "error_handling_result"],
                "description": "Implements generic abstractions with associated types, prevents ARC retain cycles with capture lists, and handles errors with Result types."
            },
            "senior": {
                "expected_subskills": ["advanced_swift_metaprogramming", "memory_layout_performance", "c_obj_c_interoperability"],
                "description": "Authors custom Swift Macros and property wrappers, analyzes low-level Swift memory layout, and bridges with Objective-C/C runtimes."
            }
        }
    },
    {
        "skill_id": "ios_app_lifecycle_xcode",
        "name": "iOS App Lifecycle, Xcode Tooling & System Integration",
        "category": "mobile_core",
        "description": "Managing the iOS application lifecycle across UIKit and SwiftUI app structures (AppDelegate, SceneDelegate, WindowGroup), Xcode IDE debugging (LLDB, view hierarchy, os_log), Asset catalogs, Background Tasks (BGTaskScheduler), WidgetKit extensions, Universal Links (AASA), Instruments profiling (Time Profiler, Leaks), multi-scheme build setups, and App Store privacy compliance (Privacy Manifests).",
        "subskills": [
            {
                "id": "app_delegate_scene_delegate",
                "name": "App & Scene Lifecycle Management",
                "description": "Managing iOS application lifecycle states (Active, Inactive, Background, Suspended, Not Running) across UIApplicationDelegate, UIWindowSceneDelegate, and SwiftUI App protocol (@main App, WindowGroup, scenePhase), and handling state preservation/restoration.",
                "keywords": ["UIApplicationDelegate", "UIWindowSceneDelegate", "SwiftUI @main App", "scenePhase environment", "app execution states", "state restoration", "didFinishLaunchingWithOptions"]
            },
            {
                "id": "xcode_ide_debugging_tools",
                "name": "Xcode IDE & Advanced LLDB Debugging",
                "description": "Leveraging Xcode debugging features — LLDB commands (po, p, expression, frame variable, thread backtrace), symbolic/exception breakpoints, Debug View Hierarchy inspector, Memory Graph Debugger, and structured logging with Unified Logging system (os_log / Logger).",
                "keywords": ["LLDB debugging (po/p/expr)", "Debug View Hierarchy", "Memory Graph Debugger", "symbolic breakpoints", "Unified Logging (os_log / Logger)", "Xcode console debugging"]
            },
            {
                "id": "asset_catalogs_localization",
                "name": "Asset Catalogs & String Catalogs Localization",
                "description": "Managing visual assets and internationalization — Asset Catalogs (.xcassets for color sets, images, app icons, vector PDFs, dark/light mode variants), SF Symbols, String Catalogs (.xcstrings in Xcode 15+), pluralization rules, and RTL (Right-to-Left) layout mirroring.",
                "keywords": ["Asset Catalogs (.xcassets)", "Color Sets & Light/Dark variants", "SF Symbols", "String Catalogs (.xcstrings)", "Localizable.strings", "internationalization (i18n)", "RTL localization"]
            },
            {
                "id": "background_modes_tasks",
                "name": "Background Modes & BGTaskScheduler",
                "description": "Executing background tasks within Apple power constraints — configuring UIBackgroundModes (remote notifications, audio, location), registering and submitting background processing with BGTaskScheduler (BGAppRefreshTask, BGProcessingTask), and silent push triggers.",
                "keywords": ["BGTaskScheduler", "BGAppRefreshTask", "BGProcessingTask", "UIBackgroundModes", "silent push notifications", "background execution limits", "power management iOS"]
            },
            {
                "id": "app_extensions_widgets",
                "name": "App Extensions, WidgetKit & App Groups",
                "description": "Developing iOS extensions — building Home Screen & Lock Screen widgets with WidgetKit (TimelineProvider, TimelineEntry, TimelineReloadPolicy), App Groups for shared container data access (UserDefaults suite / shared SQLite), and Notification Service Extensions.",
                "keywords": ["WidgetKit", "TimelineProvider / TimelineEntry", "App Groups (shared container)", "Lock Screen widgets", "Notification Service Extension", "Share Extension", "extension lifecycle"]
            },
            {
                "id": "universal_links_deep_linking",
                "name": "Universal Links & Deep Link Routing",
                "description": "Architecting deep linking on iOS — configuring Apple App Site Association (apple-app-site-association / AASA on HTTPS server), associated domains entitlement (applinks:), Custom URL Schemes, handling userActivity in scene delegates, and building hierarchical deep link routers.",
                "keywords": ["Universal Links", "apple-app-site-association (AASA)", "associated domains (applinks:)", "Custom URL Scheme", "NSUserActivity handling", "deep link router architecture"]
            },
            {
                "id": "instruments_profiling_performance",
                "name": "Xcode Instruments & Deep Profiling",
                "description": "Conducting deep application profiling using Xcode Instruments — Time Profiler (CPU call trees, heavy stack traces), Allocations & Leaks (heap growth, unreleased memory), Core Animation instrument (frame drop detection, offscreen rendering), and Energy Log.",
                "keywords": ["Xcode Instruments", "Time Profiler (Call Tree, Invert Call Tree)", "Allocations & Leaks instruments", "Core Animation (offscreen rendering, color blended layers)", "Energy Log", "Memory footprint analysis"]
            },
            {
                "id": "multi_target_build_schemes",
                "name": "Xcode Schemes, Configurations & xcconfig Files",
                "description": "Architecting enterprise multi-target Xcode projects — Xcode Schemes, Build Configurations (Debug, Staging, Release), decoupling build settings into external .xcconfig files, custom Build Phase scripts (SwiftLint, Run scripts), and bundle identifier overrides.",
                "keywords": ["Xcode Schemes", "Build Configurations", ".xcconfig files", "Build Phases (Run Script)", "multi-target project setup", "bundle identifier per environment", "preprocess macros"]
            },
            {
                "id": "app_store_guidelines_privacy",
                "name": "App Store Guidelines & Privacy Manifests",
                "description": "Complying with Apple ecosystem policies — App Store Review Guidelines, App Tracking Transparency (ATT framework / ATTrackingManager), Privacy Nutrition Labels, authoring Privacy Manifests (PrivacyInfo.xcprivacy with Required Reason APIs), and third-party SDK signature verification.",
                "keywords": ["Privacy Manifests (PrivacyInfo.xcprivacy)", "Required Reason APIs", "App Tracking Transparency (ATT)", "App Store Review Guidelines", "Privacy Nutrition Labels", "SDK code signing"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Xcode project or workspace configuration files",
                    "detection": "file_presence",
                    "pattern": "\\.xcodeproj/project\\.pbxproj|\\.xcworkspace|\\.xcconfig$",
                    "strength": 0.8,
                    "maps_to": ["ios_app_lifecycle_xcode.multi_target_build_schemes", "ios_app_lifecycle_xcode.app_delegate_scene_delegate"]
                },
                {
                    "signal": "WidgetKit TimelineProvider implementation or App Extension target",
                    "detection": "content_analysis",
                    "pattern": ": TimelineProvider|struct .*: Widget|TimelineEntry|WidgetBundle",
                    "strength": 0.9,
                    "maps_to": ["ios_app_lifecycle_xcode.app_extensions_widgets"]
                },
                {
                    "signal": "BGTaskScheduler background task registration and handling",
                    "detection": "content_analysis",
                    "pattern": "BGTaskScheduler\\.shared\\.register|BGAppRefreshTaskRequest|BGProcessingTaskRequest",
                    "strength": 0.9,
                    "maps_to": ["ios_app_lifecycle_xcode.background_modes_tasks"]
                },
                {
                    "signal": "Privacy Manifest PrivacyInfo.xcprivacy configuration file",
                    "detection": "file_presence",
                    "pattern": "PrivacyInfo\\.xcprivacy|NSPrivacyAccessedAPITypes",
                    "strength": 0.9,
                    "maps_to": ["ios_app_lifecycle_xcode.app_store_guidelines_privacy"]
                },
                {
                    "signal": "Asset Catalog or String Catalog localization files",
                    "detection": "file_presence",
                    "pattern": "\\.xcassets|\\.xcstrings$|Localizable\\.strings",
                    "strength": 0.8,
                    "maps_to": ["ios_app_lifecycle_xcode.asset_catalogs_localization"]
                }
            ],
            "cv": [
                {
                    "signal": "Configured iOS background tasks with BGTaskScheduler and built WidgetKit extensions",
                    "strength": 0.8,
                    "maps_to": ["ios_app_lifecycle_xcode.background_modes_tasks", "ios_app_lifecycle_xcode.app_extensions_widgets"]
                },
                {
                    "signal": "Profiled iOS app performance and eliminated memory leaks using Xcode Instruments",
                    "strength": 0.9,
                    "maps_to": ["ios_app_lifecycle_xcode.instruments_profiling_performance"]
                },
                {
                    "signal": "Implemented Universal Links (AASA) and Privacy Manifests (PrivacyInfo.xcprivacy)",
                    "strength": 0.9,
                    "maps_to": ["ios_app_lifecycle_xcode.universal_links_deep_linking", "ios_app_lifecycle_xcode.app_store_guidelines_privacy"]
                }
            ],
            "linkedin": [
                {
                    "signal": "iOS App Lifecycle, Xcode, or WidgetKit endorsed",
                    "strength": 0.5,
                    "maps_to": ["ios_app_lifecycle_xcode.app_delegate_scene_delegate", "ios_app_lifecycle_xcode.app_extensions_widgets"]
                },
                {
                    "signal": "Job experience describing Universal Links, Xcode Instruments profiling, or Privacy Manifest compliance",
                    "strength": 0.8,
                    "maps_to": ["ios_app_lifecycle_xcode.instruments_profiling_performance", "ios_app_lifecycle_xcode.universal_links_deep_linking", "ios_app_lifecycle_xcode.app_store_guidelines_privacy"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["app_delegate_scene_delegate", "xcode_ide_debugging_tools", "asset_catalogs_localization"],
                "description": "Manages AppDelegate and SceneDelegate lifecycles, debugs using LLDB and View Hierarchy, and organizes assets and String Catalogs."
            },
            "mid": {
                "expected_subskills": ["background_modes_tasks", "app_extensions_widgets", "universal_links_deep_linking"],
                "description": "Schedules background tasks with BGTaskScheduler, develops WidgetKit extensions with App Groups, and implements Universal Links."
            },
            "senior": {
                "expected_subskills": ["instruments_profiling_performance", "multi_target_build_schemes", "app_store_guidelines_privacy"],
                "description": "Profiles apps with Xcode Instruments, architects multi-scheme xcconfig setups, and enforces Privacy Manifests."
            }
        }
    },
    {
        "skill_id": "ios_uikit_swiftui",
        "name": "iOS UI Development: UIKit & SwiftUI Architecture",
        "category": "mobile_core",
        "description": "Modern and traditional iOS UI engineering spanning declarative SwiftUI, programmatic UIKit AutoLayout, Diffable Data Sources, SwiftUI state management (@State, @Binding, Observable macro), UIKit/SwiftUI interoperability (UIHostingController, UIViewRepresentable), Core Animation, Core Graphics custom drawing, and VoiceOver Dynamic Type accessibility.",
        "subskills": [
            {
                "id": "uikit_autolayout_programmatic",
                "name": "Programmatic AutoLayout & UIStackView",
                "description": "Constructing robust UIKit interfaces purely in code — NSLayoutConstraint, NSLayoutAnchor API, UIStackView composition, constraint priorities (UILayoutPriority), content hugging & compression resistance, and avoiding AutoLayout unsatisfiable constraints.",
                "keywords": ["Programmatic AutoLayout", "NSLayoutAnchor", "UIStackView", "translatesAutoresizingMaskIntoConstraints", "contentHuggingPriority", "contentCompressionResistancePriority", "SnapKit"]
            },
            {
                "id": "uikit_collection_table_views",
                "name": "Diffable Data Sources & Compositional Layouts",
                "description": "Building high-performance UIKit lists and grids — UITableView, UICollectionView, UITableViewDiffableDataSource / UICollectionViewDiffableDataSource with NSDiffableDataSourceSnapshot, and UICollectionViewCompositionalLayout for complex multi-axis scrolling layouts.",
                "keywords": ["UICollectionViewDiffableDataSource", "NSDiffableDataSourceSnapshot", "UICollectionViewCompositionalLayout", "NSCollectionLayoutSection", "UICollectionViewCell recycling", "custom cell configurations"]
            },
            {
                "id": "swiftui_views_state_basics",
                "name": "SwiftUI Declarative Views & State Hoisting",
                "description": "Building declarative user interfaces with SwiftUI — View protocol conformance, view hierarchy composition (VStack, HStack, ZStack, List, LazyVStack), managing local state with @State and @Binding, and state hoisting for reusable component design.",
                "keywords": ["SwiftUI View protocol", "@State / @Binding", "VStack / HStack / ZStack", "LazyVStack / LazyHStack", "State hoisting", "declarative view body", "view modifiers"]
            },
            {
                "id": "swiftui_state_management",
                "name": "SwiftUI Observable Macro & State Management",
                "description": "Managing complex state graphs across SwiftUI applications — utilizing the modern iOS 17+ @Observable macro (Observation framework), comparing with legacy @StateObject, @ObservedObject, @EnvironmentObject, @Published (ObservableObject), and scoping @Environment properties.",
                "keywords": ["@Observable macro (iOS 17+)", "Observation framework", "@StateObject vs @ObservedObject", "@EnvironmentObject", "@Published property wrapper", "@Environment custom values"]
            },
            {
                "id": "uikit_swiftui_interoperability",
                "name": "UIKit & SwiftUI Interoperability Bridging",
                "description": "Bridging between UIKit and SwiftUI frameworks — embedding SwiftUI views in UIKit with UIHostingController, wrapping UIKit views and controllers for SwiftUI using UIViewRepresentable and UIViewControllerRepresentable with custom Coordinators.",
                "keywords": ["UIHostingController", "UIViewRepresentable", "UIViewControllerRepresentable", "Coordinator pattern bridging", "makeUIView / updateUIView", "interoperability architecture"]
            },
            {
                "id": "swiftui_navigation_custom_layouts",
                "name": "NavigationStack & Custom Layout Protocol",
                "description": "Implementing type-safe navigation and custom layouts in SwiftUI — NavigationStack with navigationDestination(for:), NavigationSplitView for iPad/Mac multi-column layouts, GeometryReader for responsive measurements, and the Layout protocol (sizeThatFits, placeSubviews).",
                "keywords": ["NavigationStack", "navigationDestination(for:)", "NavigationSplitView", "GeometryReader", "SwiftUI Layout protocol (sizeThatFits/placeSubviews)", "type-safe navigation path"]
            },
            {
                "id": "custom_animations_transitions",
                "name": "Core Animation & SwiftUI Transitions",
                "description": "Designing fluid animations and transitions — Core Animation layer animations (CABasicAnimation, CAKeyframeAnimation, CATransition), UIViewPropertyAnimator for interactive scrubbable gestures, and SwiftUI matchedGeometryEffect with custom transition modifiers.",
                "keywords": ["Core Animation (CABasicAnimation)", "UIViewPropertyAnimator (interactive scrub)", "SwiftUI matchedGeometryEffect", "withAnimation spring curves", "custom AnyTransition", "CALayer animation"]
            },
            {
                "id": "custom_drawing_core_graphics",
                "name": "Core Graphics & Custom Layer Drawing",
                "description": "Performing custom 2D rendering — Core Graphics (CGContext, CGPath, UIBezierPath in draw(_:)), custom CALayer subclasses (CAShapeLayer, CAGradientLayer, CATextLayer), and SwiftUI Canvas / ShaderLibrary (Metal shader functions in iOS 17).",
                "keywords": ["Core Graphics (CGContext / CGPath)", "UIBezierPath", "CAShapeLayer / CAGradientLayer", "draw(_ rect: CGRect)", "SwiftUI Canvas", "Metal shaders in SwiftUI (colorEffect)"]
            },
            {
                "id": "accessibility_dynamic_type",
                "name": "VoiceOver Accessibility & Dynamic Type",
                "description": "Engineering accessible iOS applications — VoiceOver accessibility elements (accessibilityLabel, accessibilityValue, accessibilityTraits, accessibilityCustomActions), supporting Dynamic Type font scaling without UI clipping, and WCAG color contrast compliance.",
                "keywords": ["VoiceOver accessibility", "accessibilityLabel / accessibilityHint", "accessibilityTraits", "Dynamic Type font scaling", "UIFontMetrics", "WCAG color contrast", "accessibilityCustomActions"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "SwiftUI view declarations with state wrappers or Observable macro",
                    "detection": "content_analysis",
                    "pattern": "struct .*: View|@State private var|@Observable class|UIHostingController|NavigationStack",
                    "strength": 0.8,
                    "maps_to": ["ios_uikit_swiftui.swiftui_views_state_basics", "ios_uikit_swiftui.swiftui_state_management", "ios_uikit_swiftui.swiftui_navigation_custom_layouts"]
                },
                {
                    "signal": "Programmatic AutoLayout or UICollectionViewCompositionalLayout code",
                    "detection": "content_analysis",
                    "pattern": "NSLayoutConstraint\\.activate|UICollectionViewDiffableDataSource|UICollectionViewCompositionalLayout",
                    "strength": 0.8,
                    "maps_to": ["ios_uikit_swiftui.uikit_autolayout_programmatic", "ios_uikit_swiftui.uikit_collection_table_views"]
                },
                {
                    "signal": "UIViewRepresentable or UIViewControllerRepresentable bridging implementation",
                    "detection": "content_analysis",
                    "pattern": ": UIViewRepresentable|: UIViewControllerRepresentable|func makeUIView|func updateUIView",
                    "strength": 0.9,
                    "maps_to": ["ios_uikit_swiftui.uikit_swiftui_interoperability"]
                },
                {
                    "signal": "Core Animation UIViewPropertyAnimator or matchedGeometryEffect",
                    "detection": "content_analysis",
                    "pattern": "UIViewPropertyAnimator|matchedGeometryEffect|CABasicAnimation|CAShapeLayer",
                    "strength": 0.8,
                    "maps_to": ["ios_uikit_swiftui.custom_animations_transitions", "ios_uikit_swiftui.custom_drawing_core_graphics"]
                },
                {
                    "signal": "VoiceOver accessibility modifiers and Dynamic Type scaling",
                    "detection": "content_analysis",
                    "pattern": "\\.accessibilityLabel|\\.accessibilityHint|UIFontMetrics|accessibilityTraits",
                    "strength": 0.8,
                    "maps_to": ["ios_uikit_swiftui.accessibility_dynamic_type"]
                }
            ],
            "cv": [
                {
                    "signal": "Built modern iOS UIs with SwiftUI, Observable macro, and UIKit interoperability",
                    "strength": 0.8,
                    "maps_to": ["ios_uikit_swiftui.swiftui_views_state_basics", "ios_uikit_swiftui.swiftui_state_management", "ios_uikit_swiftui.uikit_swiftui_interoperability"]
                },
                {
                    "signal": "Engineered complex layouts using Compositional Layout and Diffable Data Sources",
                    "strength": 0.8,
                    "maps_to": ["ios_uikit_swiftui.uikit_collection_table_views", "ios_uikit_swiftui.uikit_autolayout_programmatic"]
                },
                {
                    "signal": "Designed fluid Core Animation transitions and enforced VoiceOver accessibility",
                    "strength": 0.9,
                    "maps_to": ["ios_uikit_swiftui.custom_animations_transitions", "ios_uikit_swiftui.accessibility_dynamic_type"]
                }
            ],
            "linkedin": [
                {
                    "signal": "SwiftUI, UIKit, or AutoLayout endorsed",
                    "strength": 0.5,
                    "maps_to": ["ios_uikit_swiftui.swiftui_views_state_basics", "ios_uikit_swiftui.uikit_autolayout_programmatic"]
                },
                {
                    "signal": "Job experience describing SwiftUI architecture, UIKit bridging, or interactive animations",
                    "strength": 0.8,
                    "maps_to": ["ios_uikit_swiftui.uikit_swiftui_interoperability", "ios_uikit_swiftui.custom_animations_transitions", "ios_uikit_swiftui.swiftui_navigation_custom_layouts"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["uikit_autolayout_programmatic", "uikit_collection_table_views", "swiftui_views_state_basics"],
                "description": "Constructs programmatic AutoLayout interfaces, implements Diffable Data Sources in collection views, and builds basic SwiftUI views."
            },
            "mid": {
                "expected_subskills": ["swiftui_state_management", "uikit_swiftui_interoperability", "swiftui_navigation_custom_layouts"],
                "description": "Manages complex state with the Observable macro, bridges UIKit and SwiftUI with representables, and implements NavigationStack."
            },
            "senior": {
                "expected_subskills": ["custom_animations_transitions", "custom_drawing_core_graphics", "accessibility_dynamic_type"],
                "description": "Authors Core Animation/UIViewPropertyAnimator transitions, renders custom Core Graphics layers, and enforces VoiceOver standards."
            }
        }
    },
    {
        "skill_id": "ios_architecture_patterns",
        "name": "iOS Architecture, Modularization & State Machines",
        "category": "mobile_core",
        "description": "Architectural design patterns and enterprise modularization for iOS applications. Covers MVC, MVVM (with Combine/Async), Coordinator pattern for decoupled navigation, Repository pattern, Clean Architecture (VIPER), The Composable Architecture (TCA), Swift Package Manager (SPM) multi-module modularization, Micro-apps architectures, and Finite State Machines (FSM).",
        "subskills": [
            {
                "id": "mvc_mvvm_architecture",
                "name": "MVC & MVVM Architecture with Data Binding",
                "description": "Implementing Model-View-ViewModel (MVVM) architecture on iOS, resolving 'Massive View Controller' (MVC) anti-patterns, binding View to ViewModel using Combine publishers, async properties, or closure observers, and modeling immutable UI states.",
                "keywords": ["MVVM architecture iOS", "Massive View Controller refactoring", "ViewModel data binding", "Combine in MVVM", "UI State modeling", "separation of concerns"]
            },
            {
                "id": "dependency_injection_coordinator",
                "name": "Coordinator Pattern & Dependency Injection",
                "description": "Decoupling navigation from ViewControllers using the Coordinator pattern — implementing Coordinator protocols with start(), managing navigation flows independently of UI hierarchy, and applying Constructor Dependency Injection with DI Containers.",
                "keywords": ["Coordinator pattern", "navigation decoupling", "start() protocol", "Dependency Injection Container", "Constructor Injection", "navigation separation"]
            },
            {
                "id": "repository_pattern_services",
                "name": "Repository Pattern & API Service Abstraction",
                "description": "Designing the Repository pattern to coordinate local persistence (CoreData/SwiftData) and remote networking (URLSession/Alamofire), protocol abstraction for API services, and providing mock data providers for SwiftUI previews and unit testing.",
                "keywords": ["Repository pattern iOS", "API Service protocol", "mock data providers", "SwiftUI Previews data mocking", "Single Source of Truth", "Data layer abstraction"]
            },
            {
                "id": "clean_architecture_viper",
                "name": "Clean Architecture & VIPER Pattern",
                "description": "Implementing Clean Architecture / VIPER (View, Interactor, Presenter, Entity, Router) pattern — defining strict unidirectional boundaries between presentation, domain use cases (Interactors), data models, and routing logic.",
                "keywords": ["VIPER architecture", "View-Interactor-Presenter-Entity-Router", "Clean Architecture iOS", "Interactor domain logic", "Presenter view formatting", "Router navigation"]
            },
            {
                "id": "tca_composable_architecture",
                "name": "The Composable Architecture (TCA)",
                "description": "Architecting applications using Point-Free's The Composable Architecture (TCA) — modeling State, Action enum, Reducer functions, Store/ViewStore, managing side-effects with Effect, and composing scoped child domains into parent domains.",
                "keywords": ["The Composable Architecture (TCA)", "State / Action / Reducer", "Store / ViewStore", "Effect side-effects", "Domain composition", "Point-Free TCA"]
            },
            {
                "id": "advanced_coordinators_deeplinking",
                "name": "Hierarchical Coordinators & Deep Link Trees",
                "description": "Managing complex multi-flow navigation with hierarchical Coordinators — parent-child Coordinator memory retention (childCoordinators array), clean child lifecycle dismissal, and resolving deep link URLs by traversing the Coordinator tree.",
                "keywords": ["Hierarchical Coordinators", "parent-child coordinator lifecycle", "childCoordinators retain prevention", "deep link coordinator traversal", "navigation flow composition"]
            },
            {
                "id": "modularization_spm_frameworks",
                "name": "Swift Package Manager (SPM) Modularization",
                "description": "Architecting large iOS codebases into isolated Swift Packages using SPM (Package.swift) — structuring feature packages, core packages (Networking, DesignSystem, Storage), separating interfaces from implementations to eliminate cyclic dependencies and accelerate Xcode incremental builds.",
                "keywords": ["Swift Package Manager (SPM)", "Package.swift modularization", "interface vs implementation targets", "cyclic dependency elimination", "Xcode build parallelization", "Framework modularity"]
            },
            {
                "id": "microapps_plugin_architecture",
                "name": "Micro-Apps Architecture & Dynamic Frameworks",
                "description": "Building Micro-Apps architectures where independent feature teams develop standalone executable targets (Sample Apps) for isolated feature development, dynamic framework loading, module registries, and plugin interfaces.",
                "keywords": ["Micro-Apps architecture", "standalone demo apps", "module registry pattern", "dynamic frameworks vs static libraries", "isolated feature development", "plugin architecture"]
            },
            {
                "id": "state_machine_unidirectional_flow",
                "name": "Finite State Machines & Unidirectional Data Flow",
                "description": "Designing deterministic state transitions using Finite State Machines (FSM) in Swift — modeling states and events as enums with associated values, pure state reducer functions, and ensuring predictable state restoration without invalid transition states.",
                "keywords": ["Finite State Machine (FSM)", "Unidirectional Data Flow (UDF)", "pure state reducers", "deterministic state transitions", "invalid state prevention", "state restoration"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Swift Package Manager multi-target manifest or modular frameworks",
                    "detection": "file_presence",
                    "pattern": "Package\\.swift|\\.package\\(path:|\"Feature.*\", targets: \\[\"",
                    "strength": 0.9,
                    "maps_to": ["ios_architecture_patterns.modularization_spm_frameworks", "ios_architecture_patterns.microapps_plugin_architecture"]
                },
                {
                    "signal": "Coordinator pattern implementation or navigation protocol",
                    "detection": "content_analysis",
                    "pattern": "protocol .*Coordinator: AnyObject|childCoordinators|func start\\(\\)|navigationController: UINavigationController",
                    "strength": 0.8,
                    "maps_to": ["ios_architecture_patterns.dependency_injection_coordinator", "ios_architecture_patterns.advanced_coordinators_deeplinking"]
                },
                {
                    "signal": "The Composable Architecture (TCA) Reducer or Store implementation",
                    "detection": "content_analysis",
                    "pattern": "import ComposableArchitecture|@Reducer|struct .*: Reducer|StoreOf<|Effect<Action>",
                    "strength": 0.9,
                    "maps_to": ["ios_architecture_patterns.tca_composable_architecture"]
                },
                {
                    "signal": "VIPER architecture components (Interactor, Presenter, Router)",
                    "detection": "content_analysis",
                    "pattern": "protocol .*InteractorInput|protocol .*PresenterInput|protocol .*RouterInput",
                    "strength": 0.8,
                    "maps_to": ["ios_architecture_patterns.clean_architecture_viper"]
                }
            ],
            "cv": [
                {
                    "signal": "Architected iOS apps using MVVM, Coordinators, and Clean Architecture",
                    "strength": 0.8,
                    "maps_to": ["ios_architecture_patterns.mvc_mvvm_architecture", "ios_architecture_patterns.dependency_injection_coordinator", "ios_architecture_patterns.clean_architecture_viper"]
                },
                {
                    "signal": "Modularized monolithic iOS application into 25+ SPM Swift Packages",
                    "strength": 0.9,
                    "maps_to": ["ios_architecture_patterns.modularization_spm_frameworks", "ios_architecture_patterns.microapps_plugin_architecture"]
                },
                {
                    "signal": "Implemented unidirectional data flow using The Composable Architecture (TCA)",
                    "strength": 0.9,
                    "maps_to": ["ios_architecture_patterns.tca_composable_architecture", "ios_architecture_patterns.state_machine_unidirectional_flow"]
                }
            ],
            "linkedin": [
                {
                    "signal": "iOS Architecture, MVVM, or SPM Modularization endorsed",
                    "strength": 0.5,
                    "maps_to": ["ios_architecture_patterns.mvc_mvvm_architecture", "ios_architecture_patterns.modularization_spm_frameworks"]
                },
                {
                    "signal": "Job experience describing SPM modularization, TCA architecture, or Coordinator navigation trees",
                    "strength": 0.8,
                    "maps_to": ["ios_architecture_patterns.modularization_spm_frameworks", "ios_architecture_patterns.tca_composable_architecture", "ios_architecture_patterns.advanced_coordinators_deeplinking"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["mvc_mvvm_architecture", "dependency_injection_coordinator", "repository_pattern_services"],
                "description": "Applies MVVM architecture with data binding, decouples navigation with Coordinators, and abstracts APIs with Repositories."
            },
            "mid": {
                "expected_subskills": ["clean_architecture_viper", "tca_composable_architecture", "advanced_coordinators_deeplinking"],
                "description": "Implements Clean Architecture / VIPER layers, builds features with TCA, and manages hierarchical child Coordinators."
            },
            "senior": {
                "expected_subskills": ["modularization_spm_frameworks", "microapps_plugin_architecture", "state_machine_unidirectional_flow"],
                "description": "Architects SPM multi-package modularity, builds Micro-Apps with isolated demo targets, and designs state machines."
            }
        }
    },
    {
        "skill_id": "ios_reactive_concurrency",
        "name": "Swift Concurrency, Combine & Reactive Programming",
        "category": "mobile_core",
        "description": "Modern and traditional asynchronous programming on iOS. Covers Grand Central Dispatch (GCD), OperationQueue, Swift Modern Concurrency (async/await, Tasks, TaskGroups), Actors and @MainActor thread safety, AsyncSequence / AsyncStream, Combine framework (Publishers, Subscribers, Operators), Thread Sanitizer (TSan) race detection, and RxSwift migration.",
        "subskills": [
            {
                "id": "grand_central_dispatch_basics",
                "name": "Grand Central Dispatch (GCD) & Dispatch Queues",
                "description": "Managing concurrency using Grand Central Dispatch (GCD) — DispatchQueue (Main, Global QoS: userInteractive, userInitiated, utility, background, custom serial and concurrent queues), async vs sync execution, DispatchGroup, and DispatchWorkItem.",
                "keywords": ["Grand Central Dispatch (GCD)", "DispatchQueue.main / .global()", "Quality of Service (QoS)", "serial vs concurrent queues", "DispatchGroup", "async vs sync dispatch", "DispatchWorkItem"]
            },
            {
                "id": "operations_operation_queue",
                "name": "Operation & OperationQueue Architecture",
                "description": "Managing complex, cancellable, dependent background jobs with Operation and OperationQueue — BlockOperation, custom Operation subclasses (isExecuting, isFinished, isCancelled KVO states), setting dependencies (addDependency), and maxConcurrentOperationCount.",
                "keywords": ["Operation & OperationQueue", "BlockOperation", "custom Operation subclass", "KVO states (isExecuting/isFinished)", "addDependency", "maxConcurrentOperationCount", "cancellation handling"]
            },
            {
                "id": "async_await_structured_concurrency",
                "name": "Swift Modern Concurrency: async/await & Tasks",
                "description": "Writing asynchronous code with modern Swift concurrency — async/await, Task, Task.sleep, Task.detached, structured concurrency with async let and withTaskGroup, cooperative cancellation checking (Task.isCancelled, try Task.checkCancellation()).",
                "keywords": ["async / await", "Swift Structured Concurrency", "Task / Task.detached", "async let bindings", "withTaskGroup / withThrowingTaskGroup", "cooperative cancellation (Task.isCancelled)"]
            },
            {
                "id": "actors_thread_safety",
                "name": "Actors, @MainActor & Data Race Elimination",
                "description": "Eliminating data races at compile time with Swift Actors — actor declaration, actor isolation rules, nonisolated keyword, cross-actor message passing, @MainActor for UI thread confinement, and Global Actors.",
                "keywords": ["Swift Actors", "actor isolation", "@MainActor", "nonisolated keyword", "Global Actors", "data race elimination", "reentrancy in actors"]
            },
            {
                "id": "async_sequences_streams",
                "name": "AsyncSequence, AsyncStream & Bridging Delegates",
                "description": "Consuming asynchronous streams of values using AsyncSequence protocol — for await in loops, creating custom AsyncStream and AsyncThrowingStream (continuation yield, onTermination), and bridging legacy callback/delegate APIs into async streams.",
                "keywords": ["AsyncSequence protocol", "AsyncStream / AsyncThrowingStream", "for await ... in loop", "continuation.yield()", "continuation.finish()", "bridging delegate callbacks to async"]
            },
            {
                "id": "combine_publishers_subscribers",
                "name": "Combine Framework: Publishers & Subscribers",
                "description": "Reactive programming with Apple's Combine framework — AnyPublisher, PassthroughSubject, CurrentValueSubject, subscriber subscriptions (.sink, .assign(to:on:)), managing AnyCancellable memory lifecycle with Set<AnyCancellable> (store(in:)).",
                "keywords": ["Combine framework", "AnyPublisher / Subject", "PassthroughSubject / CurrentValueSubject", "sink / assign(to:)", "AnyCancellable", "store(in: &cancellables)", "Publisher-Subscriber lifecycle"]
            },
            {
                "id": "combine_advanced_operators",
                "name": "Advanced Combine Operators & Stream Composition",
                "description": "Composing complex asynchronous pipelines using Combine operators: flatMap, combineLatest, zip, merge, debounce, throttle, removeDuplicates, error recovery with catch and retry, and switching execution with receive(on:) and subscribe(on:).",
                "keywords": ["Combine flatMap", "combineLatest / zip", "debounce / throttle", "removeDuplicates", "receive(on: DispatchQueue.main)", "subscribe(on:)", "catch / retry error handling"]
            },
            {
                "id": "concurrency_data_races_tsan",
                "name": "Thread Sanitizer (TSan) & Lock Synchronization",
                "description": "Detecting and resolving multithreaded data races in production iOS applications — utilizing Xcode Thread Sanitizer (TSan), implementing high-performance low-level locks with os_unfair_lock, and ensuring thread-safe shared mutable state.",
                "keywords": ["Thread Sanitizer (TSan)", "data race detection", "os_unfair_lock", "unfair lock synchronization", "thread safety validation", "preventing priority inversion"]
            },
            {
                "id": "rxswift_reactive_patterns",
                "name": "RxSwift / RxCocoa & Modern Concurrency Migration",
                "description": "Working with RxSwift and RxCocoa in enterprise applications — Observable, Single, Completable, DisposeBag, Schedulers, Traits (Driver, Signal), and executing structured migration plans from RxSwift to native Combine and async/await.",
                "keywords": ["RxSwift / RxCocoa", "Observable / Single / Completable", "DisposeBag lifecycle", "Schedulers (MainScheduler)", "Driver / Signal traits", "RxSwift to Combine migration", "RxSwift to Async/Await"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Swift Modern Concurrency async/await or actor declarations",
                    "detection": "content_analysis",
                    "pattern": "async throws ->|actor .* \\{|@MainActor|withTaskGroup|for await .* in",
                    "strength": 0.8,
                    "maps_to": ["ios_reactive_concurrency.async_await_structured_concurrency", "ios_reactive_concurrency.actors_thread_safety", "ios_reactive_concurrency.async_sequences_streams"]
                },
                {
                    "signal": "Combine framework publisher pipeline or subjects",
                    "detection": "content_analysis",
                    "pattern": "import Combine|AnyPublisher<|PassthroughSubject<|\\.sink \\{|\\.store\\(in: &cancellables\\)",
                    "strength": 0.8,
                    "maps_to": ["ios_reactive_concurrency.combine_publishers_subscribers", "ios_reactive_concurrency.combine_advanced_operators"]
                },
                {
                    "signal": "RxSwift Observable or DisposeBag usage",
                    "detection": "content_analysis",
                    "pattern": "import RxSwift|import RxCocoa|DisposeBag\\(\\)|Observable<|Single<",
                    "strength": 0.8,
                    "maps_to": ["ios_reactive_concurrency.rxswift_reactive_patterns"]
                },
                {
                    "signal": "Grand Central Dispatch or OperationQueue concurrency implementation",
                    "detection": "content_analysis",
                    "pattern": "DispatchQueue\\.global|DispatchGroup\\(\\)|OperationQueue\\(\\)|os_unfair_lock",
                    "strength": 0.8,
                    "maps_to": ["ios_reactive_concurrency.grand_central_dispatch_basics", "ios_reactive_concurrency.operations_operation_queue", "ios_reactive_concurrency.concurrency_data_races_tsan"]
                }
            ],
            "cv": [
                {
                    "signal": "Implemented reactive data streams using Combine, Swift Concurrency, and async/await",
                    "strength": 0.8,
                    "maps_to": ["ios_reactive_concurrency.async_await_structured_concurrency", "ios_reactive_concurrency.combine_publishers_subscribers", "ios_reactive_concurrency.actors_thread_safety"]
                },
                {
                    "signal": "Migrated legacy RxSwift codebase to native Swift Modern Concurrency and Combine",
                    "strength": 0.9,
                    "maps_to": ["ios_reactive_concurrency.rxswift_reactive_patterns", "ios_reactive_concurrency.async_sequences_streams"]
                },
                {
                    "signal": "Eliminated multi-threaded data races using Thread Sanitizer and Actor isolation",
                    "strength": 0.9,
                    "maps_to": ["ios_reactive_concurrency.actors_thread_safety", "ios_reactive_concurrency.concurrency_data_races_tsan"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Swift Concurrency, Combine, or Grand Central Dispatch endorsed",
                    "strength": 0.5,
                    "maps_to": ["ios_reactive_concurrency.async_await_structured_concurrency", "ios_reactive_concurrency.combine_publishers_subscribers"]
                },
                {
                    "signal": "Job experience describing async/await migration, actor thread safety, or Combine pipelines",
                    "strength": 0.8,
                    "maps_to": ["ios_reactive_concurrency.actors_thread_safety", "ios_reactive_concurrency.combine_advanced_operators", "ios_reactive_concurrency.async_await_structured_concurrency"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["grand_central_dispatch_basics", "operations_operation_queue", "async_await_structured_concurrency"],
                "description": "Dispatches background tasks with GCD, configures Operation dependencies, and writes async/await functions."
            },
            "mid": {
                "expected_subskills": ["actors_thread_safety", "async_sequences_streams", "combine_publishers_subscribers"],
                "description": "Enforces thread safety with Actors and @MainActor, bridges delegates with AsyncStream, and builds Combine pipelines."
            },
            "senior": {
                "expected_subskills": ["combine_advanced_operators", "concurrency_data_races_tsan", "rxswift_reactive_patterns"],
                "description": "Composes advanced Combine streams, debugs data races with Thread Sanitizer, and leads RxSwift migrations."
            }
        }
    },
    {
        "skill_id": "ios_data_persistence_networking",
        "name": "iOS Data Persistence, Offline Sync & Secure Networking",
        "category": "mobile_core",
        "description": f"Client-side data persistence, offline synchronization, and secure RESTful networking in iOS applications. IMPORTANT DISTINCTION: {CRITICAL_NOTE} Covers UserDefaults, FileManager sandbox, Keychain Services, Core Data (stack, contexts, migrations, NSFetchedResultsController), SwiftData (@Model, @Query), URLSession / Alamofire networking, offline sync engines, and SSL Certificate Pinning.",
        "subskills": [
            {
                "id": "userdefaults_filemanager",
                "name": "UserDefaults & Sandbox FileManager",
                "description": "Managing simple local data and file storage — UserDefaults (reading/writing primitive values, custom Codable encoding, @AppStorage property wrapper), and FileManager sandbox navigation (Documents, Caches, Application Support, Temporary directories) with atomic file writes.",
                "keywords": ["UserDefaults", "@AppStorage", "FileManager", "App Sandbox directories (Documents/Caches)", "atomic file writing", "Data.write(to:options: .atomic)"]
            },
            {
                "id": "urlsession_codable_networking",
                "name": "URLSession & Codable Network Consumption",
                "description": "Consuming REST APIs using Apple native URLSession — URLRequest, URLSessionConfiguration (default, ephemeral, background), Decodable/Encodable (Codable) JSON parsing with JSONDecoder (dateDecodingStrategy, keyDecodingStrategy), and HTTP status code handling.",
                "keywords": ["URLSession dataTask", "URLRequest", "Codable (Decodable / Encodable)", "JSONDecoder / JSONEncoder", "keyDecodingStrategy (.convertFromSnakeCase)", "HTTPURLResponse status validation"]
            },
            {
                "id": "keychain_secure_storage",
                "name": "Keychain Services & Secure Token Storage",
                "description": "Securing sensitive user credentials and cryptographic keys using iOS Keychain Services API — SecItemAdd, SecItemCopyMatching, SecItemUpdate, SecItemDelete, configuring accessibility flags (kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly), and Keychain wrapper architectures.",
                "keywords": ["Keychain Services API", "SecItemAdd / SecItemCopyMatching", "kSecAttrAccessible flags", "secure token storage", "Hardware Secure Enclave", "Keychain wrapper class"]
            },
            {
                "id": "core_data_fundamentals",
                "name": "Core Data Stack & NSFetchedResultsController",
                "description": "Managing relational persistence with Core Data — NSPersistentContainer, NSManagedObjectModel (.xcdatamodeld), NSManagedObject, NSManagedObjectContext CRUD operations, NSPredicate / NSSortDescriptor queries, and NSFetchedResultsController for automatic UI list updates.",
                "keywords": ["Core Data", "NSPersistentContainer", "NSManagedObjectContext", "NSFetchRequest", "NSPredicate", "NSSortDescriptor", "NSFetchedResultsController", "Core Data CRUD"]
            },
            {
                "id": "swiftdata_modern_persistence",
                "name": "SwiftData Modern Declarative Persistence",
                "description": "Implementing modern Apple persistence using SwiftData (iOS 17+) — @Model macro for schema definition, ModelContainer, ModelContext (insert, delete, save), @Query macro in SwiftUI with Predicate and FetchDescriptor, relationships (@Relationship), and SwiftData migrations.",
                "keywords": ["SwiftData (iOS 17+)", "@Model macro", "ModelContainer / ModelContext", "@Query in SwiftUI", "#Predicate / FetchDescriptor", "@Relationship (cascade/nullify)", "SchemaMigrationPlan"]
            },
            {
                "id": "alamofire_networking_layer",
                "name": "Alamofire Client & Interceptors Architecture",
                "description": "Building networking layers with Alamofire — Session configuration, RequestAdapter (injecting auth tokens), RequestRetrier (retry policies with backoff), EventMonitor for logging, multipart form-data upload, and response validation.",
                "keywords": ["Alamofire Session", "RequestAdapter", "RequestRetrier (RetryResult)", "RequestInterceptor", "multipart upload", "responseDecodable", "AF.request"]
            },
            {
                "id": "core_data_multithreading_migrations",
                "name": "Core Data Multithreading & Schema Migrations",
                "description": "Architecting high-scale Core Data systems — background context concurrency with performBackgroundTask / context.perform, parent-child context hierarchies, merge policies (NSMergeByPropertyObjectTrumpMergePolicy), lightweight vs heavyweight migrations (mapping models / NSEntityMigrationPolicy).",
                "keywords": ["Core Data background context", "performBackgroundTask", "context.perform concurrency", "NSMergePolicy", "Lightweight migrations", "Heavyweight schema migration (Mapping Model)", "NSEntityMigrationPolicy"]
            },
            {
                "id": "offline_caching_sync_engine",
                "name": "Offline Caching & Data Sync Engine",
                "description": "Architecting offline-first iOS applications — local database (CoreData/SwiftData) as Single Source of Truth, optimistic UI state updates, offline mutation queue persistence, background sync with server, and conflict resolution strategies (timestamp / vector clocks).",
                "keywords": ["Offline-first architecture iOS", "offline sync engine", "optimistic UI updates", "mutation queue", "conflict resolution", "local database Single Source of Truth", "sync state tracking"]
            },
            {
                "id": "network_security_ssl_pinning",
                "name": "SSL Pinning, ATS & Network Security",
                "description": "Hardening iOS network security — implementing SSL / Certificate Pinning via URLSessionDelegate (serverTrust authentication challenges) and Alamofire ServerTrustManager, verifying SHA-256 public key hashes, configuring App Transport Security (ATS) exceptions, and TLS 1.3 verification.",
                "keywords": ["SSL / Certificate Pinning", "URLSessionDelegate (didReceive challenge)", "ServerTrustManager Alamofire", "Public Key Pinning (SHA-256 hash)", "App Transport Security (ATS)", "MitM attack prevention"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Core Data stack or SwiftData model implementation",
                    "detection": "content_analysis",
                    "pattern": "NSPersistentContainer|@Model class|ModelContainer|NSFetchRequest|@Query var",
                    "strength": 0.8,
                    "maps_to": ["ios_data_persistence_networking.core_data_fundamentals", "ios_data_persistence_networking.swiftdata_modern_persistence", "ios_data_persistence_networking.core_data_multithreading_migrations"]
                },
                {
                    "signal": "URLSession Codable networking or Alamofire request handling",
                    "detection": "content_analysis",
                    "pattern": "URLSession\\.shared|JSONDecoder\\(\\)|AF\\.request|RequestInterceptor|URLRequest\\(",
                    "strength": 0.8,
                    "maps_to": ["ios_data_persistence_networking.urlsession_codable_networking", "ios_data_persistence_networking.alamofire_networking_layer"]
                },
                {
                    "signal": "Keychain Services API integration or wrapper",
                    "detection": "content_analysis",
                    "pattern": "SecItemAdd|SecItemCopyMatching|kSecClassGenericPassword|kSecAttrAccessible",
                    "strength": 0.9,
                    "maps_to": ["ios_data_persistence_networking.keychain_secure_storage"]
                },
                {
                    "signal": "SSL Certificate Pinning implementation in URLSession or Alamofire",
                    "detection": "content_analysis",
                    "pattern": "ServerTrustEvaluating|PinnedCertificatesTrustEvaluator|SecTrustEvaluateAsyncWithError|serverTrust",
                    "strength": 0.9,
                    "maps_to": ["ios_data_persistence_networking.network_security_ssl_pinning"]
                },
                {
                    "signal": "UserDefaults or FileManager sandbox operations",
                    "detection": "content_analysis",
                    "pattern": "UserDefaults\\.standard|@AppStorage|FileManager\\.default|urls\\(for: \\.documentDirectory",
                    "strength": 0.8,
                    "maps_to": ["ios_data_persistence_networking.userdefaults_filemanager"]
                }
            ],
            "cv": [
                {
                    "signal": "Architected offline-first iOS applications with Core Data / SwiftData and URLSession",
                    "strength": 0.8,
                    "maps_to": ["ios_data_persistence_networking.core_data_fundamentals", "ios_data_persistence_networking.offline_caching_sync_engine", "ios_data_persistence_networking.urlsession_codable_networking"]
                },
                {
                    "signal": "Implemented secure credential storage with Keychain and SSL Certificate Pinning",
                    "strength": 0.9,
                    "maps_to": ["ios_data_persistence_networking.keychain_secure_storage", "ios_data_persistence_networking.network_security_ssl_pinning"]
                },
                {
                    "signal": "Managed multi-threaded Core Data background contexts and complex schema migrations",
                    "strength": 0.9,
                    "maps_to": ["ios_data_persistence_networking.core_data_multithreading_migrations", "ios_data_persistence_networking.swiftdata_modern_persistence"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Core Data, SwiftData, or iOS Networking endorsed",
                    "strength": 0.5,
                    "maps_to": ["ios_data_persistence_networking.core_data_fundamentals", "ios_data_persistence_networking.urlsession_codable_networking"]
                },
                {
                    "signal": "Job experience describing offline sync engines, Core Data migrations, or Keychain security",
                    "strength": 0.8,
                    "maps_to": ["ios_data_persistence_networking.offline_caching_sync_engine", "ios_data_persistence_networking.core_data_multithreading_migrations", "ios_data_persistence_networking.keychain_secure_storage"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["userdefaults_filemanager", "urlsession_codable_networking", "keychain_secure_storage"],
                "description": "Stores user settings with UserDefaults/FileManager, consumes APIs with URLSession and Codable, and secures tokens with Keychain."
            },
            "mid": {
                "expected_subskills": ["core_data_fundamentals", "swiftdata_modern_persistence", "alamofire_networking_layer"],
                "description": "Models relational storage with Core Data and SwiftData, and builds networking pipelines with Alamofire interceptors."
            },
            "senior": {
                "expected_subskills": ["core_data_multithreading_migrations", "offline_caching_sync_engine", "network_security_ssl_pinning"],
                "description": "Architects background context Core Data migrations, engineers offline sync engines, and enforces SSL certificate pinning."
            }
        }
    },
    {
        "skill_id": "ios_platform_quality_distribution",
        "name": "iOS Platform Services, Quality, Fastlane & App Store Distribution",
        "category": "mobile_core",
        "description": "Automated testing (XCTest, XCUITest), Apple platform hardware services (UserNotifications, CoreLocation, LocalAuthentication Biometrics), Fastlane CI/CD automation, TestFlight beta distribution, MetricKit telemetry diagnostics, and App Thinning / binary size optimization.",
        "subskills": [
            {
                "id": "unit_testing_xctest",
                "name": "Unit Testing with XCTest & URLProtocol Mocking",
                "description": "Writing robust automated unit tests in Swift using XCTest — XCTestCase, XCTAssert assertions, testing asynchronous code with XCTestExpectation and async test methods, and mocking networking layers cleanly using custom URLProtocol subclasses.",
                "keywords": ["XCTest framework", "XCTestCase", "XCTAssertEqual / XCTAssertThrowsError", "XCTestExpectation", "URLProtocol mocking", "unit test coverage", "testing ViewModels"]
            },
            {
                "id": "user_notifications_push",
                "name": "UserNotifications Framework & Apple Push (APNs)",
                "description": "Implementing notification experiences using UserNotifications framework — UNUserNotificationCenter, requesting authorization, scheduling local notifications (UNTimeIntervalNotificationTrigger, UNCalendarNotificationTrigger), handling foreground notifications, and APNs device token registration.",
                "keywords": ["UserNotifications framework", "UNUserNotificationCenter", "UNNotificationContent", "UNNotificationAction / Category", "APNs device token registration", "remote push notifications"]
            },
            {
                "id": "app_lifecycle_permissions",
                "name": "iOS Permissions Model & Info.plist Privacy Keys",
                "description": "Managing iOS privacy permissions model — configuring Info.plist Usage Description strings (NSCameraUsageDescription, NSLocationWhenInUseUsageDescription, NSPhotoLibraryUsageDescription), checking authorization status, presenting contextual rationale UI, and handling denied states gracefully.",
                "keywords": ["Info.plist Usage Descriptions", "NSCameraUsageDescription", "NSLocationWhenInUseUsageDescription", "PHPhotoLibrary authorization", "permission request flow", "privacy compliance"]
            },
            {
                "id": "ui_testing_xcuicache",
                "name": "UI Testing with XCUITest & Page Object Pattern",
                "description": "Authoring automated end-to-end UI tests using XCUITest framework — XCUIApplication, XCUIElement query matching (buttons, textFields, staticTexts), handling asynchronous UI expectations (waitForExistence(timeout:)), and structuring tests with the Page Object Pattern.",
                "keywords": ["XCUITest framework", "XCUIApplication", "XCUIElement queries", "waitForExistence(timeout:)", "Page Object Pattern iOS", "UI test recording & assertions"]
            },
            {
                "id": "core_location_mapkit",
                "name": "CoreLocation, Geofencing & MapKit Services",
                "description": "Integrating location and mapping capabilities — CLLocationManager (requestWhenInUseAuthorization, requestAlwaysAuthorization, desiredAccuracy), tracking location updates, configuring CLCircularRegion geofences, significant location changes, and displaying annotations in MapKit / SwiftUI Map.",
                "keywords": ["CoreLocation framework", "CLLocationManager", "CLCircularRegion geofencing", "significant-change location service", "MapKit / SwiftUI Map", "MKAnnotation / MapMarker"]
            },
            {
                "id": "biometrics_local_authentication",
                "name": "LocalAuthentication & Face ID / Touch ID",
                "description": "Implementing biometric authentication using the LocalAuthentication framework — LAContext (canEvaluatePolicy, evaluatePolicy), LAPolicy.deviceOwnerAuthenticationWithBiometrics vs deviceOwnerAuthentication (passcode fallback), handling biometry lockouts, and error domain handling.",
                "keywords": ["LocalAuthentication framework", "LAContext", "Face ID / Touch ID", "LAPolicy.deviceOwnerAuthenticationWithBiometrics", "biometric passcode fallback", "LAError domain handling"]
            },
            {
                "id": "ci_cd_fastlane_testflight",
                "name": "Fastlane Automation, Code Signing & TestFlight",
                "description": "Automating iOS build and release pipelines — Fastlane (Fastfile lanes), Match for Git-based shared code signing certificates and provisioning profiles, Gym for ipa building, Scan for automated testing, Pilot for TestFlight distribution, and GitHub Actions / Xcode Cloud integration.",
                "keywords": ["Fastlane (Fastfile)", "Fastlane Match (code signing)", "Gym / build_app", "Scan / run_tests", "Pilot / upload_to_testflight", "Apple Developer Provisioning Profiles", "Xcode Cloud / CI/CD"]
            },
            {
                "id": "crash_diagnostics_metric_kit",
                "name": "MetricKit Diagnostics & Crash Symbolication",
                "description": "Monitoring production application telemetry — MetricKit framework (MXMetricManager, MXDiagnosticPayload, MXMetricPayload for hang rate, memory footprint, CPU energy), crash log symbolication using dSYM files and dwarfdump, and integrating Firebase Crashlytics with custom logs.",
                "keywords": ["MetricKit framework", "MXMetricManager", "MXDiagnosticPayload", "dSYM crash symbolication", "dwarfdump / atos", "Firebase Crashlytics iOS", "Hang Rate / Launch metric analysis"]
            },
            {
                "id": "app_thinning_size_optimization",
                "name": "App Thinning & Binary Size Optimization",
                "description": "Optimizing iOS application binary download size — App Thinning mechanisms (App Slicing for device-specific assets/binaries, On-Demand Resources / ODR), analyzing App Size Report, stripping debug symbols, dead code elimination, and asset compression.",
                "keywords": ["App Thinning", "App Slicing", "On-Demand Resources (ODR)", "App Size Report in Xcode", "binary size reduction", "dead code stripping", "asset catalog compression"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "XCTest unit test suite or URLProtocol mocking implementation",
                    "detection": "content_analysis",
                    "pattern": "import XCTest|class .*Tests: XCTestCase|XCTAssert|class .*URLProtocol: URLProtocol",
                    "strength": 0.8,
                    "maps_to": ["ios_platform_quality_distribution.unit_testing_xctest"]
                },
                {
                    "signal": "XCUITest automated UI test implementation",
                    "detection": "content_analysis",
                    "pattern": "class .*UITests: XCTestCase|XCUIApplication\\(\\)|\\.waitForExistence\\(timeout:",
                    "strength": 0.8,
                    "maps_to": ["ios_platform_quality_distribution.ui_testing_xcuicache"]
                },
                {
                    "signal": "Fastlane Fastfile or Matchfile configuration",
                    "detection": "file_presence",
                    "pattern": "fastlane/Fastfile|fastlane/Matchfile|Fastfile|Matchfile",
                    "strength": 0.9,
                    "maps_to": ["ios_platform_quality_distribution.ci_cd_fastlane_testflight"]
                },
                {
                    "signal": "CoreLocation or LocalAuthentication implementation",
                    "detection": "content_analysis",
                    "pattern": "CLLocationManager|LAContext\\(\\)|deviceOwnerAuthenticationWithBiometrics|UNUserNotificationCenter",
                    "strength": 0.8,
                    "maps_to": ["ios_platform_quality_distribution.core_location_mapkit", "ios_platform_quality_distribution.biometrics_local_authentication", "ios_platform_quality_distribution.user_notifications_push"]
                },
                {
                    "signal": "MetricKit subscriber or Crashlytics crash reporting integration",
                    "detection": "content_analysis",
                    "pattern": "MXMetricManager\\.shared|MXMetricManagerSubscriber|FirebaseCrashlytics|Crashlytics\\.crashlytics\\(\\)",
                    "strength": 0.8,
                    "maps_to": ["ios_platform_quality_distribution.crash_diagnostics_metric_kit"]
                }
            ],
            "cv": [
                {
                    "signal": "Automated iOS testing with XCTest, XCUITest, and URLProtocol network mocking",
                    "strength": 0.8,
                    "maps_to": ["ios_platform_quality_distribution.unit_testing_xctest", "ios_platform_quality_distribution.ui_testing_xcuicache"]
                },
                {
                    "signal": "Built automated Fastlane CI/CD pipelines and managed TestFlight distribution",
                    "strength": 0.9,
                    "maps_to": ["ios_platform_quality_distribution.ci_cd_fastlane_testflight", "ios_platform_quality_distribution.app_thinning_size_optimization"]
                },
                {
                    "signal": "Integrated Face ID biometrics, APNs push notifications, and MetricKit telemetry",
                    "strength": 0.8,
                    "maps_to": ["ios_platform_quality_distribution.biometrics_local_authentication", "ios_platform_quality_distribution.user_notifications_push", "ios_platform_quality_distribution.crash_diagnostics_metric_kit"]
                }
            ],
            "linkedin": [
                {
                    "signal": "XCTest, Fastlane, or iOS Testing endorsed",
                    "strength": 0.5,
                    "maps_to": ["ios_platform_quality_distribution.unit_testing_xctest", "ios_platform_quality_distribution.ci_cd_fastlane_testflight"]
                },
                {
                    "signal": "Job experience describing Fastlane code signing with Match, MetricKit diagnostics, or App Thinning",
                    "strength": 0.8,
                    "maps_to": ["ios_platform_quality_distribution.ci_cd_fastlane_testflight", "ios_platform_quality_distribution.crash_diagnostics_metric_kit", "ios_platform_quality_distribution.app_thinning_size_optimization"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["unit_testing_xctest", "user_notifications_push", "app_lifecycle_permissions"],
                "description": "Writes unit tests with XCTest and URLProtocol mocks, configures local push notifications, and handles permission requests."
            },
            "mid": {
                "expected_subskills": ["ui_testing_xcuicache", "core_location_mapkit", "biometrics_local_authentication"],
                "description": "Authors UI tests with XCUITest, integrates CoreLocation geofencing, and implements Face ID / Touch ID biometrics."
            },
            "senior": {
                "expected_subskills": ["ci_cd_fastlane_testflight", "crash_diagnostics_metric_kit", "app_thinning_size_optimization"],
                "description": "Automates Fastlane CI/CD with Match code signing, monitors MetricKit diagnostics, and optimizes binary size via App Thinning."
            }
        }
    }
]

# Write all 7 iOS skill files
for skill in ios_skills:
    file_path = os.path.join(base_dir, 'skills', 'ios', f"{skill['skill_id']}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(skill, f, indent=2, ensure_ascii=False)
    print(f"Written skill: {skill['skill_id']}.json")

# -------------------------------------------------------------
# 2. iOS Roles Definition
# -------------------------------------------------------------
roles = {
    "junior": {
        "role_id": "ios_developer",
        "level": "junior",
        "title": "Junior iOS Developer",
        "description": "Entry-level iOS developer focused on Swift language fundamentals (optionals, structs vs classes, protocols), AppDelegate/SceneDelegate lifecycles, UIKit AutoLayout and SwiftUI basics, MVVM architecture with Coordinator pattern, UserDefaults and URLSession networking, and unit testing with XCTest.",
        "experience_range": "0-2 years",
        "skills": [
            {
                "skill_id": "ios_fundamentals_swift",
                "importance": 0.95,
                "rationale": "Strong foundation in Swift optionals, value vs reference types, and protocol extensions is essential for daily iOS feature development."
            },
            {
                "skill_id": "ios_uikit_swiftui",
                "importance": 0.95,
                "rationale": "Constructing programmatic AutoLayout, implementing Diffable Data Sources in collection views, and building basic SwiftUI views."
            },
            {
                "skill_id": "ios_app_lifecycle_xcode",
                "importance": 0.9,
                "rationale": "Managing AppDelegate and SceneDelegate lifecycles, debugging with LLDB and View Hierarchy, and organizing Asset Catalogs."
            },
            {
                "skill_id": "ios_architecture_patterns",
                "importance": 0.85,
                "rationale": "Applying MVVM architecture with data binding, decoupling navigation with Coordinators, and abstracting APIs with Repositories."
            },
            {
                "skill_id": "ios_data_persistence_networking",
                "importance": 0.8,
                "rationale": "Storing user settings with UserDefaults/FileManager, consuming REST APIs with URLSession and Codable, and securing tokens in Keychain."
            },
            {
                "skill_id": "ios_reactive_concurrency",
                "importance": 0.8,
                "rationale": "Dispatching background tasks with GCD queues, configuring Operation dependencies, and writing async/await functions."
            },
            {
                "skill_id": "ios_platform_quality_distribution",
                "importance": 0.7,
                "rationale": "Writing automated unit tests with XCTest and URLProtocol mocks, configuring notifications, and handling Info.plist privacy permissions."
            }
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
            "thresholds": {
                "not_ready": {
                    "min": 0.0,
                    "max": 0.3,
                    "label": "Not Ready",
                    "description": "Significant gaps in Swift language fundamentals, iOS app lifecycles, or basic AutoLayout/SwiftUI."
                },
                "developing": {
                    "min": 0.3,
                    "max": 0.5,
                    "label": "Developing",
                    "description": "Basic understanding of UIKit and Swift, but requires guidance on SwiftUI state management, Coordinator navigation, and async/await."
                },
                "approaching": {
                    "min": 0.5,
                    "max": 0.7,
                    "label": "Approaching Ready",
                    "description": "Solid Swift fundamentals, reliable MVVM implementation, consistent XCTest habits, and clean SwiftUI code."
                },
                "ready": {
                    "min": 0.7,
                    "max": 0.85,
                    "label": "Ready",
                    "description": "Meets all junior expectations: delivers robust, tested iOS features with SwiftUI/UIKit, URLSession, and Coordinator patterns."
                },
                "exceeds": {
                    "min": 0.85,
                    "max": 1.0,
                    "label": "Exceeds Expectations",
                    "description": "Exceeds junior expectations with early mid-level proficiency in Combine pipelines, Core Data / SwiftData, and WidgetKit."
                }
            }
        }
    },
    "mid": {
        "role_id": "ios_developer",
        "level": "mid",
        "title": "Mid-level iOS Developer",
        "description": "Mid-level iOS engineer capable of independently architecting complex applications using Clean Architecture/VIPER or TCA, managing Core Data / SwiftData persistence, developing WidgetKit extensions with App Groups, enforcing thread safety with Actors and @MainActor, optimizing UIKit/SwiftUI interoperability, and building automated XCUITest suites.",
        "experience_range": "2-5 years",
        "skills": [
            {
                "skill_id": "ios_architecture_patterns",
                "importance": 0.95,
                "rationale": "Structuring applications with Clean Architecture/VIPER or TCA, and managing complex hierarchical child Coordinator trees."
            },
            {
                "skill_id": "ios_data_persistence_networking",
                "importance": 0.95,
                "rationale": "Modeling relational storage with Core Data and SwiftData, building networking layers with Alamofire interceptors, and Keychain security."
            },
            {
                "skill_id": "ios_reactive_concurrency",
                "importance": 0.9,
                "rationale": "Enforcing thread safety with Actors and @MainActor, bridging delegates with AsyncStream, and building reactive Combine pipelines."
            },
            {
                "skill_id": "ios_uikit_swiftui",
                "importance": 0.9,
                "rationale": "Managing complex state with the Observable macro, bridging UIKit and SwiftUI with representables, and implementing NavigationStack."
            },
            {
                "skill_id": "ios_app_lifecycle_xcode",
                "importance": 0.85,
                "rationale": "Scheduling background tasks with BGTaskScheduler, developing WidgetKit extensions with App Groups, and configuring Universal Links."
            },
            {
                "skill_id": "ios_fundamentals_swift",
                "importance": 0.85,
                "rationale": "Implementing generic abstractions with associated types, preventing ARC retain cycles with capture lists, and custom Error hierarchies."
            },
            {
                "skill_id": "ios_platform_quality_distribution",
                "importance": 0.8,
                "rationale": "Writing automated UI tests with XCUITest, integrating CoreLocation geofencing, and implementing Face ID / Touch ID biometrics."
            }
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
            "thresholds": {
                "not_ready": {
                    "min": 0.0,
                    "max": 0.3,
                    "label": "Not Ready",
                    "description": "Significant gaps in iOS architecture, Core Data persistence, or modern Swift concurrency."
                },
                "developing": {
                    "min": 0.3,
                    "max": 0.5,
                    "label": "Developing",
                    "description": "Competent with basic MVVM, but struggles with Core Data background contexts, Actor isolation, or UIKit/SwiftUI bridging."
                },
                "approaching": {
                    "min": 0.5,
                    "max": 0.7,
                    "label": "Approaching Ready",
                    "description": "Strong systems grasp, independent feature delivery, solid Clean Architecture/TCA implementation, and proactive memory leak hunting."
                },
                "ready": {
                    "min": 0.7,
                    "max": 0.85,
                    "label": "Ready",
                    "description": "Meets all mid-level expectations: delivers robust Core Data/SwiftData apps, designs clean TCA/VIPER layers, and debugs complex concurrency."
                },
                "exceeds": {
                    "min": 0.85,
                    "max": 1.0,
                    "label": "Exceeds Expectations",
                    "description": "Exceeds mid-level expectations with advanced SPM modularization, Swift Macros, and performance profiling expertise."
                }
            }
        }
    },
    "senior": {
        "role_id": "ios_developer",
        "level": "senior",
        "title": "Senior iOS Developer",
        "description": "Senior iOS engineer and mobile platform architect responsible for Swift Package Manager (SPM) modularization, Micro-Apps architectures, custom Swift Macros, Core Data background migrations and offline sync engines, low-level Swift memory layout optimization, Xcode Instruments profiling (Time Profiler, Leaks), Fastlane CI/CD automation with Match code signing, MetricKit diagnostics, and Privacy Manifest compliance.",
        "experience_range": "5+ years",
        "skills": [
            {
                "skill_id": "ios_architecture_patterns",
                "importance": 0.95,
                "rationale": "Architecting SPM multi-package modularity, building Micro-Apps with isolated demo targets, and designing state machines."
            },
            {
                "skill_id": "ios_uikit_swiftui",
                "importance": 0.95,
                "rationale": "Authoring Core Animation/UIViewPropertyAnimator transitions, rendering custom Core Graphics layers, and enforcing VoiceOver accessibility."
            },
            {
                "skill_id": "ios_reactive_concurrency",
                "importance": 0.9,
                "rationale": "Composing advanced Combine streams, debugging data races with Thread Sanitizer, and leading RxSwift-to-Modern-Concurrency migrations."
            },
            {
                "skill_id": "ios_platform_quality_distribution",
                "importance": 0.9,
                "rationale": "Automating Fastlane CI/CD with Match code signing, monitoring MetricKit diagnostics, and optimizing binary size via App Thinning."
            },
            {
                "skill_id": "ios_data_persistence_networking",
                "importance": 0.85,
                "rationale": "Architecting background context Core Data migrations, engineering offline sync engines, and enforcing SSL certificate pinning."
            },
            {
                "skill_id": "ios_fundamentals_swift",
                "importance": 0.85,
                "rationale": "Authoring custom Swift Macros and property wrappers, analyzing low-level Swift memory layout, and bridging with Objective-C/C."
            },
            {
                "skill_id": "ios_app_lifecycle_xcode",
                "importance": 0.85,
                "rationale": "Profiling apps with Xcode Instruments, architecting multi-scheme xcconfig setups, and enforcing Privacy Manifests."
            }
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
            "thresholds": {
                "not_ready": {
                    "min": 0.0,
                    "max": 0.3,
                    "label": "Not Ready",
                    "description": "Significant gaps in SPM modularization, performance profiling, or iOS security architectures."
                },
                "developing": {
                    "min": 0.3,
                    "max": 0.5,
                    "label": "Developing",
                    "description": "Solid mid-level feature delivery, but lacks experience in modularization strategies, Instruments profiling, and CI/CD pipelines."
                },
                "approaching": {
                    "min": 0.5,
                    "max": 0.7,
                    "label": "Approaching Ready",
                    "description": "Strong architectural capabilities; refining expertise in Swift Macros, MetricKit telemetry, and advanced Fastlane Match signing."
                },
                "ready": {
                    "min": 0.7,
                    "max": 0.85,
                    "label": "Ready",
                    "description": "Meets all senior expectations: architects scalable SPM modular apps, mentors engineers, enforces performance standards, and automates CI/CD."
                },
                "exceeds": {
                    "min": 0.85,
                    "max": 1.0,
                    "label": "Exceeds Expectations",
                    "description": "Exceeds senior expectations: staff/principal mobile leadership driving cross-platform strategy and enterprise iOS infrastructure."
                }
            }
        }
    }
}

for level_name, role_data in roles.items():
    file_path = os.path.join(base_dir, 'roles', 'ios', f"{level_name}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(role_data, f, indent=2, ensure_ascii=False)
    print(f"Written role: roles/ios/{level_name}.json")

# -------------------------------------------------------------
# 3. iOS Evidence (github, cv, linkedin)
# -------------------------------------------------------------

# github.json
github_evidence = {
    "source_id": "github",
    "name": "GitHub Repository Analysis - iOS Developer",
    "description": "Global parsing rules for iOS repositories across Swift and Objective-C codebases. NOTE: Specific evidence mappings (regex patterns and maps_to composite keys) are stored within individual skill files under evidence.github, NOT here. The validate_composite_keys.py script scans both locations to verify coverage.",
    "preprocessing_pipeline": {
        "steps": [
            {
                "step": 1,
                "name": "file_tree_scan",
                "target_files": [
                    {
                        "pattern": "Podfile|Podfile\\.lock|Package\\.swift|Cartfile|Cartfile\\.lock",
                        "skills": ["ios_architecture_patterns", "ios_data_persistence_networking", "ios_reactive_concurrency"],
                        "priority": "high",
                        "notes": "Dependency management manifests (SPM Package.swift, CocoaPods Podfile, Carthage)"
                    },
                    {
                        "pattern": "\\.xcodeproj|\\.xcworkspace|\\.xcconfig$|Info\\.plist",
                        "skills": ["ios_app_lifecycle_xcode", "ios_platform_quality_distribution"],
                        "priority": "high",
                        "notes": "Xcode project configuration, build schemes, configurations, and privacy entitlements in Info.plist"
                    },
                    {
                        "pattern": "PrivacyInfo\\.xcprivacy",
                        "skills": ["ios_app_lifecycle_xcode"],
                        "priority": "high",
                        "notes": "Apple Privacy Manifest for Required Reason API compliance"
                    },
                    {
                        "pattern": "\\.swift$|\\.m$|\\.h$",
                        "skills": ["ios_fundamentals_swift", "ios_uikit_swiftui", "ios_architecture_patterns", "ios_reactive_concurrency", "ios_data_persistence_networking"],
                        "priority": "high",
                        "notes": "Core iOS source code analyzed for SwiftUI, UIKit, Swift Concurrency, Combine, Core Data, and SwiftData"
                    },
                    {
                        "pattern": "Fastfile|Matchfile|Appfile|Pluginfile",
                        "skills": ["ios_platform_quality_distribution"],
                        "priority": "high",
                        "notes": "Fastlane CI/CD automation and code signing configuration"
                    },
                    {
                        "pattern": "*Tests\\.swift|*UITests\\.swift|*Spec\\.swift",
                        "skills": ["ios_platform_quality_distribution"],
                        "priority": "high",
                        "notes": "XCTest unit tests, URLProtocol mocks, and XCUITest automated UI test suites"
                    }
                ]
            },
            {
                "step": 2,
                "name": "dependency_extraction",
                "source_manifests": [
                    "Package.swift",
                    "Podfile",
                    "Podfile.lock",
                    "Cartfile"
                ],
                "relevant_dependencies": {
                    "ios_data_persistence_networking": ["Alamofire", "Moya", "KeychainAccess", "GRDB", "RealmSwift"],
                    "ios_architecture_patterns": ["swift-composable-architecture", "Factory", "Swinject", "Resolver"],
                    "ios_uikit_swiftui": ["SnapKit", "Kingfisher", "SDWebImageSwiftUI", "Lottie"],
                    "ios_reactive_concurrency": ["RxSwift", "RxCocoa", "CombineExt", "AsyncAlgorithms"],
                    "ios_platform_quality_distribution": ["Quick", "Nimble", "SnapshotTesting", "FirebaseCrashlytics"]
                }
            },
            {
                "step": 3,
                "name": "config_file_scan",
                "target_configs": [
                    "Package.swift",
                    "Podfile",
                    "Info.plist",
                    "PrivacyInfo.xcprivacy",
                    "fastlane/Fastfile",
                    "fastlane/Matchfile",
                    "apple-app-site-association"
                ]
            }
        ]
    },
    "ai_analysis_instructions": {
        "tasks": [
            "Map detected signals to composite keys ({skill_id}.{subskill_id}) using patterns defined in ios skill files",
            "Inspect Package.swift and Podfile dependencies for modern iOS frameworks (TCA, Alamofire, RxSwift, KeychainAccess)",
            "Check UI architecture — presence of SwiftUI with Observable macro vs UIKit with programmatic AutoLayout / Diffable Data Sources",
            "Evaluate concurrency safety — verify usage of modern Swift Concurrency (async/await, Actors, @MainActor) vs legacy GCD",
            "Assess test coverage — presence of XCTest unit tests, URLProtocol network mocking, and XCUITest UI tests"
        ]
    }
}

with open(os.path.join(base_dir, 'evidence', 'ios', 'github.json'), 'w', encoding='utf-8') as f:
    json.dump(github_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/ios/github.json")

# cv.json
cv_evidence = {
    "source_id": "cv",
    "name": "CV / Resume Analysis - iOS Developer",
    "description": "Signals extracted from the user's CV/resume to evidence iOS Developer skills. CV data provides self-reported information that must be cross-validated with GitHub and assessment sources.",
    "extraction_rules": {
        "description": "How to extract and weight information from CV content for iOS roles.",
        "sections": [
            {
                "section": "skills_list",
                "description": "Explicit list of technologies, frameworks, and tools in skills section.",
                "base_strength": 0.3,
                "notes": "Low strength alone. Listing 'Swift' or 'SwiftUI' requires verification against project details."
            },
            {
                "section": "work_experience",
                "description": "Job descriptions describing iOS engineering achievements and architectural responsibilities.",
                "base_strength": 0.5,
                "quality_indicators": [
                    "Specific iOS frameworks and architectural patterns mentioned (e.g. 'architected SPM multi-package app with SwiftUI and TCA')",
                    "Quantifiable mobile performance metrics (reduced app binary size by 35% with App Thinning, eliminated memory leaks with Instruments)",
                    "Action verbs indicating hands-on mobile leadership (architected, migrated, modularized, optimized, signed)",
                    "Scale indicators (apps with 1M+ MAU, App Store featured apps)"
                ]
            },
            {
                "section": "projects",
                "description": "Personal or open-source iOS projects demonstrating technical depth.",
                "base_strength": 0.4,
                "notes": "Higher strength if linked to GitHub with clean SwiftUI, SwiftData/CoreData persistence, and test suites."
            },
            {
                "section": "certifications",
                "description": "Apple developer certifications or training programs.",
                "base_strength": 0.2
            }
        ]
    },
    "signal_mapping": {
        "description": "How CV mentions map to skill evidence using COMPOSITE KEYS ({skill_id}.{subskill_id}).",
        "patterns": [
            {
                "pattern": "Built reactive iOS user interfaces with SwiftUI, Observable macro, and UIKit interoperability",
                "maps_to": ["ios_uikit_swiftui.swiftui_views_state_basics", "ios_uikit_swiftui.swiftui_state_management", "ios_uikit_swiftui.uikit_swiftui_interoperability"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Implemented offline-first data sync architecture with Core Data / SwiftData and URLSession",
                "maps_to": ["ios_data_persistence_networking.offline_caching_sync_engine", "ios_data_persistence_networking.core_data_fundamentals", "ios_data_persistence_networking.urlsession_codable_networking"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Modularized monolithic iOS codebase into Swift Packages using SPM",
                "maps_to": ["ios_architecture_patterns.modularization_spm_frameworks", "ios_architecture_patterns.microapps_plugin_architecture"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Migrated legacy RxSwift codebase to native Swift Concurrency and Combine",
                "maps_to": ["ios_reactive_concurrency.rxswift_reactive_patterns", "ios_reactive_concurrency.async_await_structured_concurrency", "ios_reactive_concurrency.combine_publishers_subscribers"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Scheduled background tasks using BGTaskScheduler and developed WidgetKit extensions",
                "maps_to": ["ios_app_lifecycle_xcode.background_modes_tasks", "ios_app_lifecycle_xcode.app_extensions_widgets"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Eliminated multi-threaded data races using Actor isolation and Thread Sanitizer",
                "maps_to": ["ios_reactive_concurrency.actors_thread_safety", "ios_reactive_concurrency.concurrency_data_races_tsan"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Profiled iOS apps using Xcode Instruments and eliminated memory leaks",
                "maps_to": ["ios_app_lifecycle_xcode.instruments_profiling_performance", "ios_fundamentals_swift.arc_memory_management"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Hardened app security using Keychain Services, SSL Certificate Pinning, and Privacy Manifests",
                "maps_to": ["ios_data_persistence_networking.keychain_secure_storage", "ios_data_persistence_networking.network_security_ssl_pinning", "ios_app_lifecycle_xcode.app_store_guidelines_privacy"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Automated iOS build and release pipelines using Fastlane Match and TestFlight",
                "maps_to": ["ios_platform_quality_distribution.ci_cd_fastlane_testflight", "ios_platform_quality_distribution.app_thinning_size_optimization"],
                "strength_modifier": 1.0
            }
        ]
    },
    "important_notes": [
        "Distinguish between client-side API consumption (URLSession/Keychain) and backend API design (be_api_design)",
        "Look for modern iOS stack competencies (SwiftUI, Swift Concurrency, SwiftData/CoreData, SPM) vs legacy Objective-C MVC",
        "Cross-validate self-reported performance claims with code in GitHub and assessment results"
    ]
}

with open(os.path.join(base_dir, 'evidence', 'ios', 'cv.json'), 'w', encoding='utf-8') as f:
    json.dump(cv_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/ios/cv.json")

# linkedin.json
linkedin_evidence = {
    "source_id": "linkedin",
    "name": "LinkedIn Profile Analysis - iOS Developer",
    "description": "Signals extracted from LinkedIn profiles to evidence iOS Developer skills.",
    "extraction_rules": {
        "sections": [
            {
                "section": "headline_summary",
                "description": "Profile headline and summary section.",
                "base_strength": 0.2,
                "notes": "Look for specialization (e.g. 'Senior iOS Engineer | SwiftUI | Swift Concurrency | SPM')."
            },
            {
                "section": "experience",
                "description": "Work experience entries with job titles and project descriptions.",
                "base_strength": 0.4,
                "quality_indicators": [
                    "iOS-specific job titles (iOS Engineer, Mobile Platform Architect, iOS Lead)",
                    "Technologies described (Swift, SwiftUI, Combine, Swift Concurrency, Core Data, SPM)",
                    "Scale and popularity of apps developed"
                ]
            },
            {
                "section": "skills_endorsements",
                "description": "Skills listed with endorsements.",
                "base_strength": 0.15
            },
            {
                "section": "recommendations",
                "description": "Written peer and manager recommendations.",
                "base_strength": 0.3
            }
        ]
    },
    "signal_mapping": {
        "description": "How LinkedIn mentions map to skill evidence using COMPOSITE KEYS ({skill_id}.{subskill_id}).",
        "patterns": [
            {
                "pattern": "LinkedIn skills endorsement for 'Swift' or 'iOS Development'",
                "maps_to": ["ios_fundamentals_swift.swift_language_fundamentals", "ios_app_lifecycle_xcode.app_delegate_scene_delegate"],
                "strength_modifier": 0.33
            },
            {
                "pattern": "LinkedIn skills endorsement for 'SwiftUI' or 'UIKit'",
                "maps_to": ["ios_uikit_swiftui.swiftui_views_state_basics", "ios_uikit_swiftui.uikit_autolayout_programmatic"],
                "strength_modifier": 0.33
            },
            {
                "pattern": "Job experience describing building SwiftUI design systems and SPM modular apps",
                "maps_to": ["ios_uikit_swiftui.swiftui_views_state_basics", "ios_architecture_patterns.modularization_spm_frameworks", "ios_architecture_patterns.mvc_mvvm_architecture"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing Swift Concurrency, Combine pipelines, and Core Data sync engines",
                "maps_to": ["ios_reactive_concurrency.async_await_structured_concurrency", "ios_reactive_concurrency.combine_publishers_subscribers", "ios_data_persistence_networking.offline_caching_sync_engine"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing Fastlane CI/CD automation, TestFlight, and Keychain security",
                "maps_to": ["ios_platform_quality_distribution.ci_cd_fastlane_testflight", "ios_data_persistence_networking.keychain_secure_storage"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing WidgetKit extensions, Universal Links, and Xcode Instruments profiling",
                "maps_to": ["ios_app_lifecycle_xcode.app_extensions_widgets", "ios_app_lifecycle_xcode.universal_links_deep_linking", "ios_app_lifecycle_xcode.instruments_profiling_performance"],
                "strength_modifier": 1.0
            }
        ]
    },
    "important_notes": [
        "ALL extracted signals MUST be mapped to COMPOSITE KEYS ({skill_id}.{subskill_id})",
        "LinkedIn endorsements have low evidential value on their own; cross-validate with code"
    ]
}

with open(os.path.join(base_dir, 'evidence', 'ios', 'linkedin.json'), 'w', encoding='utf-8') as f:
    json.dump(linkedin_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/ios/linkedin.json")

print("iOS skills, roles, and github/cv/linkedin evidence generated successfully.")
