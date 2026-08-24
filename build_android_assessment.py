import os
import json

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'knowledge-base'))

questions = {
    # -------------------------------------------------------------
    # 1. android_fundamentals_kotlin (9 subskills)
    # -------------------------------------------------------------
    "android_fundamentals_kotlin.kotlin_language_features": [
        {
            "level": "junior",
            "type": "code_review",
            "question": "A junior developer wrote `val nameLength = if (user != null) user.name.length else 0` and uses normal classes for UI states with multiple boolean flags (`isLoading`, `isError`, `isSuccess`). How would you refactor this using Kotlin's safe call with Elvis operator (`?.` and `?:`) and sealed interfaces for UI state representation?",
            "expected_answer_keywords": ["safe call `user?.name?.length ?: 0`", "Elvis operator", "sealed interface UiState", "exhaustive when expression", "eliminating mutually conflicting boolean flags", "type safety"]
        }
    ],
    "android_fundamentals_kotlin.kotlin_higher_order_lambdas": [
        {
            "level": "junior",
            "type": "comparison",
            "question": "Explain the behavioral and semantic differences between Kotlin scope functions `let`, `apply`, `run`, `also`, and `with`. Specifically, contrast `apply` vs `also` regarding their context receiver (`this` vs `it`) and return value when configuring an Android `Intent` or `TextView`.",
            "expected_answer_keywords": ["context object (`this` vs `it`)", "return value (context object vs lambda result)", "`apply` returns context object with `this`", "`also` returns context object with `it`", "`let` for null check transformation", "Intent configuration with `apply`"]
        }
    ],
    "android_fundamentals_kotlin.android_sdk_lifecycle_basics": [
        {
            "level": "junior",
            "type": "debugging",
            "question": "An Android application crashes with a `BadTokenException` when trying to display an `AlertDialog` using `applicationContext`, while a singleton service holding onto an `Activity` context causes a persistent 80MB memory leak. Explain why `ApplicationContext` cannot host dialog windows and why passing `Activity` context to long-lived singletons leads to memory leaks.",
            "expected_answer_keywords": ["WindowManager token attached to Activity window", "ApplicationContext has no window token", "BadTokenException", "Activity context retains entire view hierarchy", "static/singleton reference preventing GC", "ApplicationContext for singletons"]
        }
    ],
    "android_fundamentals_kotlin.kotlin_generics_variance": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "You are building a generic repository interface in Kotlin. Explain why `interface ReadOnlyRepository<out T>` requires covariance (`out`), while `interface Consumer<in T>` requires contravariance (`in`). What compiler error occurs if a function in `ReadOnlyRepository<out T>` accepts `T` as a parameter?",
            "expected_answer_keywords": ["declaration-site variance", "covariance (`out`) for producer positions", "contravariance (`in`) for consumer positions", "type safety invariant", "compile error: Type parameter T is declared as 'out' but occurs in 'in' position", "Liskov Substitution Principle"]
        }
    ],
    "android_fundamentals_kotlin.kotlin_delegated_properties": [
        {
            "level": "mid",
            "type": "code_review",
            "question": "Write a custom Kotlin property delegate `class PreferenceDelegate<T>(...) : ReadWriteProperty<Any?, T>` that automatically reads from and writes to Jetpack DataStore / SharedPreferences when the property is accessed. Explain how `getValue` and `setValue` operators work behind the scenes in Kotlin bytecode.",
            "expected_answer_keywords": ["ReadWriteProperty<Any?, T>", "operator fun getValue(thisRef: Any?, property: KProperty<*>) : T", "operator fun setValue(thisRef: Any?, property: KProperty<*>, value: T)", "KProperty reflection metadata", "by keyword delegate synthesis", "clean property access"]
        }
    ],
    "android_fundamentals_kotlin.kotlin_dsl_type_safe_builders": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "Design a custom type-safe builder DSL in Kotlin for constructing complex network request configurations (e.g. `httpClient { endpoint(\"/users\") { headers { ... } } }`). How does function literal with receiver (`HttpClientBuilder.() -> Unit`) enable this syntax, and why is the `@DslMarker` annotation necessary to prevent outer scope leaking?",
            "expected_answer_keywords": ["function literal with receiver (`Builder.() -> Unit`)", "`this` binding to receiver instance", "@DslMarker meta-annotation", "scope control", "preventing nested inner builder from calling outer builder methods implicitly"]
        }
    ],
    "android_fundamentals_kotlin.kotlin_compiler_plugins_ksp": [
        {
            "level": "senior",
            "type": "architectural_trade_off",
            "question": "Compare Kotlin Symbol Processing (KSP) with legacy KAPT (Kotlin Annotation Processing Tool) regarding build speed, Java stub generation, and incremental compilation. Walk through the architecture of a custom KSP `SymbolProcessor` that generates type-safe database mappers from `@AutoMapper` annotations.",
            "expected_answer_keywords": ["KSP eliminates Java stub generation (2x+ build speedup)", "direct Kotlin AST access via KSVisitor", "KAPT requires javac conversion", "SymbolProcessor / SymbolProcessorProvider", "Resolver API to find annotated symbols", "CodeGenerator for source file emission"]
        }
    ],
    "android_fundamentals_kotlin.kotlin_memory_model_bytecode": [
        {
            "level": "senior",
            "type": "debugging",
            "question": "A high-frequency Android rendering loop experiences recurring Garbage Collection pauses (jank). Profiling reveals that a lambda capturing an external local variable inside `forEach` allocates millions of `Function1` instances on the heap, while boxing `Int` to `java.lang.Integer`. Explain how inline functions (`inline`, `noinline`, `crossinline`) and Kotlin `inline value class` eliminate these heap allocations in bytecode.",
            "expected_answer_keywords": ["capturing lambda heap allocation (`Function1`)", "primitive boxing (`Int` to `java.lang.Integer`)", "`inline` inlines lambda body at call site", "eliminating object allocation", "`inline value class` represented as primitive in bytecode", "ART GC pressure reduction"]
        }
    ],
    "android_fundamentals_kotlin.multiplatform_kotlin_kmp": [
        {
            "level": "senior",
            "type": "architectural_trade_off",
            "question": "Architect a cross-platform mobile application sharing 70% of its codebase between Android and iOS using Kotlin Multiplatform (KMP). Detail the separation of concerns: which layers (Domain, Data, Networking with Ktor, Persistence with SqlDelight) are shared in `commonMain`, how `expect`/`actual` declarations resolve platform-specific hardware APIs (Keychain/KeyStore), and how Swift interacts with Kotlin shared models.",
            "expected_answer_keywords": ["`commonMain` for domain, repository, Ktor HTTP client, SqlDelight DB", "`expect`/`actual` for platform hardware differences", "native Swift UI (SwiftUI) consuming shared KMP Kotlin flows", "SKIE / KMP-NativeCoroutines for Swift async bridging", "CocoaPods/SPM framework packaging"]
        }
    ],

    # -------------------------------------------------------------
    # 2. android_app_components (9 subskills)
    # -------------------------------------------------------------
    "android_app_components.activity_lifecycle_navigation": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "A user is filling out a multi-step registration form in an Activity when an incoming phone call rotates the device. Explain the sequence of lifecycle events that occur, why state loss happens by default, and how you use `onSaveInstanceState(Bundle)` and `SavedStateHandle` in the ViewModel to preserve user input across process death and configuration changes.",
            "expected_answer_keywords": ["onPause -> onStop -> onSaveInstanceState -> onDestroy -> onCreate -> onStart -> onRestoreInstanceState -> onResume", "configuration change recreation", "SavedStateHandle in ViewModel", "Bundle key-value serialization", "process death survival vs orientation change"]
        }
    ],
    "android_app_components.fragment_lifecycle_manager": [
        {
            "level": "junior",
            "type": "debugging",
            "question": "An app crashes with `IllegalStateException: Can not perform this action after onSaveInstanceState` when committing a `FragmentTransaction` inside an asynchronous network callback. Explain why this exception occurs, why `commitAllowingStateLoss()` is often a dangerous workaround, and how to safely navigate using the Fragment Result API or Lifecycle-aware coroutines.",
            "expected_answer_keywords": ["state loss after `onSaveInstanceState`", "FragmentManager state serialization", "`commitAllowingStateLoss()` drops backstack state on restore", "Fragment Result API (`setFragmentResult` / `setFragmentResultListener`)", "lifecycleScope.launchWhenResumed / repeatOnLifecycle"]
        }
    ],
    "android_app_components.broadcast_receivers_intents": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "On Android 13+ (API 33+), registering a dynamic `BroadcastReceiver` without specifying `RECEIVER_EXPORTED` or `RECEIVER_NOT_EXPORTED` throws a SecurityException. Explain the security implications of this flag, when an app should export a receiver to other apps vs keeping it internal, and how implicit vs explicit intents differ in broadcast security.",
            "expected_answer_keywords": ["RECEIVER_EXPORTED vs RECEIVER_NOT_EXPORTED", "Android 13 security requirement", "preventing unauthorized external apps from sending spoofed broadcasts", "explicit intent targeting specific component", "implicit intent broadcast hijacking risks"]
        }
    ],
    "android_app_components.service_architecture_types": [
        {
            "level": "mid",
            "type": "architectural_trade_off",
            "question": "An audio streaming application needs to continue playing music when the user switches to other apps, while also allowing an in-app player controller to bind and control playback. Architect this using a Foreground Service with `foregroundServiceType=\"mediaPlayback\"` (Android 14 requirement) and a Bound Service with `MediaSessionCompat` and `IBinder`.",
            "expected_answer_keywords": ["Foreground Service with ongoing notification", "`foregroundServiceType=\"mediaPlayback\"` (Android 14)", "Bound Service via `ServiceConnection` and `IBinder`", "MediaSessionCompat integration", "background execution limits survival", "`startForeground()` within 10 seconds"]
        }
    ],
    "android_app_components.content_providers_sharing": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "Your app captures high-resolution photos and needs to share them securely with external image editing apps. Explain why using `file://` URIs triggers a `FileUriExposedException` on modern Android, and walk through configuring `FileProvider` (`<provider>`, `file_paths.xml`, `getUriForFile()`, and `FLAG_GRANT_READ_URI_PERMISSION`) to share secure `content://` URIs.",
            "expected_answer_keywords": ["`FileUriExposedException` on Android 7.0+", "FileProvider subclass of ContentProvider", "`content://` URI with temporary scoped permissions", "`file_paths.xml` directory mapping", "`FileProvider.getUriForFile()`", "`FLAG_GRANT_READ_URI_PERMISSION` in Intent"]
        }
    ],
    "android_app_components.workmanager_background_jobs": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "You need to upload 100 pending offline transaction records to the backend when the device is connected to an unmetered Wi-Fi network and charging. Explain how you implement this with `WorkManager`, configure `Constraints`, chain a compression worker with an upload worker (`beginWith(...).then(...)`), and handle worker cancellation gracefully in a `CoroutineWorker`.",
            "expected_answer_keywords": ["WorkManager with Constraints.Builder", "NetworkType.UNMETERED", "setRequiresCharging(true)", "OneTimeWorkRequestBuilder chaining", "CoroutineWorker with `doWork()`", "handling cancellation via `isStopped` / CancellationException", "WorkManager UniqueWork (ExistingWorkPolicy.KEEP/REPLACE)"]
        }
    ],
    "android_app_components.ipc_aid_binder_architecture": [
        {
            "level": "senior",
            "type": "debugging",
            "question": "A banking SDK runs in an isolated Android process (`:remote_auth`) and communicates with client apps via AIDL and the Linux Binder driver. During a high-payload biometric transaction, the app crashes with `TransactionTooLargeException`. Explain the Binder transaction buffer limit (1MB shared across process), how to handle `DeadObjectException` via `IBinder.DeathRecipient`, and how to stream large payloads across IPC using `ParcelFileDescriptor` / Ashmem.",
            "expected_answer_keywords": ["Binder 1MB transaction buffer limit", "TransactionTooLargeException", "IBinder.DeathRecipient linkToDeath / binderDied", "DeadObjectException handling on process kill", "ParcelFileDescriptor shared memory (Ashmem) for large payloads", "AIDL synchronous vs oneway calls"]
        }
    ],
    "android_app_components.process_lifecycle_management": [
        {
            "level": "senior",
            "type": "governance_case_study",
            "question": "Explain how the Android Linux kernel Low Memory Killer (LMK) determines which processes to terminate under memory pressure using `oom_adj` / `oom_score_adj` values. Compare the priority levels of Foreground Process, Visible Process, Service Process, and Cached Process. What architectural patterns guarantee that user state is completely recoverable even if the OS kills the process in the background?",
            "expected_answer_keywords": ["Low Memory Killer (LMK)", "oom_adj / oom_score_adj priority scoring", "Cached process (highest kill priority) vs Foreground process", "SavedStateHandle / persistent database sync", "onTrimMemory callbacks handling", "idempotent app initialization on cold restore"]
        }
    ],
    "android_app_components.deep_linking_app_links": [
        {
            "level": "senior",
            "type": "architectural_trade_off",
            "question": "Compare standard custom URI schemes (`myapp://order/123`) with verified Android App Links (`https://myapp.com/order/123`) in terms of security, user disambiguation dialogs, and domain hijacking. Walk through configuring Digital Asset Links (`assetlinks.json` on HTTPS server), AndroidManifest `<intent-filter android:autoVerify=\"true\">`, and synthetic backstack generation using `TaskStackBuilder` when deep linking directly into a detail screen.",
            "expected_answer_keywords": ["custom URI scheme hijacking by malicious apps", "Android App Links verification with `assetlinks.json` SHA-256 fingerprint", "android:autoVerify=\"true\"", "eliminating app chooser disambiguation dialog", "TaskStackBuilder to create proper hierarchical parent backstack", "navigation routing engine"]
        }
    ],

    # -------------------------------------------------------------
    # 3. android_ui_layouts (9 subskills)
    # -------------------------------------------------------------
    "android_ui_layouts.xml_layouts_view_binding": [
        {
            "level": "junior",
            "type": "code_review",
            "question": "A legacy XML layout uses 5 nested `LinearLayout`s and `RelativeLayout`s to align user profile elements, causing severe layout flattening issues during inflation. How would you refactor this layout using `ConstraintLayout` with Barriers, Guidelines, and Chains? Explain why `ViewBinding` is superior to `findViewById` and synthetic imports regarding null safety and type safety.",
            "expected_answer_keywords": ["ConstraintLayout flat view hierarchy", "Guidelines (percentage/fixed)", "Barriers for dynamic content alignment", "Chains (spread/spread_inside/packed)", "ViewBinding compile-time type safety", "ViewBinding null safety (no NullPointerException on missing IDs)"]
        }
    ],
    "android_ui_layouts.recyclerview_adapter_patterns": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "A news feed `RecyclerView` stutters and drops frames when loading new articles because the adapter calls `notifyDataSetChanged()`, causing all visible items to re-bind. Explain how refactoring to `ListAdapter` with `DiffUtil.ItemCallback` and `AsyncListDiffer` computes granular list diffs on a background thread and triggers targeted insert/delete/update animations.",
            "expected_answer_keywords": ["`notifyDataSetChanged()` invalidates entire view cache causing jank", "ListAdapter with DiffUtil.ItemCallback", "areItemsTheSame (identity/ID check)", "areContentsTheSame (equality check)", "AsyncListDiffer computes diffs on background thread", "granular item animations (notifyItemRangeInserted)"]
        }
    ],
    "android_ui_layouts.compose_fundamentals_state": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "Explain the concept of State Hoisting in Jetpack Compose. Given a composable `Counter` that manages its own internal count with `remember { mutableStateOf(0) }`, refactor it into an uncontrolled/stateless composable that accepts `count: Int` and `onIncrement: () -> Unit`. Why is `rememberSaveable` necessary if the screen is rotated?",
            "expected_answer_keywords": ["State Hoisting (moving state to caller)", "stateless composable with value and event parameters", "`count: Int, onIncrement: () -> Unit`", "unidirectional data flow (state flows down, events flow up)", "`remember` lost on configuration change", "`rememberSaveable` persists state in saved instance state Bundle"]
        }
    ],
    "android_ui_layouts.compose_layout_modifiers": [
        {
            "level": "mid",
            "type": "code_review",
            "question": "Explain the significance of Modifier ordering in Jetpack Compose by comparing `Modifier.padding(16.dp).clickable { }.background(Color.Blue)` versus `Modifier.background(Color.Blue).clickable { }.padding(16.dp)`. In a `LazyColumn` containing heterogeneous items (Ads, Posts, Headers), why is specifying `contentType` alongside `key` critical for composition recycling?",
            "expected_answer_keywords": ["Modifier ordering determines layout & draw pipeline execution order", "padding before clickable affects touch target and background bounds", "LazyColumn `key` for identity tracking across dataset shifts", "`contentType` enables Compose layout node recycling between same-type items", "eliminating unnecessary composition allocation"]
        }
    ],
    "android_ui_layouts.custom_views_canvas_drawing": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "You need to build a custom circular speedometer Gauge View in Android that draws dynamic arcs, tick marks, and animated needles. Explain how you implement this in a custom `View` subclass by overriding `onMeasure` (handling `MeasureSpec.EXACTLY` vs `AT_MOST`), using `Canvas.drawArc()` and `Paint.Style.STROKE`, and invalidating with `postInvalidateOnAnimation()`.",
            "expected_answer_keywords": ["Custom View subclass", "onMeasure with MeasureSpec.getMode and getSize", "handling wrap_content (`MeasureSpec.AT_MOST`)", "Canvas.drawArc, drawLine, drawText", "Paint configuration (anti-alias, strokeCap, shader)", "ValueAnimator with `invalidate()` or `postInvalidateOnAnimation()`"]
        }
    ],
    "android_ui_layouts.compose_side_effects_lifecycle": [
        {
            "level": "mid",
            "type": "debugging",
            "question": "A Compose screen triggers an API call directly in the composable body: `viewModel.fetchUser(userId)`. Every time the user types in a search bar, the entire screen recomposes and re-fires the network request 50 times. Explain why this bug occurs and how to fix it using `LaunchedEffect(userId)`. Contrast `LaunchedEffect`, `DisposableEffect`, and `rememberUpdatedState`.",
            "expected_answer_keywords": ["Composable body executes on every recomposition", "LaunchedEffect(key) launches coroutine tied to Compose lifecycle and key change", "DisposableEffect for teardown/cleanup on key change or disposal", "rememberUpdatedState captures latest lambda without restarting effect", "preventing infinite recomposition loops"]
        }
    ],
    "android_ui_layouts.compose_compiler_recomposition": [
        {
            "level": "senior",
            "type": "debugging",
            "question": "In a Compose app, a `UserCard(user: User)` composable recomposes every frame even though `user` data has not changed. Compose compiler metrics reveal that `User` from an external multi-module data layer is inferred as 'unstable'. Explain how Compose stability inference works (primitive types vs collections like `List<T>`), why `List<T>` is considered unstable, and how to resolve it using `@Immutable`, `@Stable`, or Kotlinx Immutable Collections (`ImmutableList`).",
            "expected_answer_keywords": ["Compose Stability inference (`@Stable` / `@Immutable`)", "Standard `List<T>` is an interface (could be mutable `ArrayList` behind scenes -> unstable)", "Compose compiler cannot skip composables with unstable parameters", "Kotlinx Immutable Collections (`ImmutableList<T>`)", "@Immutable wrapper annotation", "skipping recomposition optimization"]
        }
    ],
    "android_ui_layouts.design_systems_theming": [
        {
            "level": "senior",
            "type": "architectural_trade_off",
            "question": "Architect a centralized Material Design 3 (M3) design system library for an enterprise suite of 5 Android applications. How do you structure design tokens (Color Roles: primary, surface, container; Typography styles; Shape scales), support Android 12+ Dynamic Color (Material You) with user wallpaper tones while falling back to brand palettes on older devices, and implement high-contrast / dark theme switching?",
            "expected_answer_keywords": ["Material 3 ColorScheme tokenization (container, on-color, surface)", "Dynamic Color via `dynamicLightColorScheme(context)` and `dynamicDarkColorScheme(context)`", "custom LocalExtendedColors / CompositionLocalProvider", "Typography and Shape scale definitions", "multi-app white-label theme swapping", "dark/light theme tokens"]
        }
    ],
    "android_ui_layouts.ui_performance_profiling": [
        {
            "level": "senior",
            "type": "governance_case_study",
            "question": "Users on 120Hz display devices report noticeable frame drops (jank) during fast scrolling in a complex feed. Walk through your performance diagnosis methodology: using `JankStats` to track frame rendering metrics, identifying GPU overdraw in Developer Options, analyzing Perfetto / Systrace UI thread slice traces for `Choreographer#doFrame` stalls, and fixing View hierarchy overdraw or heavy modifier chains.",
            "expected_answer_keywords": ["120Hz = 8.3ms per frame budget", "JankStats library for real-time jank telemetry", "GPU Overdraw color inspection (blue/green/red)", "eliminating redundant window backgrounds", "Perfetto / Systrace trace inspection (`Choreographer#doFrame`, `RenderThread`)", "Layout Inspector recomposition count analysis"]
        }
    ],

    # -------------------------------------------------------------
    # 4. android_architecture_patterns (9 subskills)
    # -------------------------------------------------------------
    "android_architecture_patterns.mvvm_architecture_pattern": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "Design a clean MVVM architecture for an Android user profile screen. How does the Jetpack `ViewModel` communicate state changes to the UI layer without holding a direct reference to the Activity/View? Model the UI state using a single immutable Kotlin data class `ProfileUiState(val user: User?, val isLoading: Boolean, val error: String?)` exposed via `StateFlow`.",
            "expected_answer_keywords": ["ViewModel does not reference Activity/View (memory leak prevention)", "Single immutable `ProfileUiState` data class", "Private `MutableStateFlow` and public `asStateFlow()`", "UI collects StateFlow in lifecycle-aware manner", "separation of UI rendering from business state"]
        }
    ],
    "android_architecture_patterns.dependency_injection_hilt_basics": [
        {
            "level": "junior",
            "type": "code_review",
            "question": "Review an Android codebase where Activities instantiate their own Retrofit instances and Room databases with `new`. Refactor this using Hilt Dependency Injection: annotate the Application class with `@HiltAndroidApp`, Activity with `@AndroidEntryPoint`, ViewModel with `@HiltViewModel`, create a `@Module` with `@Provides` and `@Singleton` for the OkHttpClient, and constructor-inject the repository with `@Inject`.",
            "expected_answer_keywords": ["@HiltAndroidApp on Application", "@AndroidEntryPoint on Activity/Fragment", "@HiltViewModel and @Inject constructor on ViewModel", "@Module @InstallIn(SingletonComponent::class)", "@Provides @Singleton for OkHttpClient/Retrofit/Room", "constructor injection with @Inject"]
        }
    ],
    "android_architecture_patterns.repository_pattern_data_sources": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "Explain the Repository pattern as the single source of truth (SSOT) in an Android data layer. When `UserRepository.getUser(id)` is called, how does the repository coordinate between a local Room database cache and a remote Retrofit API service? Why should raw API Data Transfer Objects (DTOs) be mapped to Domain models inside the repository layer?",
            "expected_answer_keywords": ["Repository as Single Source of Truth (SSOT)", "local database cache with remote API synchronization", "DTO to Domain model mapper functions", "preventing API schema changes from polluting UI/Domain layers", "returning Flow<Resource<User>> from repository"]
        }
    ],
    "android_architecture_patterns.clean_architecture_domain_layer": [
        {
            "level": "mid",
            "type": "architectural_trade_off",
            "question": "Explain why the Domain layer in Clean Architecture should be a pure Kotlin module with zero Android SDK dependencies (`android.*`). Design a `GetOrderSummaryUseCase` that orchestrates multiple repositories (`OrderRepository`, `UserRepository`, `PaymentRepository`), executes business validation rules, and exposes an `operator fun invoke(orderId: String): Flow<OrderSummary>`.",
            "expected_answer_keywords": ["Pure Kotlin Domain layer (no Android framework dependencies)", "Unit testability without Robolectric or mocks of Android classes", "single-responsibility UseCase / Interactor", "`operator fun invoke` convention", "Dependency Inversion Principle (Domain defines repository interfaces, Data implements them)"]
        }
    ],
    "android_architecture_patterns.mvi_unidirectional_data_flow": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "Compare Model-View-ViewModel (MVVM) with Model-View-Intent (MVI) architecture. In an MVI payment checkout screen, design the sealed interface `CheckoutIntent` (e.g. `ApplyCoupon`, `SelectPaymentMethod`, `SubmitOrder`), the immutable `CheckoutState`, and the single-shot `CheckoutEffect` (e.g. `NavigateToSuccess`, `ShowToast`). Why does MVI prevent state synchronization race conditions?",
            "expected_answer_keywords": ["MVI Unidirectional Data Flow (UDF)", "sealed interface Intent/Action from UI to ViewModel", "single immutable ViewState reducer", "SideEffect / Event Channel for one-off events (navigation, toast)", "eliminating multiple conflicting StateFlows in ViewModel", "reproducible state machine"]
        }
    ],
    "android_architecture_patterns.advanced_di_scopes_modules": [
        {
            "level": "mid",
            "type": "code_review",
            "question": "You need to inject a dynamic runtime parameter `userId: String` into a ViewModel while still letting Hilt inject all other dependencies. Explain how `@AssistedInject` and `@AssistedFactory` solve this. Furthermore, how do Dagger Multi-bindings (`@IntoSet`, `@IntoMap`, `@StringKey`) allow plugin-based architecture for dynamic feature handlers?",
            "expected_answer_keywords": ["@AssistedInject for runtime parameter injection", "@AssistedFactory interface definition", "@Assisted parameter annotation", "Dagger Multi-bindings (@IntoSet, @IntoMap)", "@StringKey / @ClassKey multibinding map", "plugin architecture without hardcoded switch statements"]
        }
    ],
    "android_architecture_patterns.modularization_multi_module": [
        {
            "level": "senior",
            "type": "architectural_trade_off",
            "question": "Architect a multi-module Android project for a large engineering organization with 30+ developers. Detail the module hierarchy: `:app`, `:feature:*`, `:core:database`, `:core:network`, `:core:model`, `:core:designsystem`. How do you implement the 'core-api' vs 'core-impl' pattern to prevent feature modules from depending on each other directly and eliminate circular dependencies while maximizing Gradle build caching?",
            "expected_answer_keywords": ["Feature-by-feature modularization", "core-api (interfaces/contracts) vs core-impl (implementations)", "feature modules only depend on core-api", "eliminating circular dependencies", "Gradle build parallelization and compilation avoidance", "internal Kotlin visibility in implementation modules"]
        }
    ],
    "android_architecture_patterns.navigation_component_compose": [
        {
            "level": "senior",
            "type": "scenario",
            "question": "With Navigation Compose 2.8+ introducing type-safe navigation via Kotlin Serialization (`@Serializable`), design a complete navigation architecture for a multi-module app. How do you define type-safe route objects (`@Serializable data class OrderDetailRoute(val orderId: String)`), share route definitions across feature modules, handle nested navigation graphs, and pass deep link URLs into type-safe routes?",
            "expected_answer_keywords": ["Navigation Compose type-safe routing with `@Serializable`", "eliminating string route templates (\"order/{id}\")", "`NavHost` and `composable<T>`", "nested navigation graphs (`navigation<T>`)", "route contract shared in api module", "type-safe deep link parsing"]
        }
    ],
    "android_architecture_patterns.app_startup_architecture": [
        {
            "level": "senior",
            "type": "governance_case_study",
            "question": "A production app's cold start time is 2.8 seconds due to 12 different third-party SDKs each registering their own `ContentProvider` in `AndroidManifest.xml` to initialize on startup. Walk through optimizing startup: using the Jetpack `App Startup` library (`Initializer<T>`), deferring non-critical initializations to background threads via Coroutines, and generating Baseline Profiles with Macrobenchmark to eliminate JIT compilation during app launch.",
            "expected_answer_keywords": ["ContentProvider startup overhead in manifest", "Jetpack App Startup library (`Initializer<T>`)", "`tools:node=\"remove\"` to disable automatic provider initialization", "lazy / background asynchronous SDK initialization", "Baseline Profiles generation via Macrobenchmark", "AOT compilation on install reducing cold start to <1s"]
        }
    ],

    # -------------------------------------------------------------
    # 5. android_data_persistence (9 subskills)
    # -------------------------------------------------------------
    "android_data_persistence.datastore_preferences_preferences": [
        {
            "level": "junior",
            "type": "comparison",
            "question": "Compare Jetpack `Preferences DataStore` and `Proto DataStore` with legacy `SharedPreferences`. Why is calling `SharedPreferences.apply()` or `commit()` on the main thread dangerous (causing UI jank and ANRs), and how does DataStore's Flow-based asynchronous transactional API provide data consistency and type safety?",
            "expected_answer_keywords": ["SharedPreferences main thread I/O leading to ANRs", "DataStore runs asynchronously on Dispatchers.IO via Kotlin Flow", "Preferences DataStore for key-value vs Proto DataStore for schema-backed Protocol Buffers", "transactional updates with `dataStore.edit`", "compile-time type safety in Proto DataStore", "built-in SharedPreferences migration helper"]
        }
    ],
    "android_data_persistence.room_database_fundamentals": [
        {
            "level": "junior",
            "type": "code_review",
            "question": "Write a complete Room database setup in Kotlin: define an `@Entity(tableName = \"products\")` data class with a primary key, write a `@Dao` interface with `@Insert(onConflict = OnConflictStrategy.REPLACE)` and a reactive query `fun getProducts(): Flow<List<Product>>`, create the `@Database` abstract class, and explain how Room manages thread dispatching for Flow queries.",
            "expected_answer_keywords": ["@Entity with primaryKeys", "@Dao interface with @Query returning Flow", "OnConflictStrategy.REPLACE", "@Database(entities = [...], version = 1)", "Room executes Flow queries asynchronously on background thread pool", "automatic re-emission on table invalidation"]
        }
    ],
    "android_data_persistence.retrofit_networking_client": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "Configure a complete Retrofit2 client in Android with OkHttp: configure `HttpLoggingInterceptor` (enabled only in DEBUG builds), an `AuthInterceptor` that attaches `Bearer <token>` to all outgoing requests, integrate `Kotlinx.serialization` or `MoshiConverterFactory`, and define a Retrofit interface with suspend functions returning `Response<UserDto>`.",
            "expected_answer_keywords": ["Retrofit.Builder and OkHttpClient.Builder", "HttpLoggingInterceptor with Level.BODY in BuildConfig.DEBUG", "AuthInterceptor adding Authorization header", "Kotlinx.serialization / Moshi converter", "suspend functions returning DTO / Response<T>", "HTTP exception handling (4xx/5xx)"]
        }
    ],
    "android_data_persistence.room_relations_migrations": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "In a Room database, model a One-to-Many relationship between `User` and `Order` entities using `@Embedded` and `@Relation`. Write a database migration from schema version 1 to 2 that adds a non-null `status` column with default value `'PENDING'` to the `orders` table using `Migration(1, 2)`, and explain how to verify this migration with `MigrationTestHelper`.",
            "expected_answer_keywords": ["@Embedded parent entity", "@Relation with parentColumn and entityColumn", "Migration(1, 2) executing `database.execSQL(\"ALTER TABLE ...\")`", "AutoMigrationSpec", "MigrationTestHelper in instrumented tests", "preventing IllegalStateException / database corruption on update"]
        }
    ],
    "android_data_persistence.offline_first_synchronization": [
        {
            "level": "mid",
            "type": "architectural_trade_off",
            "question": "Design an offline-first repository architecture in Android for a field inspection app. How do you implement a sync engine where the UI exclusively observes Room database Flow (Single Source of Truth), user mutations are immediately written to local Room with a `syncState = PENDING` flag (optimistic UI), and a background worker syncs pending records with the server resolving conflicts with a Last-Write-Wins or server-reconciliation strategy?",
            "expected_answer_keywords": ["UI observes local Room database exclusively (SSOT)", "Optimistic UI update (`syncState = PENDING`)", "NetworkBoundResource / Flow sync pattern", "Conflict resolution (Last-Write-Wins, server timestamps)", "Sync queue processed via WorkManager", "error retry and rollback strategy"]
        }
    ],
    "android_data_persistence.encrypted_storage_keystore": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "A fintech application requires hardware-backed encryption for user session tokens and OAuth refresh tokens. Explain how the Android KeyStore system generates and stores cryptographic keys inside the Trusted Execution Environment (TEE) / StrongBox Keymaster. Walk through configuring `EncryptedSharedPreferences` with `MasterKey.Builder(context).setKeyScheme(MasterKey.KeyScheme.AES256_GCM).build()`.",
            "expected_answer_keywords": ["Android KeyStore hardware isolation (TEE / StrongBox)", "MasterKey.Builder with AES256_GCM key scheme", "EncryptedSharedPreferences (Jetpack Security)", "keys never exposed in application memory", "BiometricPrompt CryptoObject integration for key authentication", "preventing root inspection of tokens"]
        }
    ],
    "android_data_persistence.room_paging3_integration": [
        {
            "level": "senior",
            "type": "scenario",
            "question": "Implement infinite scrolling for a 1-million-item feed using Room and the Android Paging 3 library. Design a custom `RemoteMediator<Int, PostEntity>` that coordinates network page fetching with local database caching: explain how `RemoteKeys` are stored in the database to track next/prev page tokens, how `LoadType.REFRESH`, `APPEND`, and `PREPEND` are handled, and how `PagingData` flows directly to the UI.",
            "expected_answer_keywords": ["Paging 3 `RemoteMediator` implementation", "RemoteKeys entity for next/prev cursor tracking", "LoadType.REFRESH (clear DB and keys)", "LoadType.APPEND / PREPEND", "PagingConfig with pageSize, prefetchDistance", "PagingData Flow collected in Compose via `collectAsLazyPagingItems()`"]
        }
    ],
    "android_data_persistence.sqlite_advanced_indexing": [
        {
            "level": "senior",
            "type": "debugging",
            "question": "A query `SELECT * FROM messages WHERE chat_id = ? AND timestamp > ? ORDER BY timestamp DESC` takes 600ms on an Android device with 500,000 messages. Walk through optimizing this in Room: using SQLite `EXPLAIN QUERY PLAN` to detect a full table scan (`SCAN TABLE`), designing an optimal composite index `@Entity(indices = [Index(value = [\"chat_id\", \"timestamp\"])])`, and enabling Write-Ahead Logging (`WAL` mode) with `@Transaction` batching.",
            "expected_answer_keywords": ["SQLite `EXPLAIN QUERY PLAN` analysis", "SCAN TABLE vs SEARCH TABLE USING INDEX", "composite index order (`chat_id`, `timestamp DESC`)", "Write-Ahead Logging (`WAL` mode) for concurrent reads during writes", "@Transaction for atomic batch inserts", "query time reduced from 600ms to <2ms"]
        }
    ],
    "android_data_persistence.network_resilience_caching": [
        {
            "level": "senior",
            "type": "architectural_trade_off",
            "question": "Design a high-resilience networking layer for Android using OkHttp. How do you configure HTTP response caching with `Cache-Control` interceptors to enable stale-while-revalidate offline viewing, implement an exponential backoff retry interceptor with random jitter for idempotent endpoints, and enforce Certificate Pinning with `CertificatePinner` while ensuring safe backup pin rotation before certificate expiry?",
            "expected_answer_keywords": ["OkHttp Cache with custom offline `Cache-Control: public, only-if-cached, max-stale=...`", "exponential backoff retry interceptor with jitter", "CertificatePinner with SHA-256 public key hashes", "primary and backup pins for zero-downtime certificate rotation", "MitM attack prevention", "network state awareness (ConnectivityManager)"]
        }
    ],

    # -------------------------------------------------------------
    # 6. android_concurrency_async (9 subskills)
    # -------------------------------------------------------------
    "android_concurrency_async.coroutines_basics_dispatchers": [
        {
            "level": "junior",
            "type": "code_review",
            "question": "A developer writes `GlobalScope.launch { val data = api.fetch(); textView.text = data }`. Identify the two critical bugs in this code (GlobalScope lifecycle leak and updating UI from background thread) and refactor it properly using `viewModelScope.launch`, `Dispatchers.IO` with `withContext`, and exposing state to the UI.",
            "expected_answer_keywords": ["GlobalScope causes coroutine memory leaks on Activity destroy", "Updating UI on background thread causes CalledFromWrongThreadException", "viewModelScope.launch manages lifecycle automatically", "suspend function handles dispatcher internally or withContext(Dispatchers.IO)", "updating UI on Dispatchers.Main"]
        }
    ],
    "android_concurrency_async.structured_concurrency_jobs": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "Explain the concept of Structured Concurrency in Kotlin Coroutines. Given a parent coroutine that launches two child coroutines (Child A and Child B), what happens if Child A throws an uncaught `RuntimeException`? How does `supervisorScope` / `SupervisorJob` change this failure propagation to prevent Child A's crash from cancelling Child B?",
            "expected_answer_keywords": ["Structured Concurrency: child coroutine lifecycles bound to parent scope", "Standard Job: uncaught exception in Child A cancels parent and all siblings (Child B)", "SupervisorJob / supervisorScope isolates child failures", "Child A failure does not cancel Child B", "CoroutineExceptionHandler on child scope"]
        }
    ],
    "android_concurrency_async.flow_fundamentals_cold_streams": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "Explain why standard Kotlin `Flow` is described as a 'cold stream' (code inside `flow { ... }` does not execute until collected). Contrast cold Flow with hot streams, write a cold flow that emits sensor data periodically, and demonstrate intermediate operators (`map`, `filter`) and the `catch` operator for upstream error handling.",
            "expected_answer_keywords": ["Cold stream: producer starts only when terminal operator (`collect`) is called", "Each collector gets independent stream execution", "Hot stream produces values regardless of active collectors", "`flow { while(true) { emit(sensor.read()); delay(1000) } }`", "`flow.map().filter().catch { emit(fallback) }.collect()`", "upstream exception handling"]
        }
    ],
    "android_concurrency_async.stateflow_sharedflow_hot_streams": [
        {
            "level": "mid",
            "type": "comparison",
            "question": "Compare `StateFlow` and `SharedFlow` in Android ViewModel architecture. Why is `StateFlow` ideal for UI state (holding a current value, conflation, replay=1) while `SharedFlow` is suited for one-shot events (navigation, snackbars)? Explain why `stateIn(scope, SharingStarted.WhileSubscribed(5000), initialValue)` is the recommended policy for UI state flows in Android.",
            "expected_answer_keywords": ["StateFlow holds current value (`.value`), conflates identical emissions, replay=1", "SharedFlow has no initial value, configurable replay cache and buffer overflow", "one-shot event modeling with SharedFlow / Channel", "`SharingStarted.WhileSubscribed(5000)` stops upstream when UI is in background", "5-second timeout handles orientation changes without restarting upstream"]
        }
    ],
    "android_concurrency_async.flow_transformations_combination": [
        {
            "level": "mid",
            "type": "code_review",
            "question": "In a search screen, a user types rapidly in an input field. Write a Flow transformation pipeline that: (1) ignores input under 300ms using `debounce(300)`, (2) filters out duplicate queries with `distinctUntilChanged()`, (3) cancels ongoing search requests if a new query arrives using `flatMapLatest`, and (4) combines search results with user preferences using `combine`.",
            "expected_answer_keywords": ["searchQueryFlow.debounce(300)", "distinctUntilChanged()", "flatMapLatest { query -> searchRepository.search(query) }", "cancelling in-flight requests on new query emission", "combine(userPreferencesFlow) { results, prefs -> ... }", "efficient reactive search pipeline"]
        }
    ],
    "android_concurrency_async.concurrency_synchronization_primitives": [
        {
            "level": "mid",
            "type": "debugging",
            "question": "Two concurrent coroutines running on `Dispatchers.Default` modify a shared `var counter = 0` concurrently, resulting in race conditions and incorrect counts. Why is Java `synchronized(lock)` an anti-pattern in coroutines (blocking the underlying carrier thread), and how do you resolve this using Kotlin Coroutines `Mutex.withLock` or `AtomicInteger`?",
            "expected_answer_keywords": ["Java `synchronized` blocks OS carrier thread causing thread starvation", "Kotlin `Mutex` suspends coroutine without blocking carrier thread", "Mutex.withLock { counter++ }", "AtomicInteger (`incrementAndGet()`) for lock-free atomic primitive mutations", "safe concurrent shared mutable state"]
        }
    ],
    "android_concurrency_async.coroutine_memory_leaks_profiling": [
        {
            "level": "senior",
            "type": "debugging",
            "question": "A developer collects a ViewModel `StateFlow` in a Fragment using `lifecycleScope.launch { viewModel.uiState.collect { ... } }`. When the user navigates away and the Fragment enters `onStop`, the flow collection continues in the background, wasting CPU and battery. Explain why `repeatOnLifecycle(Lifecycle.State.STARTED)` or `flowWithLifecycle` fixes this by automatically cancelling and restarting collection across lifecycle states.",
            "expected_answer_keywords": ["`lifecycleScope.launch` stays active while Fragment is in background (STOPPED/PAUSED)", "background flow collection wastes CPU, battery, and network", "`repeatOnLifecycle(Lifecycle.State.STARTED)` cancels coroutine on STOP and restarts on START", "safe UI state collection pattern", "Memory Profiler verification"]
        }
    ],
    "android_concurrency_async.reactive_streams_rxjava_migration": [
        {
            "level": "senior",
            "type": "architectural_trade_off",
            "question": "Your team is migrating a 200,000-line Android codebase from RxJava 3 (`Observable`, `Single`, `Flowable`, `PublishSubject`, `CompositeDisposable`) to Kotlin Coroutines and Flow. Detail the migration strategy: mapping Rx operators to Flow equivalents, bridging legacy RxJava services with `kotlinx-coroutines-rx3` (`asFlow()`, `asObservable()`, `awaitSingle()`), and comparing backpressure models (RxJava reactive pull vs Kotlin Flow suspension).",
            "expected_answer_keywords": ["Single -> suspend function", "Observable/Flowable -> Flow", "PublishSubject -> SharedFlow / Channel", "CompositeDisposable -> CoroutineScope cancellation", "`asFlow()` and `asObservable()` interop via `kotlinx-coroutines-rx3`", "suspension-based backpressure (no MissingBackpressureException) vs RxJava pull backpressure"]
        }
    ],
    "android_concurrency_async.custom_coroutine_context_testing": [
        {
            "level": "senior",
            "type": "scenario",
            "question": "Write a unit test for a ViewModel that debounces search queries and emits UI state. Explain how to use Kotlin Coroutines Test library with `runTest`: replacing `Dispatchers.Main` with `StandardTestDispatcher` via a JUnit Rule (`MainDispatcherRule`), controlling virtual time with `advanceTimeBy(300)` and `advanceUntilIdle()`, and asserting sequential Flow emissions using the `Turbine` testing library (`viewModel.uiState.test { awaitItem() }`).",
            "expected_answer_keywords": ["`runTest` with virtual time control", "MainDispatcherRule setting Dispatchers.setMain(testDispatcher)", "StandardTestDispatcher (explicit time advancement)", "advanceTimeBy(300) to trigger debounce", "advanceUntilIdle() to complete pending coroutines", "Turbine library `test { val item = awaitItem(); expectNoEvents() }`"]
        }
    ],

    # -------------------------------------------------------------
    # 7. android_platform_services_quality (9 subskills)
    # -------------------------------------------------------------
    "android_platform_services_quality.runtime_permissions_model": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "Implement modern Android runtime permissions for camera access on Android 13+: explain using `ActivityResultContracts.RequestPermission()` with `registerForActivityResult`, checking permission state with `ContextCompat.checkSelfPermission`, showing user-friendly rationale dialogs with `shouldShowRequestPermissionRationale`, and handling permanent denial by directing users to App Settings.",
            "expected_answer_keywords": ["ActivityResultContracts.RequestPermission", "registerForActivityResult launcher", "ContextCompat.checkSelfPermission", "shouldShowRequestPermissionRationale", "handling permanent denial (directing to Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS))", "Photo Picker alternative without permissions"]
        }
    ],
    "android_platform_services_quality.unit_testing_mockk_junit5": [
        {
            "level": "junior",
            "type": "code_review",
            "question": "Write a clean unit test in Kotlin using JUnit 5 and MockK for `UserViewModel`: mock the `UserRepository` with `mockk<UserRepository>()`, stub a suspend call using `coEvery { repository.getUser(any()) } returns Result.Success(mockUser)`, execute the ViewModel function, and verify the call with `coVerify(exactly = 1) { repository.getUser(eq(\"123\")) }`.",
            "expected_answer_keywords": ["MockK library (`mockk<T>()`)", "stubbing suspend functions with `coEvery { ... } returns ...`", "verifying suspend calls with `coVerify(exactly = 1) { ... }`", "JUnit 5 / JUnit 4 assertions", "testing state transitions deterministically"]
        }
    ],
    "android_platform_services_quality.notifications_channels_manager": [
        {
            "level": "junior",
            "type": "scenario",
            "question": "Build a notification system for an Android e-commerce app: create a `NotificationChannel` with `IMPORTANCE_HIGH` (Android 8+ requirement), construct a rich notification with `NotificationCompat.Builder` using `BigTextStyle` and action buttons, attach a `PendingIntent` with `PendingIntent.FLAG_IMMUTABLE`, and request the runtime `POST_NOTIFICATIONS` permission on Android 13+.",
            "expected_answer_keywords": ["NotificationChannel creation with NotificationManager", "NotificationCompat.Builder", "NotificationManagerCompat.from(context).notify()", "PendingIntent with `FLAG_IMMUTABLE`", "BigTextStyle expandable notification", "POST_NOTIFICATIONS runtime permission (Android 13)"]
        }
    ],
    "android_platform_services_quality.espresso_ui_testing": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "Write an automated UI test for an authentication screen using Jetpack Compose Testing API (`createAndroidComposeRule`): find the email input field with `onNodeWithTag(\"email_input\")`, perform text entry with `performTextInput(\"user@test.com\")`, click the login button with `performClick()`, and assert that the welcome text is displayed with `assertIsDisplayed()`. Contrast Compose testing with traditional Espresso `onView(withId(...))` testing.",
            "expected_answer_keywords": ["ComposeTestRule / createAndroidComposeRule", "SemanticsNode interaction (`onNodeWithTag`, `onNodeWithText`)", "performTextInput and performClick", "assertIsDisplayed / assertTextEquals", "Compose auto-synchronization vs Espresso IdlingResource", "testTags for semantic UI matching"]
        }
    ],
    "android_platform_services_quality.location_camera_hardware_services": [
        {
            "level": "mid",
            "type": "scenario",
            "question": "Build an in-app document scanner feature: configure `CameraX` API using `ProcessCameraProvider` with `Preview` and `ImageCapture` use cases attached to the Activity lifecycle. For geotagging the photo, request background/foreground location using Google Play Services `FusedLocationProviderClient` with `Priority.PRIORITY_HIGH_ACCURACY` and handle battery-efficient single location updates.",
            "expected_answer_keywords": ["CameraX `ProcessCameraProvider`", "Preview and ImageCapture use case binding", "LifecycleOwner binding", "FusedLocationProviderClient for location", "Priority.PRIORITY_HIGH_ACCURACY", "single update via `getCurrentLocation()` vs continuous `requestLocationUpdates()`", "battery optimization"]
        }
    ],
    "android_platform_services_quality.memory_leak_detection_leakcanary": [
        {
            "level": "mid",
            "type": "debugging",
            "question": "LeakCanary detects a memory leak in your Android app: `Activity instance leaked through static Handler in MyCustomView`. Walk through diagnosing this leak from the HPROF heap dump retain chain: explain how an anonymous `Handler` or `Runnable` implicitly retains an outer `Activity` reference, why pending messages in the `MessageQueue` prevent garbage collection, and how to fix it using a static class with `WeakReference<Activity>`.",
            "expected_answer_keywords": ["LeakCanary heap dump (.hprof) analysis", "GC root retain reference chain", "non-static inner class / Handler implicitly retains outer Activity instance", "pending message in Looper MessageQueue acts as GC root", "fix with static inner class and `WeakReference<Activity>`", "clearing callbacks on `onDestroy` (`removeCallbacksAndMessages(null)`)"]
        }
    ],
    "android_platform_services_quality.ci_cd_gradle_build_optimization": [
        {
            "level": "senior",
            "type": "governance_case_study",
            "question": "An enterprise Android build takes 22 minutes on CI/CD (GitHub Actions), slowing down pull request velocity. Walk through your Gradle build speed optimization strategy: enabling Gradle Configuration Cache, remote Build Cache, parallel execution (`org.gradle.parallel=true`), compiler daemon memory tuning, and configuring automated App Bundle (`.aab`) signing and Fastlane deployment to Play Store Internal Test tracks.",
            "expected_answer_keywords": ["Gradle Configuration Cache (`org.gradle.configuration-cache=true`)", "Remote Gradle Build Cache", "parallel module compilation", "daemon heap tuning (`-Xmx6g`)", "Fastlane `supply` / `upload_to_play_store`", "signed Android App Bundle (.aab) generation", "build time reduced from 22m to <4m"]
        }
    ],
    "android_platform_services_quality.crash_reporting_observability": [
        {
            "level": "senior",
            "type": "debugging",
            "question": "Your Android app has a 99.2% crash-free user rate, but Google Play Android Vitals reports a high ANR (Application Not Responding) rate of 1.4% (above the 0.47% bad behavior threshold). Walk through diagnosing ANRs using Google Play Console traces and Firebase Crashlytics: analyzing `traces.txt` main thread state (BLOCKED on lock vs continuous I/O vs heavy JSON parsing), and setting up custom Crashlytics keys and non-fatal exception logs to reproduce production issues.",
            "expected_answer_keywords": ["Google Play Android Vitals ANR threshold (<0.47%)", "ANR trace analysis (`traces.txt`)", "main thread state: BLOCKED on monitor lock vs TIMED_WAITING vs RUNNABLE in heavy computation", "moving main-thread disk/network I/O to Dispatchers.IO", "FirebaseCrashlytics.setCustomKey / recordException", "StrictPolicy enforcement in debug builds"]
        }
    ],
    "android_platform_services_quality.security_obfuscation_tamper_proofing": [
        {
            "level": "senior",
            "type": "governance_case_study",
            "question": "Hardening a banking Android application against reverse engineering and runtime tampering: author comprehensive R8 / ProGuard rules that obfuscate class and method names while preserving serialization models (`-keepattributes *Annotation*`, `@Keep`), integrate Google Play Integrity API to detect side-loaded or tampered APKs on the server, implement root detection (detecting su binaries, Magisk, Test-Keys), and verify APK signature schemes (v2/v3/v4).",
            "expected_answer_keywords": ["R8 code shrinking, optimization, and obfuscation", "ProGuard `-keep` rules for reflection/serialization models", "Google Play Integrity API (genuine app, genuine device, genuine license verdicts)", "root detection (su binary, Magisk mount checks, build tags)", "APK Signature Scheme v2/v3/v4 verification", "preventing repackaging and tampering"]
        }
    ]
}

assessment_data = {
    "source_id": "assessment",
    "name": "Adaptive Technical Assessment - Android Developer",
    "description": "Adaptive assessment question bank for Android Developer skills. Each question is hand-crafted and technology-specific with diverse scenario, debugging, architectural, code analysis, and trade-off formats.",
    "sample_questions_by_composite_key": questions
}

output_path = os.path.join(base_dir, 'evidence', 'android', 'assessment.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(assessment_data, f, indent=2, ensure_ascii=False)

print(f"Written evidence/android/assessment.json with {len(questions)} composite keys.")
