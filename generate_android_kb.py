import os
import json

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'knowledge-base'))

# Ensure directories
os.makedirs(os.path.join(base_dir, 'skills', 'android'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'roles', 'android'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'evidence', 'android'), exist_ok=True)

CRITICAL_NOTE = "Mobil networking ve credential saklama (Retrofit/URLSession, Keychain/DataStore) istemci tarafında API tüketimi ve güvenli yerel depolamadır; Backend'in be_api_design/be_auth_security'si sunucu tarafında API sunma ve credential doğrulamadır — farklı taraflar, farklı sorumluluklar."

# -------------------------------------------------------------
# 1. Android Skills Definition
# -------------------------------------------------------------
android_skills = [
    {
        "skill_id": "android_fundamentals_kotlin",
        "name": "Kotlin Language & Android SDK Fundamentals",
        "category": "mobile_core",
        "description": "Core Kotlin programming language proficiency and Android SDK architectural foundations. Covers idiomatic Kotlin features (null safety, extensions, sealed types), generics variance, delegated properties, DSL builders, KSP compiler plugins, JVM bytecode memory layout optimization, and Kotlin Multiplatform (KMP) shared logic architecture.",
        "subskills": [
            {
                "id": "kotlin_language_features",
                "name": "Kotlin Idiomatic Features & Null Safety",
                "description": "Applying idiomatic Kotlin features including compile-time null safety (nullable vs non-nullable types, safe calls ?., elvis operator ?:), data classes, sealed classes/interfaces for exhaustive when modeling, inline value classes, and extension functions.",
                "keywords": ["Kotlin null safety", "sealed classes", "data classes", "extension functions", "inline value classes", "smart casting", "exhaustive when"]
            },
            {
                "id": "kotlin_higher_order_lambdas",
                "name": "Higher-Order Functions & Scope Functions",
                "description": "Utilizing higher-order functions, function references, lambda expressions, and Kotlin scope functions (let, apply, run, also, with) with precise selection criteria based on context object receiver (this vs it) and return value.",
                "keywords": ["higher-order functions", "scope functions (let/apply/run/also/with)", "lambdas", "inline functions", "noinline", "crossinline", "function references"]
            },
            {
                "id": "android_sdk_lifecycle_basics",
                "name": "Android SDK Architecture & Context Hierarchy",
                "description": "Navigating the Android SDK architecture, API level compatibility (minSdk, targetSdk, compileSdk), application class lifecycle, and Context taxonomy (ApplicationContext vs ActivityContext, memory leak prevention when holding Context references).",
                "keywords": ["Android SDK", "minSdk/targetSdk/compileSdk", "Context hierarchy", "ApplicationContext vs ActivityContext", "Application class", "Context leak prevention"]
            },
            {
                "id": "kotlin_generics_variance",
                "name": "Kotlin Generics & Type Variance",
                "description": "Designing generic classes and functions with declaration-site variance (out for covariance, in for contravariance), type projections (use-site variance), reified type parameters with inline functions, and generic constraints.",
                "keywords": ["Kotlin generics", "declaration-site variance", "covariance (out)", "contravariance (in)", "reified type parameters", "type projections", "where clause constraints"]
            },
            {
                "id": "kotlin_delegated_properties",
                "name": "Delegated Properties & Custom Delegates",
                "description": "Implementing and utilizing standard Kotlin property delegates (lazy, Delegates.observable, Delegates.vetoable, Delegates.notNull) and authoring custom ReadWriteProperty/ReadOnlyProperty delegates for Android lifecycle, SharedPreferences, or ViewBinding.",
                "keywords": ["delegated properties", "by lazy", "Delegates.observable", "Delegates.vetoable", "custom property delegates", "ReadWriteProperty", "ReadOnlyProperty"]
            },
            {
                "id": "kotlin_dsl_type_safe_builders",
                "name": "Type-Safe Builders & Kotlin DSLs",
                "description": "Authoring type-safe DSL builders using function literals with receivers (T.() -> Unit), @DslMarker annotation to enforce scope control, and maintaining Gradle Kotlin DSL (build.gradle.kts) build scripts with version catalogs.",
                "keywords": ["Kotlin DSL", "type-safe builders", "function literal with receiver", "@DslMarker", "build.gradle.kts", "Gradle version catalogs", "libs.versions.toml"]
            },
            {
                "id": "kotlin_compiler_plugins_ksp",
                "name": "Kotlin Symbol Processing (KSP) & Compiler Plugins",
                "description": "Authoring and maintaining custom annotation processors using Kotlin Symbol Processing (KSP) API, understanding KSP performance benefits over KAPT (Kotlin Annotation Processing Tool with Java stubs), and integrating Kotlin compiler plugins.",
                "keywords": ["KSP (Kotlin Symbol Processing)", "KAPT migration", "SymbolProcessor", "KSVisitor", "code generation", "compiler plugins", "annotation processing performance"]
            },
            {
                "id": "kotlin_memory_model_bytecode",
                "name": "Kotlin JVM Bytecode & Memory Optimization",
                "description": "Analyzing decompiled Kotlin JVM bytecode, measuring runtime overhead of lambdas (capturing vs non-capturing), primitive boxing/unboxing costs in generic collections, companion object overhead, and optimizing memory allocation on ART runtime.",
                "keywords": ["JVM bytecode analysis", "capturing lambdas", "primitive boxing overhead", "ART runtime memory layout", "companion object bytecode", "inline function inlining"]
            },
            {
                "id": "multiplatform_kotlin_kmp",
                "name": "Kotlin Multiplatform (KMP) Architecture",
                "description": "Architecting shared business logic across Android and iOS using Kotlin Multiplatform (KMP), managing expect/actual platform declarations, sharing network/database/domain layers with Ktor/SqlDelight, and structuring multiplatform sourceSets.",
                "keywords": ["Kotlin Multiplatform (KMP)", "expect/actual declarations", "shared domain logic", "Ktor client shared", "SqlDelight KMP", "KMP sourceSets", "multiplatform architecture"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Kotlin source code with idioms (sealed interfaces, extension functions, scope functions)",
                    "detection": "content_analysis",
                    "pattern": "sealed (class|interface)|inline value class|fun <.*> .*\\.ext|\\.let \\{.*\\}|\\.apply \\{",
                    "strength": 0.8,
                    "maps_to": ["android_fundamentals_kotlin.kotlin_language_features", "android_fundamentals_kotlin.kotlin_higher_order_lambdas"]
                },
                {
                    "signal": "Gradle build scripts using Kotlin DSL and version catalogs",
                    "detection": "file_presence",
                    "pattern": "build\\.gradle\\.kts|settings\\.gradle\\.kts|gradle/libs\\.versions\\.toml",
                    "strength": 0.8,
                    "maps_to": ["android_fundamentals_kotlin.kotlin_dsl_type_safe_builders", "android_fundamentals_kotlin.android_sdk_lifecycle_basics"]
                },
                {
                    "signal": "Kotlin Symbol Processing (KSP) processor implementation or configuration",
                    "detection": "content_analysis",
                    "pattern": "SymbolProcessorProvider|SymbolProcessor|com\\.google\\.devtools\\.ksp|ksp\\(",
                    "strength": 0.9,
                    "maps_to": ["android_fundamentals_kotlin.kotlin_compiler_plugins_ksp"]
                },
                {
                    "signal": "Kotlin Multiplatform project configuration and expect/actual declarations",
                    "detection": "content_analysis",
                    "pattern": "kotlin\\(\"multiplatform\"\\)|expect (class|fun|val)|actual (class|fun|val)|commonMain",
                    "strength": 0.9,
                    "maps_to": ["android_fundamentals_kotlin.multiplatform_kotlin_kmp"]
                }
            ],
            "cv": [
                {
                    "signal": "Developed Android applications using Kotlin, custom DSLs, and modern SDKs",
                    "strength": 0.8,
                    "maps_to": ["android_fundamentals_kotlin.kotlin_language_features", "android_fundamentals_kotlin.android_sdk_lifecycle_basics", "android_fundamentals_kotlin.kotlin_dsl_type_safe_builders"]
                },
                {
                    "signal": "Architected Kotlin Multiplatform (KMP) shared modules between Android and iOS",
                    "strength": 0.9,
                    "maps_to": ["android_fundamentals_kotlin.multiplatform_kotlin_kmp", "android_fundamentals_kotlin.kotlin_generics_variance"]
                },
                {
                    "signal": "Built custom KSP compiler plugins or optimized Kotlin JVM bytecode performance",
                    "strength": 0.9,
                    "maps_to": ["android_fundamentals_kotlin.kotlin_compiler_plugins_ksp", "android_fundamentals_kotlin.kotlin_memory_model_bytecode"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Kotlin, Android Development, or Kotlin Multiplatform endorsed",
                    "strength": 0.5,
                    "maps_to": ["android_fundamentals_kotlin.kotlin_language_features", "android_fundamentals_kotlin.android_sdk_lifecycle_basics"]
                },
                {
                    "signal": "Job experience describing KMP migration, custom Gradle DSLs, or Kotlin compiler tooling",
                    "strength": 0.8,
                    "maps_to": ["android_fundamentals_kotlin.multiplatform_kotlin_kmp", "android_fundamentals_kotlin.kotlin_compiler_plugins_ksp", "android_fundamentals_kotlin.kotlin_delegated_properties"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["kotlin_language_features", "kotlin_higher_order_lambdas", "android_sdk_lifecycle_basics"],
                "description": "Writes idiomatic Kotlin code with null safety, utilizes scope functions cleanly, and understands Android SDK Context hierarchies and application lifecycles."
            },
            "mid": {
                "expected_subskills": ["kotlin_generics_variance", "kotlin_delegated_properties", "kotlin_dsl_type_safe_builders"],
                "description": "Applies generics type variance, implements custom property delegates, and maintains type-safe Kotlin DSL Gradle build scripts."
            },
            "senior": {
                "expected_subskills": ["kotlin_compiler_plugins_ksp", "kotlin_memory_model_bytecode", "multiplatform_kotlin_kmp"],
                "description": "Authors KSP annotation processors, analyzes decompiled bytecode for memory optimizations, and architects cross-platform Kotlin Multiplatform (KMP) shared systems."
            }
        }
    },
    {
        "skill_id": "android_app_components",
        "name": "Android Application Components & Process Lifecycle",
        "category": "mobile_core",
        "description": "Deep understanding and implementation of the core Android application building blocks (Activities, Fragments, Services, BroadcastReceivers, ContentProviders, WorkManager), Intent routing, Android IPC / Binder architecture, process priorities, Low Memory Killer (LMK) survival, and deep link verification.",
        "subskills": [
            {
                "id": "activity_lifecycle_navigation",
                "name": "Activity Lifecycle & State Restoration",
                "description": "Managing Activity lifecycle callbacks (onCreate, onStart, onResume, onPause, onStop, onDestroy, onRestart), handling runtime configuration changes without state loss, saving UI state with onSaveInstanceState and SavedStateHandle, and using Activity Result API.",
                "keywords": ["Activity lifecycle", "onSaveInstanceState", "SavedStateHandle", "configuration changes", "ActivityResultLauncher", "launchMode (standard/singleTop/singleTask/singleInstance)"]
            },
            {
                "id": "fragment_lifecycle_manager",
                "name": "Fragment Lifecycle & Backstack Transactions",
                "description": "Mastering Fragment lifecycle states (viewLifecycleOwner vs Fragment lifecycle), FragmentManager backstack operations (add, replace, addToBackStack), Fragment Result API for inter-fragment communication, and avoiding fragment transaction state loss exceptions.",
                "keywords": ["Fragment lifecycle", "viewLifecycleOwner", "FragmentManager", "FragmentTransaction", "Fragment Result API", "commitAllowingStateLoss", "backstack navigation"]
            },
            {
                "id": "broadcast_receivers_intents",
                "name": "BroadcastReceivers & Intent Filter Resolution",
                "description": "Registering static (AndroidManifest.xml) and dynamic (registerReceiver) BroadcastReceivers with exported flags (RECEIVER_EXPORTED vs RECEIVER_NOT_EXPORTED in Android 13+), intent filter matching rules, ordered broadcasts, and system broadcast handling.",
                "keywords": ["BroadcastReceiver", "Intent filters", "dynamic receiver registration", "RECEIVER_EXPORTED", "ordered broadcasts", "system broadcasts", "implicit vs explicit intents"]
            },
            {
                "id": "service_architecture_types",
                "name": "Foreground, Background & Bound Services",
                "description": "Architecting Android Services — implementing Foreground Services with ongoing notifications and foregroundServiceType (Android 14+), Bound Services with IBinder and ServiceConnection, background execution limits, and startService vs bindService lifecycles.",
                "keywords": ["Foreground Service", "foregroundServiceType (Android 14)", "Bound Service", "ServiceConnection", "IBinder", "background execution limits", "ongoing notification"]
            },
            {
                "id": "content_providers_sharing",
                "name": "ContentProviders & Secure Data Sharing",
                "description": "Implementing custom ContentProviders for structured data sharing across apps, UriMatcher for URI resolution, ContentResolver CRUD operations, FileProvider for secure file URI sharing (content:// vs file://), and granting temporary URI permissions.",
                "keywords": ["ContentProvider", "ContentResolver", "UriMatcher", "FileProvider", "content:// URI", "grantUriPermission", "cross-app data sharing"]
            },
            {
                "id": "workmanager_background_jobs",
                "name": "WorkManager & Guaranteed Deferrable Work",
                "description": "Scheduling guaranteed background work with WorkManager, configuring PeriodicWorkRequest vs OneTimeWorkRequest, applying runtime Constraints (network, battery, charging), chaining sequential and parallel tasks, and implementing CoroutineWorker with ForegroundInfo.",
                "keywords": ["WorkManager", "CoroutineWorker", "PeriodicWorkRequest", "OneTimeWorkRequest", "WorkConstraints", "chained work", "expedited work / setExpedited", "ForegroundInfo"]
            },
            {
                "id": "ipc_aid_binder_architecture",
                "name": "Android IPC & AIDL Binder Architecture",
                "description": "Designing Inter-Process Communication (IPC) across separate Android processes using the Binder driver, writing Android Interface Definition Language (AIDL) files, handling Parcelable data marshaling, and managing dead object exceptions (DeadObjectException / DeathRecipient).",
                "keywords": ["Android IPC", "AIDL (.aidl)", "Binder driver", "Parcelable marshaling", "IBinder DeathRecipient", "Messenger IPC", "cross-process transactions"]
            },
            {
                "id": "process_lifecycle_management",
                "name": "Process Priority & Low Memory Killer (LMK)",
                "description": "Understanding Android process lifecycle states (Foreground, Visible, Service, Cached), the Low Memory Killer (LMK) oom_adj scoring mechanism, designing memory-resilient applications that survive process death, and multi-process application architecture (:remote).",
                "keywords": ["Low Memory Killer (LMK)", "oom_adj / oom_score_adj", "process death survival", "cached processes", "multi-process architecture (android:process)", "memory trims (onTrimMemory)"]
            },
            {
                "id": "deep_linking_app_links",
                "name": "Deep Links & Android App Links Verification",
                "description": "Designing unified deep linking architectures — standard URI schemes vs verified Android App Links (Digital Asset Links with assetlinks.json), handling intent filter verification on Android 12+, backstack synthesis on deep link entry, and deep link routing engines.",
                "keywords": ["Android App Links", "Digital Asset Links (assetlinks.json)", "deep link verification", "intent-filter autoVerify", "TaskStackBuilder", "deep link routing", "custom URI schemes"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "AndroidManifest.xml with component declarations, intent filters, and permissions",
                    "detection": "file_presence",
                    "pattern": "AndroidManifest\\.xml",
                    "strength": 0.8,
                    "maps_to": ["android_app_components.activity_lifecycle_navigation", "android_app_components.broadcast_receivers_intents", "android_app_components.deep_linking_app_links"]
                },
                {
                    "signal": "WorkManager Worker or CoroutineWorker implementations",
                    "detection": "content_analysis",
                    "pattern": ": CoroutineWorker|: Worker|WorkManager\\.getInstance|PeriodicWorkRequestBuilder",
                    "strength": 0.8,
                    "maps_to": ["android_app_components.workmanager_background_jobs"]
                },
                {
                    "signal": "Foreground Service or Bound Service implementation",
                    "detection": "content_analysis",
                    "pattern": "startForeground\\(|ServiceConnection|onBind\\(Intent\\)|foregroundServiceType",
                    "strength": 0.8,
                    "maps_to": ["android_app_components.service_architecture_types"]
                },
                {
                    "signal": "AIDL file definition or Binder IPC implementation",
                    "detection": "file_presence",
                    "pattern": "\\.aidl$|Stub\\.asInterface|DeathRecipient",
                    "strength": 0.9,
                    "maps_to": ["android_app_components.ipc_aid_binder_architecture"]
                },
                {
                    "signal": "Digital Asset Links configuration for Android App Links",
                    "detection": "content_analysis",
                    "pattern": "assetlinks\\.json|android:autoVerify=\"true\"|TaskStackBuilder",
                    "strength": 0.9,
                    "maps_to": ["android_app_components.deep_linking_app_links"]
                }
            ],
            "cv": [
                {
                    "signal": "Implemented background processing with WorkManager and Foreground Services",
                    "strength": 0.8,
                    "maps_to": ["android_app_components.workmanager_background_jobs", "android_app_components.service_architecture_types"]
                },
                {
                    "signal": "Architected deep linking navigation and verified Android App Links",
                    "strength": 0.8,
                    "maps_to": ["android_app_components.deep_linking_app_links", "android_app_components.activity_lifecycle_navigation"]
                },
                {
                    "signal": "Designed multi-process Android architecture or IPC services with AIDL",
                    "strength": 0.9,
                    "maps_to": ["android_app_components.ipc_aid_binder_architecture", "android_app_components.process_lifecycle_management"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Android SDK, WorkManager, or App Components endorsed",
                    "strength": 0.5,
                    "maps_to": ["android_app_components.activity_lifecycle_navigation", "android_app_components.workmanager_background_jobs"]
                },
                {
                    "signal": "Job experience describing Android component lifecycles, background services, or IPC architecture",
                    "strength": 0.8,
                    "maps_to": ["android_app_components.service_architecture_types", "android_app_components.process_lifecycle_management", "android_app_components.fragment_lifecycle_manager"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["activity_lifecycle_navigation", "fragment_lifecycle_manager", "broadcast_receivers_intents"],
                "description": "Manages Activity and Fragment lifecycles with state restoration, handles backstack transactions, and registers broadcast receivers."
            },
            "mid": {
                "expected_subskills": ["service_architecture_types", "content_providers_sharing", "workmanager_background_jobs"],
                "description": "Builds foreground services meeting modern Android constraints, shares data via ContentProviders/FileProvider, and schedules background tasks with WorkManager."
            },
            "senior": {
                "expected_subskills": ["ipc_aid_binder_architecture", "process_lifecycle_management", "deep_linking_app_links"],
                "description": "Architects multi-process IPC using AIDL/Binder, engineers applications for LMK process death survival, and implements verified Android App Links routing."
            }
        }
    },
    {
        "skill_id": "android_ui_layouts",
        "name": "Android UI Development, Views & Jetpack Compose",
        "category": "mobile_core",
        "description": "Modern and traditional Android UI engineering spanning Jetpack Compose declarative UI, XML layouts (ConstraintLayout), RecyclerView performance, custom Canvas drawing, Compose state and side-effects, compiler stability optimization, Material 3 design systems, and 120fps UI profiling.",
        "subskills": [
            {
                "id": "xml_layouts_view_binding",
                "name": "XML Layouts, ConstraintLayout & ViewBinding",
                "description": "Building XML layouts using ConstraintLayout (guidelines, barriers, chains, flow virtual layouts), ViewBinding for type-safe view lookups replacing findViewById, style/theme definitions, and layout inflation.",
                "keywords": ["ConstraintLayout", "ViewBinding", "XML layouts", "Barriers/Chains/Guidelines", "layout_optimization", "styles/themes", "ViewBinding inflate"]
            },
            {
                "id": "recyclerview_adapter_patterns",
                "name": "RecyclerView, ListAdapter & DiffUtil",
                "description": "Implementing high-performance lists with RecyclerView, ListAdapter with AsyncListDiffer and DiffUtil for granular item update animations, custom ItemTouchHelper for swipe/drag gestures, and multiple ViewHolder view types.",
                "keywords": ["RecyclerView", "ListAdapter", "DiffUtil.ItemCallback", "AsyncListDiffer", "ViewHolder pattern", "multiple view types", "ItemTouchHelper", "item view recycling"]
            },
            {
                "id": "compose_fundamentals_state",
                "name": "Jetpack Compose Fundamentals & State",
                "description": "Building declarative UIs with Jetpack Compose, understanding unidirectional data flow in UI, managing state with remember, mutableStateOf, and rememberSaveable, and applying state hoisting patterns to create stateless, reusable composables.",
                "keywords": ["Jetpack Compose", "@Composable", "remember", "mutableStateOf", "rememberSaveable", "State hoisting", "unidirectional data flow"]
            },
            {
                "id": "compose_layout_modifiers",
                "name": "Compose Layouts, Modifiers & Lazy Lists",
                "description": "Designing complex layouts with Box, Column, Row, LazyColumn/LazyRow (with items, keys, and contentType for composition recycling), applying and chaining Modifiers (layout, draw, pointerInput), and custom Layout composables.",
                "keywords": ["LazyColumn / LazyRow", "Modifier chaining", "Box/Column/Row", "contentType in Lazy layouts", "custom Layout composable", "SubcomposeLayout", "Intrinsic measurements"]
            },
            {
                "id": "custom_views_canvas_drawing",
                "name": "Custom Views & 2D Canvas Drawing",
                "description": "Subclassing View/ViewGroup to build custom views from scratch, overriding onMeasure (MeasureSpec modes: EXACTLY, AT_MOST, UNSPECIFIED), onLayout, and onDraw using Canvas, Paint, Path, and handling custom touch gestures in onTouchEvent.",
                "keywords": ["Custom View", "onMeasure / MeasureSpec", "onDraw / Canvas", "Paint & Path", "onTouchEvent / GestureDetector", "custom XML declare-styleable attributes"]
            },
            {
                "id": "compose_side_effects_lifecycle",
                "name": "Compose Side-Effects & Lifecycle",
                "description": "Managing asynchronous operations and external state in Compose using side-effect handlers: LaunchedEffect, rememberCoroutineScope, DisposableEffect for resource cleanup, SideEffect, rememberUpdatedState, and derivedStateOf for calculation caching.",
                "keywords": ["LaunchedEffect", "rememberCoroutineScope", "DisposableEffect", "SideEffect", "rememberUpdatedState", "derivedStateOf", "produceState"]
            },
            {
                "id": "compose_compiler_recomposition",
                "name": "Compose Compiler Metrics & Recomposition Tuning",
                "description": "Analyzing Compose compiler metrics (composable reports), understanding parameter Stability inference (@Stable, @Immutable annotations), eliminating unnecessary recompositions, avoiding lambda instantiation in recomposition loops, and using Compose layout inspector.",
                "keywords": ["Compose compiler metrics", "@Stable / @Immutable", "Stability inference", "recomposition optimization", "Layout Inspector recomposition counters", "unstable parameters fix"]
            },
            {
                "id": "design_systems_theming",
                "name": "Material Design 3 & Design System Architecture",
                "description": "Architecting scalable design systems using Material Design 3 (Material You), dynamic color theming, custom Typography, Shapes, ColorScheme palettes, building custom reusable component libraries, and supporting dark/light/contrast themes.",
                "keywords": ["Material Design 3 (M3)", "MaterialTheme", "Dynamic Color (Material You)", "ColorScheme tokenization", "Design System component library", "custom Typography & Shapes"]
            },
            {
                "id": "ui_performance_profiling",
                "name": "UI Rendering Pipeline & 120fps Profiling",
                "description": "Profiling the Android UI rendering pipeline (Measure, Layout, Draw), measuring UI frame rendering performance using JankStats, identifying and eliminating GPU overdraw in Developer Options, Systrace / Perfetto UI thread frame analysis, and achieving stable 120fps rendering.",
                "keywords": ["JankStats library", "GPU Overdraw elimination", "Perfetto / Systrace UI frame analysis", "120fps rendering", "Choreographer frame drops", "RenderThread profiling"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Jetpack Compose UI components and state management",
                    "detection": "content_analysis",
                    "pattern": "@Composable|remember \\{ mutableStateOf|rememberSaveable|LazyColumn \\{",
                    "strength": 0.8,
                    "maps_to": ["android_ui_layouts.compose_fundamentals_state", "android_ui_layouts.compose_layout_modifiers"]
                },
                {
                    "signal": "Compose side-effects or derivedStateOf optimizations",
                    "detection": "content_analysis",
                    "pattern": "LaunchedEffect\\(|DisposableEffect\\(|derivedStateOf \\{|rememberUpdatedState",
                    "strength": 0.8,
                    "maps_to": ["android_ui_layouts.compose_side_effects_lifecycle"]
                },
                {
                    "signal": "RecyclerView ListAdapter with DiffUtil implementation",
                    "detection": "content_analysis",
                    "pattern": ": ListAdapter<.*,.*>|DiffUtil\\.ItemCallback|AsyncListDiffer",
                    "strength": 0.8,
                    "maps_to": ["android_ui_layouts.recyclerview_adapter_patterns"]
                },
                {
                    "signal": "Custom View implementation with onMeasure and onDraw Canvas",
                    "detection": "content_analysis",
                    "pattern": "override fun onDraw\\(canvas: Canvas\\)|override fun onMeasure\\(|MeasureSpec\\.getMode",
                    "strength": 0.9,
                    "maps_to": ["android_ui_layouts.custom_views_canvas_drawing"]
                },
                {
                    "signal": "Compose stability annotations or compiler metrics configuration",
                    "detection": "content_analysis",
                    "pattern": "@Immutable|@Stable|composeCompilerMetricsReports|enableCompilerMetrics",
                    "strength": 0.9,
                    "maps_to": ["android_ui_layouts.compose_compiler_recomposition"]
                }
            ],
            "cv": [
                {
                    "signal": "Built reactive Android UIs using Jetpack Compose and Material 3 design systems",
                    "strength": 0.8,
                    "maps_to": ["android_ui_layouts.compose_fundamentals_state", "android_ui_layouts.design_systems_theming", "android_ui_layouts.compose_layout_modifiers"]
                },
                {
                    "signal": "Optimized Jetpack Compose recomposition performance using compiler metrics",
                    "strength": 0.9,
                    "maps_to": ["android_ui_layouts.compose_compiler_recomposition", "android_ui_layouts.ui_performance_profiling"]
                },
                {
                    "signal": "Created custom 2D Canvas views and eliminated GPU overdraw for 120fps rendering",
                    "strength": 0.9,
                    "maps_to": ["android_ui_layouts.custom_views_canvas_drawing", "android_ui_layouts.ui_performance_profiling"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Jetpack Compose, Android UI, or Material Design endorsed",
                    "strength": 0.5,
                    "maps_to": ["android_ui_layouts.compose_fundamentals_state", "android_ui_layouts.design_systems_theming"]
                },
                {
                    "signal": "Job experience describing Jetpack Compose architecture, custom views, or UI jank elimination",
                    "strength": 0.8,
                    "maps_to": ["android_ui_layouts.compose_compiler_recomposition", "android_ui_layouts.ui_performance_profiling", "android_ui_layouts.compose_side_effects_lifecycle"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["xml_layouts_view_binding", "recyclerview_adapter_patterns", "compose_fundamentals_state"],
                "description": "Constructs XML layouts with ConstraintLayout, implements RecyclerView lists with ListAdapter and DiffUtil, and builds Compose UIs with state hoisting."
            },
            "mid": {
                "expected_subskills": ["compose_layout_modifiers", "custom_views_canvas_drawing", "compose_side_effects_lifecycle"],
                "description": "Builds complex Compose layouts with Lazy collections, implements custom 2D Canvas views, and manages asynchronous side-effects in Compose."
            },
            "senior": {
                "expected_subskills": ["compose_compiler_recomposition", "design_systems_theming", "ui_performance_profiling"],
                "description": "Optimizes Compose compiler stability and recompositions, architects enterprise Material 3 design systems, and profiles UI rendering for 120fps execution."
            }
        }
    },
    {
        "skill_id": "android_architecture_patterns",
        "name": "Android Architecture, Dependency Injection & Modularity",
        "category": "mobile_core",
        "description": "Clean, scalable, and testable Android application architecture. Encompasses MVVM, MVI (Unidirectional Data Flow), Clean Architecture domain layers, Dependency Injection with Hilt/Dagger, multi-module modularization strategies, Navigation Compose, and App Startup optimization.",
        "subskills": [
            {
                "id": "mvvm_architecture_pattern",
                "name": "MVVM Pattern & ViewModel Lifecycle",
                "description": "Implementing Model-View-ViewModel architecture, leveraging Android Jetpack ViewModel to survive configuration changes, modeling UI state using immutable data classes, and exposing state to UI via StateFlow/LiveData.",
                "keywords": ["MVVM architecture", "Jetpack ViewModel", "ViewModelProvider", "UI State modeling", "StateFlow in ViewModel", "SingleLiveEvent / Channel events"]
            },
            {
                "id": "dependency_injection_hilt_basics",
                "name": "Dependency Injection with Hilt Fundamentals",
                "description": "Applying dependency injection in Android using Hilt/Dagger, annotating application (@HiltAndroidApp), activities/fragments (@AndroidEntryPoint), view models (@HiltViewModel), constructor injection with @Inject, and providing dependencies with @Module and @Provides.",
                "keywords": ["Hilt DI", "Dagger Hilt", "@HiltAndroidApp", "@AndroidEntryPoint", "@HiltViewModel", "@Inject constructor", "@Module / @Provides"]
            },
            {
                "id": "repository_pattern_data_sources",
                "name": "Repository Pattern & Single Source of Truth",
                "description": "Designing the Repository pattern as the mediator between UI and data layers, coordinating remote API and local database data sources, establishing single source of truth (SSOT) policies, and converting raw DTOs to UI/domain models using mappers.",
                "keywords": ["Repository pattern", "Single Source of Truth (SSOT)", "remote data source", "local data source", "DTO to domain model mappers", "data layer architecture"]
            },
            {
                "id": "clean_architecture_domain_layer",
                "name": "Clean Architecture & Domain Layer UseCases",
                "description": "Structuring applications using Clean Architecture principles, defining pure Kotlin Domain layers independent of Android framework dependencies, authoring single-responsibility UseCases / Interactors, and enforcing dependency inversion.",
                "keywords": ["Clean Architecture", "Domain layer", "UseCase / Interactor pattern", "Dependency Inversion Principle", "business logic isolation", "pure Kotlin modules"]
            },
            {
                "id": "mvi_unidirectional_data_flow",
                "name": "MVI Architecture & Unidirectional Data Flow (UDF)",
                "description": "Implementing Model-View-Intent (MVI) architecture, modeling state machines with sealed Intent/Action, immutable ViewState, and one-shot SideEffect/Event channels, and ensuring strict unidirectional data flow without state synchronization races.",
                "keywords": ["MVI architecture", "Unidirectional Data Flow (UDF)", "Intent / Action modeling", "immutable ViewState", "SideEffect / Event handling", "Redux pattern Android"]
            },
            {
                "id": "advanced_di_scopes_modules",
                "name": "Advanced Dagger/Hilt Scopes & Multi-Bindings",
                "description": "Configuring custom Hilt/Dagger component hierarchies, @InstallIn scopes (SingletonComponent, ActivityRetainedComponent, ViewModelComponent), custom @Scope annotations, Dagger Multi-bindings (@IntoSet, @IntoMap), and @AssistedInject for dynamic runtime parameters.",
                "keywords": ["Hilt scopes (@InstallIn)", "Dagger Multi-bindings (@IntoMap/@IntoSet)", "custom @Scope", "@AssistedInject / AssistedFactory", "subcomponents", "component hierarchies"]
            },
            {
                "id": "modularization_multi_module",
                "name": "Multi-Module Architecture & Feature Modularity",
                "description": "Architecting large-scale Android codebases into multi-module Gradle setups: feature-by-feature modularization, core-api and core-impl split patterns to eliminate circular dependencies, internal visibility modifiers, and dynamic feature delivery modules.",
                "keywords": ["multi-module architecture", "feature modularization", "core-api / core-impl pattern", "circular dependency resolution", "Gradle build parallelization", "Dynamic Feature Modules"]
            },
            {
                "id": "navigation_component_compose",
                "name": "Jetpack Navigation & Navigation Compose",
                "description": "Implementing type-safe in-app navigation using Navigation Compose and Jetpack Navigation Component, passing serialized arguments, defining nested navigation graphs, bottom navigation integration, and managing deep link navigation hierarchies.",
                "keywords": ["Navigation Compose", "NavHost / NavController", "type-safe navigation routes", "nested navigation graphs", "NavBackStackEntry", "bottom bar navigation", "deep link destination mapping"]
            },
            {
                "id": "app_startup_architecture",
                "name": "App Startup & Baseline Profiles Initialization",
                "description": "Optimizing Android application cold start time using the App Startup library (Initializer<T>), eliminating redundant ContentProvider initializers, generating Baseline Profiles using Macrobenchmark to pre-compile critical execution paths on install.",
                "keywords": ["App Startup library", "Initializer<T>", "cold start optimization", "Baseline Profiles", "Macrobenchmark pre-compilation", "lazy dependency initialization"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Hilt or Dagger dependency injection configuration",
                    "detection": "content_analysis",
                    "pattern": "@HiltAndroidApp|@AndroidEntryPoint|@HiltViewModel|@InstallIn\\(|@Module.*@InstallIn",
                    "strength": 0.8,
                    "maps_to": ["android_architecture_patterns.dependency_injection_hilt_basics", "android_architecture_patterns.advanced_di_scopes_modules"]
                },
                {
                    "signal": "Clean Architecture UseCase / Interactor implementations",
                    "detection": "content_analysis",
                    "pattern": "class .*UseCase\\(|class .*Interactor\\(|operator fun invoke\\(",
                    "strength": 0.8,
                    "maps_to": ["android_architecture_patterns.clean_architecture_domain_layer"]
                },
                {
                    "signal": "Multi-module Gradle architecture with feature and core modules",
                    "detection": "file_presence",
                    "pattern": ":feature:.*|:core:.*|include\\(\":.*\"\\)",
                    "strength": 0.9,
                    "maps_to": ["android_architecture_patterns.modularization_multi_module"]
                },
                {
                    "signal": "Navigation Compose type-safe route definitions",
                    "detection": "content_analysis",
                    "pattern": "NavHost\\(|composable<.*>\\(|rememberNavController|NavGraphBuilder",
                    "strength": 0.8,
                    "maps_to": ["android_architecture_patterns.navigation_component_compose"]
                },
                {
                    "signal": "Baseline profile generator or App Startup Initializer",
                    "detection": "content_analysis",
                    "pattern": "BaselineProfileRule|class .*Initializer : Initializer<|macrobenchmark",
                    "strength": 0.9,
                    "maps_to": ["android_architecture_patterns.app_startup_architecture"]
                }
            ],
            "cv": [
                {
                    "signal": "Architected Android apps using Clean Architecture, MVVM/MVI, and Hilt DI",
                    "strength": 0.8,
                    "maps_to": ["android_architecture_patterns.mvvm_architecture_pattern", "android_architecture_patterns.clean_architecture_domain_layer", "android_architecture_patterns.dependency_injection_hilt_basics"]
                },
                {
                    "signal": "Refactored monolithic Android codebase into 20+ feature and core modules",
                    "strength": 0.9,
                    "maps_to": ["android_architecture_patterns.modularization_multi_module", "android_architecture_patterns.advanced_di_scopes_modules"]
                },
                {
                    "signal": "Reduced cold start time by 40% using App Startup and Baseline Profiles",
                    "strength": 0.9,
                    "maps_to": ["android_architecture_patterns.app_startup_architecture", "android_architecture_patterns.navigation_component_compose"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Android Architecture, Clean Architecture, or Hilt endorsed",
                    "strength": 0.5,
                    "maps_to": ["android_architecture_patterns.mvvm_architecture_pattern", "android_architecture_patterns.dependency_injection_hilt_basics"]
                },
                {
                    "signal": "Job experience describing multi-module modularization, MVI architecture, or baseline profile optimizations",
                    "strength": 0.8,
                    "maps_to": ["android_architecture_patterns.modularization_multi_module", "android_architecture_patterns.mvi_unidirectional_data_flow", "android_architecture_patterns.app_startup_architecture"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["mvvm_architecture_pattern", "dependency_injection_hilt_basics", "repository_pattern_data_sources"],
                "description": "Applies MVVM architecture with ViewModels, injects dependencies using Hilt, and implements the Repository pattern with remote/local data sources."
            },
            "mid": {
                "expected_subskills": ["clean_architecture_domain_layer", "mvi_unidirectional_data_flow", "advanced_di_scopes_modules"],
                "description": "Structures domain layers with Clean Architecture UseCases, implements MVI unidirectional data flow, and configures custom Hilt scopes and multibindings."
            },
            "senior": {
                "expected_subskills": ["modularization_multi_module", "navigation_component_compose", "app_startup_architecture"],
                "description": "Architects multi-module codebases, designs type-safe navigation graphs, and optimizes application cold startup with Baseline Profiles."
            }
        }
    },
    {
        "skill_id": "android_data_persistence",
        "name": "Android Data Persistence, Offline Sync & Networking",
        "category": "mobile_core",
        "description": f"Client-side data persistence, offline synchronization, and RESTful API consumption in Android applications. IMPORTANT DISTINCTION: {CRITICAL_NOTE} Covers DataStore (Preferences & Proto), Room ORM (entities, DAOs, migrations, Paging 3), Retrofit/OkHttp client consumption, Android KeyStore encryption, and SQLite query optimization.",
        "subskills": [
            {
                "id": "datastore_preferences_preferences",
                "name": "Jetpack DataStore (Preferences & Proto)",
                "description": "Replacing SharedPreferences with Jetpack DataStore — implementing Preferences DataStore for simple key-value pairs and Proto DataStore with Protocol Buffers for type-safe structured persistence, handling migration from SharedPreferences, and observing updates via Flow.",
                "keywords": ["Preferences DataStore", "Proto DataStore", "SharedPreferences migration", "Protocol Buffers DataStore", "DataStore Flow", "edit { preferences -> }"]
            },
            {
                "id": "room_database_fundamentals",
                "name": "Room Database & DAO Fundamentals",
                "description": "Implementing local relational storage with Android Jetpack Room ORM — modeling @Entity tables, writing Data Access Objects (@Dao) with type-safe @Query / @Insert / @Update / @Delete, primary keys, autoGenerate, TypeConverters, and returning Flow<List<T>>.",
                "keywords": ["Room ORM", "@Entity", "@Dao", "@Database", "@TypeConverter", "Room with Flow", "@Query SQLite", "Room database builder"]
            },
            {
                "id": "retrofit_networking_client",
                "name": "Retrofit Client & HTTP Consumption",
                "description": "Consuming REST APIs on Android using Retrofit2 and OkHttp — configuring BaseUrl, ConverterFactory (Kotlinx.serialization, Moshi, Gson), OkHttp logging/auth interceptors, defining GET/POST/PUT endpoints with suspend functions, and HTTP error handling.",
                "keywords": ["Retrofit2", "OkHttp Interceptors", "Kotlinx.serialization", "Moshi", "HttpLoggingInterceptor", "AuthInterceptor", "REST API consumption Android"]
            },
            {
                "id": "room_relations_migrations",
                "name": "Room Relations & Database Migrations",
                "description": "Modeling complex relational data in Room using @Embedded, @Relation (one-to-one, one-to-many, many-to-many via junction entities), writing automated and manual database Migrations (Migration(1, 2)), and testing database migrations with MigrationTestHelper.",
                "keywords": ["Room @Relation", "Room @Embedded", "Junction table Room", "Room Migrations", "MigrationTestHelper", "AutoMigration", "foreignKeys constraint"]
            },
            {
                "id": "offline_first_synchronization",
                "name": "Offline-First Repository & Sync Engine",
                "description": "Architecting offline-first Android applications — Room as the single source of truth, synchronizing remote API data to local database, conflict resolution policies (server-wins vs client-wins), optimistic UI updates, and handling offline sync queues.",
                "keywords": ["offline-first architecture", "offline sync engine", "conflict resolution", "optimistic UI updates", "NetworkBoundResource pattern", "sync queue"]
            },
            {
                "id": "encrypted_storage_keystore",
                "name": "Android KeyStore & Encrypted Data Storage",
                "description": "Securing sensitive client data using Android KeyStore system for hardware-backed cryptographic key generation (AES/GCM, RSA), utilizing EncryptedSharedPreferences and EncryptedFile (Jetpack Security / crypto library), and integrating BiometricPrompt crypto authentication.",
                "keywords": ["Android KeyStore", "EncryptedSharedPreferences", "EncryptedFile", "Jetpack Security", "hardware-backed keys (TEE/StrongBox)", "BiometricPrompt CryptoObject", "AES-256 GCM"]
            },
            {
                "id": "room_paging3_integration",
                "name": "Room Paging 3 & RemoteMediator",
                "description": "Implementing infinite scrolling lists with Paging 3 and Room database — authoring custom RemoteMediator to orchestrate network pagination and local database caching, managing PagingSource, handling boundary conditions (LoadType.REFRESH, PREPEND, APPEND).",
                "keywords": ["Paging 3 library", "RemoteMediator", "PagingSource", "PagingData Flow", "LoadState handling", "database + network pagination", "RemoteKeys entity"]
            },
            {
                "id": "sqlite_advanced_indexing",
                "name": "SQLite Optimization, Indexing & FTS5",
                "description": "Optimizing SQLite database performance in Room — designing composite indexes (@Index), configuring Write-Ahead Logging (WAL mode), utilizing SQLite Full-Text Search (FTS4 / FTS5) with @Fts4/@Fts5 entities, analyzing SQLite EXPLAIN QUERY PLAN, and transaction batching.",
                "keywords": ["Room @Index", "SQLite EXPLAIN QUERY PLAN", "Write-Ahead Logging (WAL)", "Full-Text Search (@Fts5)", "SQLite composite index", "transaction batching (@Transaction)"]
            },
            {
                "id": "network_resilience_caching",
                "name": "Network Resilience, Caching & Certificate Pinning",
                "description": "Engineering client-side network resilience — configuring OkHttp response Cache with Cache-Control directives, implementing exponential retry interceptors with jitter, certificate pinning via CertificatePinner to prevent MitM attacks, and handling network bandwidth adaptation.",
                "keywords": ["OkHttp Cache-Control", "CertificatePinner / SSL Pinning", "exponential backoff interceptor", "network resilience", "MitM protection", "stale-while-revalidate client"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Room Database entity, DAO, and database builder code",
                    "detection": "content_analysis",
                    "pattern": "@Database\\(entities =|@Dao|@Entity|Room\\.databaseBuilder",
                    "strength": 0.8,
                    "maps_to": ["android_data_persistence.room_database_fundamentals", "android_data_persistence.room_relations_migrations"]
                },
                {
                    "signal": "Retrofit API interface and OkHttp client configuration",
                    "detection": "content_analysis",
                    "pattern": "Retrofit\\.Builder|@GET\\(\"|@POST\\(\"|OkHttpClient\\.Builder|addInterceptor",
                    "strength": 0.8,
                    "maps_to": ["android_data_persistence.retrofit_networking_client", "android_data_persistence.network_resilience_caching"]
                },
                {
                    "signal": "Jetpack DataStore Preferences or Proto implementation",
                    "detection": "content_analysis",
                    "pattern": "preferencesDataStore|ProtoDataStore|DataStore<Preferences>|edit \\{ prefs ->",
                    "strength": 0.8,
                    "maps_to": ["android_data_persistence.datastore_preferences_preferences"]
                },
                {
                    "signal": "Paging 3 RemoteMediator implementation",
                    "detection": "content_analysis",
                    "pattern": ": RemoteMediator<.*,.*>|LoadType\\.REFRESH|PagingData",
                    "strength": 0.9,
                    "maps_to": ["android_data_persistence.room_paging3_integration"]
                },
                {
                    "signal": "Android KeyStore or EncryptedSharedPreferences implementation",
                    "detection": "content_analysis",
                    "pattern": "KeyStore\\.getInstance\\(\"AndroidKeyStore\"\\)|EncryptedSharedPreferences|MasterKey\\.Builder",
                    "strength": 0.9,
                    "maps_to": ["android_data_persistence.encrypted_storage_keystore"]
                }
            ],
            "cv": [
                {
                    "signal": "Architected offline-first Android apps using Room ORM, Retrofit, and Paging 3",
                    "strength": 0.8,
                    "maps_to": ["android_data_persistence.room_database_fundamentals", "android_data_persistence.offline_first_synchronization", "android_data_persistence.room_paging3_integration"]
                },
                {
                    "signal": "Implemented secure credential storage with Android KeyStore and SSL Pinning",
                    "strength": 0.9,
                    "maps_to": ["android_data_persistence.encrypted_storage_keystore", "android_data_persistence.network_resilience_caching"]
                },
                {
                    "signal": "Optimized local SQLite database with FTS5 search and automated Room migrations",
                    "strength": 0.9,
                    "maps_to": ["android_data_persistence.sqlite_advanced_indexing", "android_data_persistence.room_relations_migrations"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Room Database, Retrofit, or Android Storage endorsed",
                    "strength": 0.5,
                    "maps_to": ["android_data_persistence.room_database_fundamentals", "android_data_persistence.retrofit_networking_client"]
                },
                {
                    "signal": "Job experience describing offline sync engines, Room migrations, or KeyStore encryption",
                    "strength": 0.8,
                    "maps_to": ["android_data_persistence.offline_first_synchronization", "android_data_persistence.encrypted_storage_keystore", "android_data_persistence.room_paging3_integration"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["datastore_preferences_preferences", "room_database_fundamentals", "retrofit_networking_client"],
                "description": "Stores key-value data with DataStore, models local Room tables with basic DAOs, and consumes REST APIs using Retrofit."
            },
            "mid": {
                "expected_subskills": ["room_relations_migrations", "offline_first_synchronization", "encrypted_storage_keystore"],
                "description": "Handles Room relational queries and schema migrations, builds offline-first sync repositories, and secures credentials using KeyStore."
            },
            "senior": {
                "expected_subskills": ["room_paging3_integration", "sqlite_advanced_indexing", "network_resilience_caching"],
                "description": "Implements Paging 3 RemoteMediator for local+remote pagination, tunes SQLite indexes and FTS5 search, and enforces SSL pinning with retry resilience."
            }
        }
    },
    {
        "skill_id": "android_concurrency_async",
        "name": "Kotlin Coroutines, Asynchronous Flow & Concurrency",
        "category": "mobile_core",
        "description": "Mastering asynchronous and reactive programming on Android using Kotlin Coroutines and Kotlin Flow. Covers structured concurrency, Dispatchers, cold vs hot streams (StateFlow, SharedFlow), flow transformations, thread synchronization primitives, lifecycle-aware flow collection, and coroutine unit testing.",
        "subskills": [
            {
                "id": "coroutines_basics_dispatchers",
                "name": "Coroutines Fundamentals & Dispatchers",
                "description": "Launching coroutines with launch and async builders, switching execution contexts using CoroutineDispatchers (Dispatchers.Main, Dispatchers.IO, Dispatchers.Default, Dispatchers.Unconfined), and writing non-blocking suspend functions.",
                "keywords": ["Kotlin Coroutines", "CoroutineDispatchers (Main/IO/Default)", "suspend functions", "coroutine builders (launch/async)", "withContext", "non-blocking execution"]
            },
            {
                "id": "structured_concurrency_jobs",
                "name": "Structured Concurrency & Cancellation Propagation",
                "description": "Enforcing structured concurrency principles — managing Job hierarchies, parent-child cancellation propagation, handling non-cancellable blocks with withContext(NonCancellable), and isolating coroutine failures using supervisorScope and SupervisorJob.",
                "keywords": ["Structured Concurrency", "Job hierarchy", "CancellationException", "NonCancellable", "supervisorScope", "SupervisorJob", "CoroutineExceptionHandler"]
            },
            {
                "id": "flow_fundamentals_cold_streams",
                "name": "Cold Kotlin Flow Fundamentals",
                "description": "Creating and consuming cold asynchronous streams using Kotlin Flow — flow { ... } builders, flowOf, asFlow, applying intermediate operators (map, filter, take, onEach), terminal operators (collect, toList, first), and exception handling with catch.",
                "keywords": ["Kotlin Flow", "cold streams", "flow builder", "flow operators (map/filter/onEach)", "terminal operators (collect/first)", "flow catch exception", "flowOn dispatcher"]
            },
            {
                "id": "stateflow_sharedflow_hot_streams",
                "name": "Hot Streams: StateFlow & SharedFlow",
                "description": "Managing hot reactive streams in Android — utilizing StateFlow for UI state representation, SharedFlow for one-shot broadcast events, configuring replay cache, buffer overflow strategies (BufferOverflow.DROP_OLDEST), and converting cold flows with stateIn/shareIn and SharingStarted policies.",
                "keywords": ["StateFlow", "SharedFlow", "hot streams", "stateIn / shareIn", "SharingStarted.WhileSubscribed(5000)", "replay cache", "BufferOverflow strategy"]
            },
            {
                "id": "flow_transformations_combination",
                "name": "Advanced Flow Operators & Stream Combination",
                "description": "Composing complex reactive pipelines with advanced Flow operators: flatMapLatest vs flatMapMerge vs flatMapConcat, combining streams with combine and zip, search debouncing with debounce and distinctUntilChanged, and flow retries with retryWhen.",
                "keywords": ["flatMapLatest", "flatMapMerge", "combine / zip Flow", "debounce search", "distinctUntilChanged", "retryWhen / retry backoff", "Flow composition"]
            },
            {
                "id": "concurrency_synchronization_primitives",
                "name": "Concurrency Primitives, Mutex & Channels",
                "description": "Managing shared mutable state across coroutines safely — utilizing Mutex (withLock) for mutual exclusion without thread blocking, Semaphore for concurrency throttling, Channel (Buffered, Rendezvous, Conflated) for producer-consumer communication, and Atomic primitives.",
                "keywords": ["Mutex withLock", "Semaphore", "Channel (Buffered/Conflated/Rendezvous)", "shared mutable state", "AtomicInteger / AtomicReference", "producer-consumer pattern"]
            },
            {
                "id": "coroutine_memory_leaks_profiling",
                "name": "Lifecycle-Aware Flow Collection & Leak Prevention",
                "description": "Safely collecting Flows in Android UI components — using repeatOnLifecycle and flowWithLifecycle to automatically pause collection when the UI is stopped, preventing background resource leaks, and diagnosing coroutine leaks with Android Studio Profiler.",
                "keywords": ["repeatOnLifecycle", "flowWithLifecycle", "lifecycleScope.launch", "coroutine leak prevention", "background collection pause", "Memory Profiler coroutines"]
            },
            {
                "id": "reactive_streams_rxjava_migration",
                "name": "RxJava to Coroutines/Flow Interoperability & Migration",
                "description": "Interoperating between RxJava (Observable, Single, Flowable, Completable) and Kotlin Coroutines/Flow using kotlinx-coroutines-rx2/rx3, migrating legacy reactive codebases to native Coroutines, and comparing backpressure models.",
                "keywords": ["RxJava to Coroutines migration", "asFlow / asObservable", "awaitSingle", "kotlinx-coroutines-rx3", "RxJava Flowable vs Kotlin Flow", "reactive interop"]
            },
            {
                "id": "custom_coroutine_context_testing",
                "name": "Coroutine Testing with TestDispatcher & Turbine",
                "description": "Testing asynchronous coroutine and Flow code deterministically — utilizing StandardTestDispatcher and UnconfinedTestDispatcher with runTest, controlling virtual time with advanceTimeBy and advanceUntilIdle, and asserting Flow emissions using the Turbine library.",
                "keywords": ["runTest", "StandardTestDispatcher", "UnconfinedTestDispatcher", "advanceUntilIdle / advanceTimeBy", "Turbine library (test { awaitItem() })", "MainDispatcherRule"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Kotlin Flow and Coroutine usage in ViewModels or Repositories",
                    "detection": "content_analysis",
                    "pattern": "MutableStateFlow|MutableSharedFlow|stateIn\\(|viewModelScope\\.launch|withContext\\(Dispatchers\\.",
                    "strength": 0.8,
                    "maps_to": ["android_concurrency_async.coroutines_basics_dispatchers", "android_concurrency_async.stateflow_sharedflow_hot_streams"]
                },
                {
                    "signal": "Lifecycle-aware flow collection with repeatOnLifecycle",
                    "detection": "content_analysis",
                    "pattern": "repeatOnLifecycle\\(Lifecycle\\.State|flowWithLifecycle\\(",
                    "strength": 0.9,
                    "maps_to": ["android_concurrency_async.coroutine_memory_leaks_profiling"]
                },
                {
                    "signal": "Advanced Flow operators (flatMapLatest, combine, debounce)",
                    "detection": "content_analysis",
                    "pattern": "\\.flatMapLatest|\\.combine\\(|\\.debounce\\(|\\.distinctUntilChanged",
                    "strength": 0.8,
                    "maps_to": ["android_concurrency_async.flow_transformations_combination"]
                },
                {
                    "signal": "Coroutine testing with runTest and Turbine library",
                    "detection": "content_analysis",
                    "pattern": "runTest \\{|\\.test \\{.*awaitItem|StandardTestDispatcher|advanceUntilIdle",
                    "strength": 0.9,
                    "maps_to": ["android_concurrency_async.custom_coroutine_context_testing"]
                },
                {
                    "signal": "Mutex or Channel concurrency primitive usage",
                    "detection": "content_analysis",
                    "pattern": "Mutex\\(\\)|\\.withLock \\{|Channel<.*>\\(|Channel\\.BUFFERED",
                    "strength": 0.8,
                    "maps_to": ["android_concurrency_async.concurrency_synchronization_primitives"]
                }
            ],
            "cv": [
                {
                    "signal": "Engineered reactive Android data flows using Kotlin Flow, StateFlow, and Coroutines",
                    "strength": 0.8,
                    "maps_to": ["android_concurrency_async.coroutines_basics_dispatchers", "android_concurrency_async.stateflow_sharedflow_hot_streams", "android_concurrency_async.flow_transformations_combination"]
                },
                {
                    "signal": "Migrated legacy RxJava2/3 codebase to Kotlin Coroutines and Flow",
                    "strength": 0.9,
                    "maps_to": ["android_concurrency_async.reactive_streams_rxjava_migration", "android_concurrency_async.coroutine_memory_leaks_profiling"]
                },
                {
                    "signal": "Authored comprehensive asynchronous unit test suites using Turbine and runTest",
                    "strength": 0.8,
                    "maps_to": ["android_concurrency_async.custom_coroutine_context_testing", "android_concurrency_async.structured_concurrency_jobs"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Kotlin Coroutines, Reactive Programming, or Asynchronous Programming endorsed",
                    "strength": 0.5,
                    "maps_to": ["android_concurrency_async.coroutines_basics_dispatchers", "android_concurrency_async.flow_fundamentals_cold_streams"]
                },
                {
                    "signal": "Job experience describing complex Flow pipelines, repeatOnLifecycle leak prevention, or Coroutines migration",
                    "strength": 0.8,
                    "maps_to": ["android_concurrency_async.coroutine_memory_leaks_profiling", "android_concurrency_async.flow_transformations_combination", "android_concurrency_async.custom_coroutine_context_testing"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["coroutines_basics_dispatchers", "structured_concurrency_jobs", "flow_fundamentals_cold_streams"],
                "description": "Launches coroutines with appropriate Dispatchers, adheres to structured concurrency, and consumes cold Flows with basic operators."
            },
            "mid": {
                "expected_subskills": ["stateflow_sharedflow_hot_streams", "flow_transformations_combination", "concurrency_synchronization_primitives"],
                "description": "Exposes UI state using StateFlow/SharedFlow, builds complex Flow combination pipelines, and coordinates coroutines with Mutex and Channels."
            },
            "senior": {
                "expected_subskills": ["coroutine_memory_leaks_profiling", "reactive_streams_rxjava_migration", "custom_coroutine_context_testing"],
                "description": "Prevents memory leaks with lifecycle-aware collection, leads RxJava-to-Flow migrations, and tests async pipelines deterministically with virtual time."
            }
        }
    },
    {
        "skill_id": "android_platform_services_quality",
        "name": "Android Platform Services, Quality, CI/CD & Security",
        "category": "mobile_core",
        "description": "Android hardware and platform services integration, automated testing (Unit, UI, Compose), memory leak analysis with LeakCanary, CI/CD Gradle build pipelines with R8/ProGuard, crash observability, and device security hardening (Play Integrity).",
        "subskills": [
            {
                "id": "runtime_permissions_model",
                "name": "Runtime Permissions & Privacy Sandbox",
                "description": "Implementing Android runtime permission workflows (normal vs dangerous permissions, special permissions), requesting permissions via ActivityResultContracts.RequestPermission, displaying rationale dialogs, handling 'Don't ask again', and adapting to Privacy Sandbox changes.",
                "keywords": ["Runtime Permissions", "ActivityResultContracts.RequestPermission", "shouldShowRequestPermissionRationale", "POST_NOTIFICATIONS (Android 13)", "Photo Picker privacy", "Privacy Sandbox"]
            },
            {
                "id": "unit_testing_mockk_junit5",
                "name": "Unit Testing with JUnit5, MockK & Kotest",
                "description": "Writing comprehensive unit tests for ViewModels, Repositories, and UseCases using JUnit5 / JUnit4, mocking dependencies with MockK (coEvery, coVerify, relaxed mocks), testing state transitions, and structuring test cases cleanly.",
                "keywords": ["Unit testing Android", "MockK (coEvery/coVerify)", "JUnit5 / JUnit4", "ViewModel unit testing", "relaxed mocks", "test assertions"]
            },
            {
                "id": "notifications_channels_manager",
                "name": "Notification Channels & System Notifications",
                "description": "Designing notification experiences using NotificationManagerCompat and NotificationCompat.Builder — configuring NotificationChannels (importance levels, sound, vibration), building rich expandable styles (BigTextStyle, BigPictureStyle, MessagingStyle), PendingIntent flags (FLAG_IMMUTABLE), and action buttons.",
                "keywords": ["NotificationChannel", "NotificationCompat.Builder", "NotificationManagerCompat", "PendingIntent.FLAG_IMMUTABLE", "BigTextStyle / MessagingStyle", "notification priority"]
            },
            {
                "id": "espresso_ui_testing",
                "name": "UI Testing with Espresso & Compose Test Rules",
                "description": "Writing automated UI tests using Espresso (onView, withId, withText, perform(click()), check(matches(isDisplayed()))) and Jetpack Compose Testing API (createComposeRule, onNodeWithText, performClick, assertIsDisplayed), and managing IdlingResources for async UI synchronization.",
                "keywords": ["Espresso UI testing", "createComposeRule / createAndroidComposeRule", "onNodeWithText / onNodeWithTag", "IdlingResource", "UI test assertions", "UI Automator"]
            },
            {
                "id": "location_camera_hardware_services",
                "name": "Hardware Services (CameraX, Location & Sensors)",
                "description": "Integrating Android hardware capabilities — capturing photos and video with CameraX API (Preview, ImageCapture, ImageAnalysis), tracking precise/approximate device location with FusedLocationProviderClient and LocationRequest, and reading hardware Sensors.",
                "keywords": ["CameraX API (ImageCapture/ImageAnalysis)", "FusedLocationProviderClient", "LocationRequest (PRIORITY_HIGH_ACCURACY)", "approximate vs precise location", "SensorManager", "BiometricPrompt"]
            },
            {
                "id": "memory_leak_detection_leakcanary",
                "name": "Memory Leak Detection & LeakCanary Analysis",
                "description": "Detecting and resolving Android memory leaks — integrating LeakCanary, analyzing heap dumps (HPROF), tracing retain reference chains back to GC roots (static views, inner class handlers, leaked Activity contexts), and optimizing Bitmap memory footprint.",
                "keywords": ["LeakCanary", "Memory leak detection", "Heap dump (.hprof) analysis", "GC root retain chain", "leaked Activity context", "Bitmap memory optimization (inSampleSize)"]
            },
            {
                "id": "ci_cd_gradle_build_optimization",
                "name": "Gradle CI/CD & Build Speed Optimization",
                "description": "Architecting automated CI/CD build pipelines for Android (GitHub Actions, Bitrise, GitLab CI) — optimizing Gradle build times with Build Cache, Configuration Cache, and Gradle daemon tuning, generating signed Android App Bundles (.aab), and deploying to Play Store tracks.",
                "keywords": ["Android CI/CD", "Gradle Build Cache", "Gradle Configuration Cache", "Android App Bundle (.aab)", "Fastlane Android", "Play Store track deployment (Internal/Alpha/Production)"]
            },
            {
                "id": "crash_reporting_observability",
                "name": "Crash Reporting, ANR Diagnostics & App Vitals",
                "description": "Monitoring application production health — integrating Firebase Crashlytics with custom keys and non-fatal logging, diagnosing Application Not Responding (ANR) trace files, tracking Google Play Android Vitals (crash rate, excessive wakeups, slow rendering).",
                "keywords": ["Firebase Crashlytics", "custom keys & logs", "ANR diagnostics (traces.txt)", "Google Play Android Vitals", "non-fatal exception tracking", "real-time observability"]
            },
            {
                "id": "security_obfuscation_tamper_proofing",
                "name": "R8 Code Shrinking & Play Integrity Hardening",
                "description": "Hardening Android application security — authoring custom ProGuard/R8 rules for code shrinking and obfuscation without breaking reflection/serialization, integrating Google Play Integrity API to verify app genuineness, detecting rooted devices, and verifying APK signature schemes (v2/v3/v4).",
                "keywords": ["R8 / ProGuard rules", "code obfuscation & shrinking", "Google Play Integrity API", "root detection", "APK signature scheme (v2/v3/v4)", "tamper proofing", "reverse engineering protection"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Unit tests using MockK and JUnit for ViewModels or repositories",
                    "detection": "content_analysis",
                    "pattern": "@Test|mockk<|coEvery \\{|coVerify \\{|assertk|assert\\(",
                    "strength": 0.8,
                    "maps_to": ["android_platform_services_quality.unit_testing_mockk_junit5"]
                },
                {
                    "signal": "Espresso or Compose UI test implementations",
                    "detection": "content_analysis",
                    "pattern": "onView\\(withId|createComposeRule\\(\\)|onNodeWithTag|onNodeWithText",
                    "strength": 0.8,
                    "maps_to": ["android_platform_services_quality.espresso_ui_testing"]
                },
                {
                    "signal": "ProGuard or R8 rules configuration files",
                    "detection": "file_presence",
                    "pattern": "proguard-rules\\.pro|consumer-rules\\.pro|proguard-android-optimize\\.txt",
                    "strength": 0.9,
                    "maps_to": ["android_platform_services_quality.security_obfuscation_tamper_proofing"]
                },
                {
                    "signal": "CameraX or Location Services integration",
                    "detection": "content_analysis",
                    "pattern": "ProcessCameraProvider|ImageCapture\\.Builder|FusedLocationProviderClient|LocationServices",
                    "strength": 0.8,
                    "maps_to": ["android_platform_services_quality.location_camera_hardware_services"]
                },
                {
                    "signal": "Firebase Crashlytics or LeakCanary dependencies and setup",
                    "detection": "content_analysis",
                    "pattern": "com\\.google\\.firebase:firebase-crashlytics|com\\.squareup\\.leakcanary:leakcanary-android|FirebaseCrashlytics\\.getInstance",
                    "strength": 0.8,
                    "maps_to": ["android_platform_services_quality.crash_reporting_observability", "android_platform_services_quality.memory_leak_detection_leakcanary"]
                }
            ],
            "cv": [
                {
                    "signal": "Built automated testing suites with JUnit, MockK, Espresso, and Compose Test",
                    "strength": 0.8,
                    "maps_to": ["android_platform_services_quality.unit_testing_mockk_junit5", "android_platform_services_quality.espresso_ui_testing"]
                },
                {
                    "signal": "Optimized Gradle CI/CD pipelines and published App Bundles to Google Play",
                    "strength": 0.8,
                    "maps_to": ["android_platform_services_quality.ci_cd_gradle_build_optimization", "android_platform_services_quality.crash_reporting_observability"]
                },
                {
                    "signal": "Hardened application security with R8 obfuscation and Play Integrity API",
                    "strength": 0.9,
                    "maps_to": ["android_platform_services_quality.security_obfuscation_tamper_proofing", "android_platform_services_quality.memory_leak_detection_leakcanary"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Android Testing, Gradle, or Mobile Security endorsed",
                    "strength": 0.5,
                    "maps_to": ["android_platform_services_quality.unit_testing_mockk_junit5", "android_platform_services_quality.ci_cd_gradle_build_optimization"]
                },
                {
                    "signal": "Job experience describing CI/CD automation, LeakCanary memory tuning, or R8 obfuscation",
                    "strength": 0.8,
                    "maps_to": ["android_platform_services_quality.ci_cd_gradle_build_optimization", "android_platform_services_quality.memory_leak_detection_leakcanary", "android_platform_services_quality.security_obfuscation_tamper_proofing"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["runtime_permissions_model", "unit_testing_mockk_junit5", "notifications_channels_manager"],
                "description": "Requests runtime permissions cleanly, writes unit tests with MockK, and implements notification channels."
            },
            "mid": {
                "expected_subskills": ["espresso_ui_testing", "location_camera_hardware_services", "memory_leak_detection_leakcanary"],
                "description": "Writes automated UI tests with Espresso/Compose, integrates CameraX and location services, and debugs memory leaks using LeakCanary."
            },
            "senior": {
                "expected_subskills": ["ci_cd_gradle_build_optimization", "crash_reporting_observability", "security_obfuscation_tamper_proofing"],
                "description": "Optimizes Gradle CI/CD build caches, monitors production health and ANRs via Crashlytics, and hardens apps with R8 and Play Integrity."
            }
        }
    }
]

# Write all 7 Android skill files
for skill in android_skills:
    file_path = os.path.join(base_dir, 'skills', 'android', f"{skill['skill_id']}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(skill, f, indent=2, ensure_ascii=False)
    print(f"Written skill: {skill['skill_id']}.json")

# -------------------------------------------------------------
# 2. Android Roles Definition
# -------------------------------------------------------------
roles = {
    "junior": {
        "role_id": "android_developer",
        "level": "junior",
        "title": "Junior Android Developer",
        "description": "Entry-level Android developer focused on Kotlin language fundamentals, Activity/Fragment lifecycles, Jetpack Compose UI basics with XML ViewBinding, basic MVVM architecture with Hilt dependency injection, Room database CRUD, and unit testing with MockK.",
        "experience_range": "0-2 years",
        "skills": [
            {
                "skill_id": "android_fundamentals_kotlin",
                "importance": 0.95,
                "rationale": "Strong foundation in Kotlin null safety, scope functions, and Android SDK Context hierarchy is essential for daily feature delivery."
            },
            {
                "skill_id": "android_ui_layouts",
                "importance": 0.95,
                "rationale": "Building layouts in Compose and XML ConstraintLayout, implementing RecyclerView with ListAdapter and DiffUtil."
            },
            {
                "skill_id": "android_app_components",
                "importance": 0.9,
                "rationale": "Proper handling of Activity and Fragment lifecycles, state preservation across configuration changes, and Intent navigation."
            },
            {
                "skill_id": "android_architecture_patterns",
                "importance": 0.85,
                "rationale": "Adhering to MVVM pattern, injecting dependencies with Hilt, and organizing data access through repositories."
            },
            {
                "skill_id": "android_data_persistence",
                "importance": 0.8,
                "rationale": "Querying local SQLite with Room ORM, storing preferences in DataStore, and consuming REST APIs with Retrofit."
            },
            {
                "skill_id": "android_concurrency_async",
                "importance": 0.8,
                "rationale": "Launching coroutines on appropriate Dispatchers and adhering to structured concurrency without blocking the main thread."
            },
            {
                "skill_id": "android_platform_services_quality",
                "importance": 0.7,
                "rationale": "Requesting runtime permissions, writing ViewModel unit tests with MockK, and creating notification channels."
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
                    "description": "Significant gaps in Kotlin fundamentals, Android lifecycles, or UI layout construction."
                },
                "developing": {
                    "min": 0.3,
                    "max": 0.5,
                    "label": "Developing",
                    "description": "Basic understanding of Views and Activities, but requires guidance on Compose state hoisting, Hilt DI, and Coroutines."
                },
                "approaching": {
                    "min": 0.5,
                    "max": 0.7,
                    "label": "Approaching Ready",
                    "description": "Solid Kotlin fundamentals, reliable MVVM implementation, consistent unit testing habits, and clean Compose UI code."
                },
                "ready": {
                    "min": 0.7,
                    "max": 0.85,
                    "label": "Ready",
                    "description": "Meets all junior expectations: delivers robust, tested Android features with Room, Retrofit, Compose, and Hilt."
                },
                "exceeds": {
                    "min": 0.85,
                    "max": 1.0,
                    "label": "Exceeds Expectations",
                    "description": "Exceeds junior expectations with early mid-level proficiency in offline sync, StateFlow pipelines, and WorkManager."
                }
            }
        }
    },
    "mid": {
        "role_id": "android_developer",
        "level": "mid",
        "title": "Mid-level Android Developer",
        "description": "Mid-level Android engineer capable of independently architecting complex features using Clean Architecture and MVI, implementing offline-first sync engines, managing foreground services and WorkManager tasks, optimizing Compose side-effects, and building automated Espresso/Compose test suites.",
        "experience_range": "2-5 years",
        "skills": [
            {
                "skill_id": "android_architecture_patterns",
                "importance": 0.95,
                "rationale": "Structuring domain layers with Clean Architecture UseCases, implementing MVI unidirectional data flow, and managing complex Hilt component scopes."
            },
            {
                "skill_id": "android_data_persistence",
                "importance": 0.95,
                "rationale": "Managing Room relational models and migrations, architecting offline-first sync repositories, and securing credentials in Android KeyStore."
            },
            {
                "skill_id": "android_concurrency_async",
                "importance": 0.9,
                "rationale": "Exposing UI state with StateFlow/SharedFlow, combining complex reactive streams, and coordinating concurrency with Mutex and Channels."
            },
            {
                "skill_id": "android_ui_layouts",
                "importance": 0.9,
                "rationale": "Handling Compose side-effects with LaunchedEffect/DisposableEffect, building custom 2D Canvas views, and managing Lazy collections."
            },
            {
                "skill_id": "android_app_components",
                "importance": 0.85,
                "rationale": "Implementing background processing with WorkManager, designing foreground services under modern Android restrictions, and FileProvider sharing."
            },
            {
                "skill_id": "android_fundamentals_kotlin",
                "importance": 0.85,
                "rationale": "Leveraging generics variance, creating custom property delegates, and maintaining type-safe Gradle build scripts."
            },
            {
                "skill_id": "android_platform_services_quality",
                "importance": 0.8,
                "rationale": "Writing automated UI tests with Espresso/Compose, integrating CameraX and location services, and diagnosing memory leaks with LeakCanary."
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
                    "description": "Significant gaps in Android architecture, reactive Flow pipelines, or background processing."
                },
                "developing": {
                    "min": 0.3,
                    "max": 0.5,
                    "label": "Developing",
                    "description": "Competent with basic MVVM, but struggles with offline-first synchronization, complex Flow transformations, or custom View drawing."
                },
                "approaching": {
                    "min": 0.5,
                    "max": 0.7,
                    "label": "Approaching Ready",
                    "description": "Strong systems grasp, independent feature delivery, solid Clean Architecture implementation, and proactive memory leak hunting."
                },
                "ready": {
                    "min": 0.7,
                    "max": 0.85,
                    "label": "Ready",
                    "description": "Meets all mid-level expectations: delivers offline-first apps, designs clean MVI/Clean Architecture layers, and debugs complex concurrency."
                },
                "exceeds": {
                    "min": 0.85,
                    "max": 1.0,
                    "label": "Exceeds Expectations",
                    "description": "Exceeds mid-level expectations with advanced multi-module architecture, KMP contributions, and performance profiling expertise."
                }
            }
        }
    },
    "senior": {
        "role_id": "android_developer",
        "level": "senior",
        "title": "Senior Android Developer",
        "description": "Senior Android engineer and mobile platform architect responsible for multi-module codebases, Kotlin Multiplatform (KMP) shared modules, Compose compiler stability and recomposition tuning, 120fps UI rendering pipelines, multi-process IPC with AIDL/Binder, Gradle CI/CD build cache optimization, R8 code obfuscation, and Play Integrity security hardening.",
        "experience_range": "5+ years",
        "skills": [
            {
                "skill_id": "android_architecture_patterns",
                "importance": 0.95,
                "rationale": "Architecting multi-module codebases, type-safe Navigation Compose graphs, and cold startup optimization with Baseline Profiles."
            },
            {
                "skill_id": "android_ui_layouts",
                "importance": 0.95,
                "rationale": "Tuning Compose compiler stability metrics, eliminating recompositions, architecting Material 3 design systems, and 120fps frame profiling."
            },
            {
                "skill_id": "android_concurrency_async",
                "importance": 0.9,
                "rationale": "Preventing memory leaks with lifecycle-aware collection, leading RxJava-to-Flow migrations, and testing async code with virtual time."
            },
            {
                "skill_id": "android_platform_services_quality",
                "importance": 0.9,
                "rationale": "Optimizing Gradle CI/CD build caches, monitoring production health/ANRs via Crashlytics, and hardening security with R8 and Play Integrity."
            },
            {
                "skill_id": "android_data_persistence",
                "importance": 0.85,
                "rationale": "Implementing Paging 3 RemoteMediator, optimizing SQLite indexes and FTS5 search, and enforcing SSL certificate pinning."
            },
            {
                "skill_id": "android_fundamentals_kotlin",
                "importance": 0.85,
                "rationale": "Building KSP annotation processors, analyzing decompiled bytecode for memory optimization, and architecting Kotlin Multiplatform (KMP) shared modules."
            },
            {
                "skill_id": "android_app_components",
                "importance": 0.85,
                "rationale": "Designing multi-process IPC with AIDL/Binder, engineering LMK process death survival, and configuring verified Android App Links."
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
                    "description": "Significant gaps in multi-module architecture, performance profiling, or mobile platform security."
                },
                "developing": {
                    "min": 0.3,
                    "max": 0.5,
                    "label": "Developing",
                    "description": "Solid mid-level feature delivery, but lacks experience in modularization strategies, Compose compiler optimization, and CI/CD pipelines."
                },
                "approaching": {
                    "min": 0.5,
                    "max": 0.7,
                    "label": "Approaching Ready",
                    "description": "Strong architectural capabilities; refining expertise in Baseline Profiles, KMP, and advanced R8 obfuscation rules."
                },
                "ready": {
                    "min": 0.7,
                    "max": 0.85,
                    "label": "Ready",
                    "description": "Meets all senior expectations: architects scalable multi-module apps, mentors engineers, enforces performance standards, and automates CI/CD."
                },
                "exceeds": {
                    "min": 0.85,
                    "max": 1.0,
                    "label": "Exceeds Expectations",
                    "description": "Exceeds senior expectations: staff/principal mobile leadership driving cross-platform KMP strategy and enterprise mobile infrastructure."
                }
            }
        }
    }
}

for level_name, role_data in roles.items():
    file_path = os.path.join(base_dir, 'roles', 'android', f"{level_name}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(role_data, f, indent=2, ensure_ascii=False)
    print(f"Written role: roles/android/{level_name}.json")

# -------------------------------------------------------------
# 3. Android Evidence (github, cv, linkedin, assessment)
# -------------------------------------------------------------

# github.json
github_evidence = {
    "source_id": "github",
    "name": "GitHub Repository Analysis - Android Developer",
    "description": "Global parsing rules for Android repositories across Kotlin and Java codebases. NOTE: Specific evidence mappings (regex patterns and maps_to composite keys) are stored within individual skill files under evidence.github, NOT here. The validate_composite_keys.py script scans both locations to verify coverage.",
    "preprocessing_pipeline": {
        "steps": [
            {
                "step": 1,
                "name": "file_tree_scan",
                "target_files": [
                    {
                        "pattern": "build\\.gradle|build\\.gradle\\.kts|settings\\.gradle|settings\\.gradle\\.kts|gradle/libs\\.versions\\.toml",
                        "skills": ["android_fundamentals_kotlin", "android_platform_services_quality", "android_architecture_patterns"],
                        "priority": "high",
                        "notes": "Gradle build configuration, Kotlin DSL, version catalogs, and dependency graph"
                    },
                    {
                        "pattern": "AndroidManifest\\.xml",
                        "skills": ["android_app_components", "android_platform_services_quality"],
                        "priority": "high",
                        "notes": "Component declarations, permissions, foreground services, intent filters, and application metadata"
                    },
                    {
                        "pattern": "proguard-rules\\.pro|consumer-rules\\.pro",
                        "skills": ["android_platform_services_quality"],
                        "priority": "high",
                        "notes": "R8 and ProGuard code shrinking, obfuscation, and optimization rules"
                    },
                    {
                        "pattern": "\\.kt$|\\.java$",
                        "skills": ["android_fundamentals_kotlin", "android_ui_layouts", "android_architecture_patterns", "android_concurrency_async", "android_data_persistence"],
                        "priority": "high",
                        "notes": "Core Android source code analyzed for Compose, Coroutines, Room, Hilt, and architecture patterns"
                    },
                    {
                        "pattern": "\\.aidl$",
                        "skills": ["android_app_components"],
                        "priority": "medium",
                        "notes": "Android Interface Definition Language (AIDL) for inter-process communication"
                    },
                    {
                        "pattern": "*Test*\\.kt|*Test*\\.java|*Spec*\\.kt|androidTest/",
                        "skills": ["android_platform_services_quality", "android_concurrency_async"],
                        "priority": "high",
                        "notes": "Unit tests (MockK, JUnit5) and instrumented UI tests (Espresso, Compose test rules)"
                    }
                ]
            },
            {
                "step": 2,
                "name": "dependency_extraction",
                "source_manifests": [
                    "build.gradle",
                    "build.gradle.kts",
                    "gradle/libs.versions.toml"
                ],
                "relevant_dependencies": {
                    "android_data_persistence": ["androidx.room", "retrofit", "okhttp3", "androidx.datastore", "androidx.paging"],
                    "android_architecture_patterns": ["com.google.dagger:hilt", "androidx.hilt", "androidx.navigation", "androidx.lifecycle"],
                    "android_ui_layouts": ["androidx.compose.ui", "androidx.compose.material3", "androidx.constraintlayout", "androidx.recyclerview"],
                    "android_concurrency_async": ["org.jetbrains.kotlinx:kotlinx-coroutines", "app.cash.turbine", "io.reactivex.rxjava3"],
                    "android_platform_services_quality": ["io.mockk:mockk", "androidx.test.espresso", "com.google.firebase:firebase-crashlytics", "com.squareup.leakcanary:leakcanary-android"]
                }
            },
            {
                "step": 3,
                "name": "config_file_scan",
                "target_configs": [
                    "AndroidManifest.xml",
                    "build.gradle.kts",
                    "build.gradle",
                    "proguard-rules.pro",
                    "libs.versions.toml",
                    "assetlinks.json"
                ]
            }
        ]
    },
    "ai_analysis_instructions": {
        "tasks": [
            "Map detected signals to composite keys ({skill_id}.{subskill_id}) using patterns defined in android skill files",
            "Inspect build.gradle.kts dependencies for modern Jetpack libraries (Compose, Room, Hilt, Coroutines, Paging 3)",
            "Check UI architecture — presence of Jetpack Compose declarative layouts with State hoisting vs legacy XML layouts",
            "Evaluate concurrency safety — verify usage of repeatOnLifecycle or flowWithLifecycle for UI Flow collection",
            "Assess test coverage — presence of MockK unit tests and Compose UI tests"
        ]
    }
}

with open(os.path.join(base_dir, 'evidence', 'android', 'github.json'), 'w', encoding='utf-8') as f:
    json.dump(github_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/android/github.json")

# cv.json
cv_evidence = {
    "source_id": "cv",
    "name": "CV / Resume Analysis - Android Developer",
    "description": "Signals extracted from the user's CV/resume to evidence Android Developer skills. CV data provides self-reported information that must be cross-validated with GitHub and assessment sources.",
    "extraction_rules": {
        "description": "How to extract and weight information from CV content for Android roles.",
        "sections": [
            {
                "section": "skills_list",
                "description": "Explicit list of technologies, frameworks, and tools in skills section.",
                "base_strength": 0.3,
                "notes": "Low strength alone. Listing 'Kotlin' or 'Jetpack Compose' requires verification against project details."
            },
            {
                "section": "work_experience",
                "description": "Job descriptions describing Android engineering achievements and architectural responsibilities.",
                "base_strength": 0.5,
                "quality_indicators": [
                    "Specific Jetpack libraries and architectural patterns mentioned (e.g. 'architected multi-module MVI app with Jetpack Compose and Hilt')",
                    "Quantifiable mobile performance metrics (reduced cold start time by 40% using Baseline Profiles, eliminated UI frame drops to 0.1%)",
                    "Action verbs indicating hands-on mobile leadership (architected, migrated, modularized, optimized, hardened)",
                    "Scale indicators (apps with 1M+ MAU, multi-tenant white-label SDKs)"
                ]
            },
            {
                "section": "projects",
                "description": "Personal or open-source Android projects demonstrating technical depth.",
                "base_strength": 0.4,
                "notes": "Higher strength if linked to GitHub with clean Compose UI, Room offline-first sync, and test suites."
            },
            {
                "section": "certifications",
                "description": "Professional Android certifications (Associate Android Developer).",
                "base_strength": 0.2,
                "recognized_certifications": {
                    "android_google": [
                        "Google Associate Android Developer (AAD)",
                        "Meta Android Developer Professional Certificate"
                    ]
                }
            }
        ]
    },
    "signal_mapping": {
        "description": "How CV mentions map to skill evidence using COMPOSITE KEYS ({skill_id}.{subskill_id}).",
        "patterns": [
            {
                "pattern": "Built reactive Android user interfaces with Jetpack Compose, Material 3, and state hoisting",
                "maps_to": ["android_ui_layouts.compose_fundamentals_state", "android_ui_layouts.design_systems_theming", "android_ui_layouts.compose_layout_modifiers"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Implemented offline-first data sync architecture with Room ORM and Retrofit",
                "maps_to": ["android_data_persistence.offline_first_synchronization", "android_data_persistence.room_database_fundamentals", "android_data_persistence.retrofit_networking_client"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Architected multi-module Android codebases using Clean Architecture and Hilt DI",
                "maps_to": ["android_architecture_patterns.modularization_multi_module", "android_architecture_patterns.clean_architecture_domain_layer", "android_architecture_patterns.dependency_injection_hilt_basics"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Migrated legacy RxJava codebase to Kotlin Coroutines and asynchronous Flow",
                "maps_to": ["android_concurrency_async.reactive_streams_rxjava_migration", "android_concurrency_async.stateflow_sharedflow_hot_streams", "android_concurrency_async.coroutine_memory_leaks_profiling"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Scheduled guaranteed background sync tasks using WorkManager and Foreground Services",
                "maps_to": ["android_app_components.workmanager_background_jobs", "android_app_components.service_architecture_types"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Developed cross-platform shared business logic using Kotlin Multiplatform (KMP)",
                "maps_to": ["android_fundamentals_kotlin.multiplatform_kotlin_kmp", "android_fundamentals_kotlin.kotlin_generics_variance"],
                "strength_modifier": 1.2
            },
            {
                "pattern": "Optimized app startup performance with Baseline Profiles and App Startup library",
                "maps_to": ["android_architecture_patterns.app_startup_architecture", "android_ui_layouts.ui_performance_profiling"],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Hardened app security using Android KeyStore, EncryptedSharedPreferences, and R8 obfuscation",
                "maps_to": ["android_data_persistence.encrypted_storage_keystore", "android_platform_services_quality.security_obfuscation_tamper_proofing"],
                "strength_modifier": 1.1
            }
        ]
    },
    "important_notes": [
        "Distinguish between client-side API consumption (Retrofit/Room) and backend API design (be_api_design)",
        "Look for modern Android stack competencies (Compose, Coroutines/Flow, Hilt) vs legacy patterns (AsyncTask, findViewById)",
        "Cross-validate self-reported performance claims with code in GitHub and assessment results"
    ]
}

with open(os.path.join(base_dir, 'evidence', 'android', 'cv.json'), 'w', encoding='utf-8') as f:
    json.dump(cv_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/android/cv.json")

# linkedin.json
linkedin_evidence = {
    "source_id": "linkedin",
    "name": "LinkedIn Profile Analysis - Android Developer",
    "description": "Signals extracted from LinkedIn profiles to evidence Android Developer skills.",
    "extraction_rules": {
        "sections": [
            {
                "section": "headline_summary",
                "description": "Profile headline and summary section.",
                "base_strength": 0.2,
                "notes": "Look for specialization (e.g. 'Senior Android Engineer | Jetpack Compose | KMP')."
            },
            {
                "section": "experience",
                "description": "Work experience entries with job titles and project descriptions.",
                "base_strength": 0.4,
                "quality_indicators": [
                    "Android-specific job titles (Android Engineer, Mobile Platform Architect, Android Lead)",
                    "Technologies described (Kotlin, Compose, Coroutines, Room, Hilt, KMP)",
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
                "pattern": "LinkedIn skills endorsement for 'Kotlin' or 'Android Development'",
                "maps_to": ["android_fundamentals_kotlin.kotlin_language_features", "android_fundamentals_kotlin.android_sdk_lifecycle_basics"],
                "strength_modifier": 0.33
            },
            {
                "pattern": "LinkedIn skills endorsement for 'Jetpack Compose' or 'Android UI'",
                "maps_to": ["android_ui_layouts.compose_fundamentals_state", "android_ui_layouts.compose_layout_modifiers"],
                "strength_modifier": 0.33
            },
            {
                "pattern": "Job experience describing building Jetpack Compose design systems and multi-module apps",
                "maps_to": ["android_ui_layouts.design_systems_theming", "android_architecture_patterns.modularization_multi_module", "android_architecture_patterns.mvvm_architecture_pattern"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing Kotlin Coroutines, asynchronous Flow, and offline sync engines",
                "maps_to": ["android_concurrency_async.coroutines_basics_dispatchers", "android_concurrency_async.stateflow_sharedflow_hot_streams", "android_data_persistence.offline_first_synchronization"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing Android CI/CD pipelines, Gradle build optimization, and R8 obfuscation",
                "maps_to": ["android_platform_services_quality.ci_cd_gradle_build_optimization", "android_platform_services_quality.security_obfuscation_tamper_proofing"],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing WorkManager background tasks and Foreground Services",
                "maps_to": ["android_app_components.workmanager_background_jobs", "android_app_components.service_architecture_types"],
                "strength_modifier": 1.0
            }
        ]
    },
    "important_notes": [
        "ALL extracted signals MUST be mapped to COMPOSITE KEYS ({skill_id}.{subskill_id})",
        "LinkedIn endorsements have low evidential value on their own; cross-validate with code"
    ]
}

with open(os.path.join(base_dir, 'evidence', 'android', 'linkedin.json'), 'w', encoding='utf-8') as f:
    json.dump(linkedin_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/android/linkedin.json")

print("Android skills, roles, and github/cv/linkedin evidence generated successfully.")
