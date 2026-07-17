# Awesome Apple UI Engineering

<!-- markdownlint-disable MD013 -->

> A curated field guide to production SwiftUI, UIKit, and AppKit engineering.

## Contents

- [Selection Policy](#selection-policy)
- [Official Foundations](#official-foundations)
- [Architecture and State](#architecture-and-state)
- [Navigation and Presentation](#navigation-and-presentation)
- [Interoperability and Migration](#interoperability-and-migration)
- [Layout, Components, and Interaction](#layout-components-and-interaction)
- [Images, Media, and Text](#images-media-and-text)
- [Testing, Previews, and Accessibility](#testing-previews-and-accessibility)
- [Performance, Debugging, and Inspection](#performance-debugging-and-inspection)
- [macOS and AppKit Engineering](#macos-and-appkit-engineering)
- [Sample Apps and Case Studies](#sample-apps-and-case-studies)
- [License](#license)

## Selection Policy

Resources in this guide should have a clear engineering purpose, first-party documentation, an identifiable license when code is distributed, and evidence that they remain useful with current Apple-platform development. Recent commits are a signal, not an absolute requirement: small, finished libraries may be stable without frequent changes.

Tags identify the primary UI frameworks, platforms, and licenses.

This guide excludes generic Swift infrastructure, trivial visual demos, repositories without a usable license, and resources whose only differentiator is popularity.

## Official Foundations

- [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui) - Primary API reference for declarative user interfaces across Apple platforms. Start here before adopting compatibility packages or introspection. `SwiftUI` `All Apple Platforms`
- [UIKit Documentation](https://developer.apple.com/documentation/uikit) - Primary API reference for iOS, iPadOS, and tvOS interface infrastructure, including view controllers, responder handling, collection views, and presentation. `UIKit` `iOS` `iPadOS` `tvOS`
- [AppKit Documentation](https://developer.apple.com/documentation/appkit) - Primary API reference for native macOS windows, controls, menus, documents, text, and event handling. `AppKit` `macOS`
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) - Apple's platform design guidance. Use it to evaluate whether a reusable component behaves like a native control rather than merely resembling one. `Design` `All Apple Platforms`
- [SwiftUI Tutorials](https://developer.apple.com/tutorials/swiftui) - Apple's maintained learning path covering composition, data flow, navigation, drawing, animation, and cross-platform adaptation. Best as a canonical foundation rather than a production architecture guide. `SwiftUI` `Tutorial`
- [UIKit Integration](https://developer.apple.com/documentation/swiftui/uikit-integration) - Apple's index for hosting SwiftUI inside UIKit and wrapping UIKit views and controllers for SwiftUI. `SwiftUI` `UIKit` `Interoperability`
- [AppKit Integration](https://developer.apple.com/documentation/swiftui/appkit-integration) - Apple's index for `NSHostingView`, `NSHostingController`, representable protocols, menus, scenes, and related AppKit bridges. `SwiftUI` `AppKit` `Interoperability`
- [Use SwiftUI with AppKit and UIKit](https://developer.apple.com/videos/play/wwdc2026/272/) - WWDC26 guidance for sharing observable models, adopting automatic observation in AppKit/UIKit update methods, and introducing SwiftUI incrementally. Some capabilities require the 2026 OS releases or explicit back-deployment configuration. `SwiftUI` `UIKit` `AppKit` `WWDC26`
- [What's New in SwiftUI](https://developer.apple.com/videos/play/wwdc2026/269/) - WWDC26 overview of the current SwiftUI feature set and tooling. Treat it as a version-specific entry point, not a substitute for API availability checks. `SwiftUI` `WWDC26`

## Architecture and State

- [The Composable Architecture](https://github.com/pointfreeco/swift-composable-architecture) - Opinionated architecture for composable state, side effects, navigation, dependencies, and deterministic testing across SwiftUI and UIKit. Excellent for complex feature domains; the concepts, macros, and framework-wide adoption cost are excessive for many small apps. `SwiftUI` `UIKit` `MIT`
- [Dependencies](https://github.com/pointfreeco/swift-dependencies) - Controllable live, preview, and test dependencies inspired by SwiftUI's environment, usable with or without TCA. Useful for deterministic previews and tests, but key-based registration can make dependencies implicit unless a team establishes clear boundaries. `SwiftUI` `UIKit` `AppKit` `MIT`
- [Sharing](https://github.com/pointfreeco/swift-sharing) - Shared-state tools for memory, app storage, files, and custom persistence with explicit testing support. Helps bridge state across SwiftUI and UIKit features; indiscriminate global sharing can increase coupling. `SwiftUI` `UIKit` `MIT`
- [Perception](https://github.com/pointfreeco/swift-perception) - Back-ports Observation-style modeling and bindability to older Apple operating systems. Valuable when deployment targets predate native Observation; it adds its own annotations and tracking wrappers, so projects targeting only modern systems should prefer the platform APIs. `SwiftUI` `Back Deployment` `MIT`

## Navigation and Presentation

- [Swift Navigation](https://github.com/pointfreeco/swift-navigation) - State-driven navigation primitives and dedicated SwiftUI/UIKit libraries for stacks, sheets, popovers, alerts, deep links, and testable presentation. The additional domain modeling may be unnecessary for a small `NavigationStack` app. `SwiftUI` `UIKit` `AppKit` `MIT`
- [RouteComposer](https://github.com/ekazaev/route-composer) - Protocol-oriented UIKit routing that composes navigation steps and validates the existing controller hierarchy before building new screens. Strong for large UIKit applications; its configuration vocabulary and abstraction layer require deliberate team adoption. `UIKit` `iOS` `MIT`
- [Navigator](https://github.com/hmlongco/Navigator) - Modular SwiftUI routing with deep links, restoration, checkpoints, logging, and debugging on top of `NavigationStack`. Version 2 targets iOS 17 or later and introduces its own stack and destination abstractions. `SwiftUI` `iOS` `MIT`

## Interoperability and Migration

- [UIHostingController](https://developer.apple.com/documentation/swiftui/uihostingcontroller) - Hosts a SwiftUI hierarchy inside an existing UIKit controller tree. Treat containment, traits, sizing, lifecycle, and state ownership as integration responsibilities rather than implementation details. `SwiftUI` `UIKit` `iOS 13+`
- [UIHostingConfiguration](https://developer.apple.com/documentation/swiftui/uihostingconfiguration) - The official lightweight path for placing SwiftUI content in table and collection cells that use `UIContentConfiguration`. It targets content, not whole-screen controller hosting. `SwiftUI` `UIKit` `iOS 16+`
- [UIViewRepresentable](https://developer.apple.com/documentation/swiftui/uiviewrepresentable) - Standard protocol for wrapping an existing `UIView` in SwiftUI. Production wrappers must make creation, updates, delegates, sizing, and bidirectional state flow explicit. `SwiftUI` `UIKit`
- [UIViewControllerRepresentable](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable) - Bridge for camera, document picker, media, and existing business controllers whose behavior cannot be expressed as one view. Dismissal and controller lifecycle remain the integrator's responsibility. `SwiftUI` `UIKit`
- [NSHostingView](https://developer.apple.com/documentation/swiftui/nshostingview) - Hosts a SwiftUI view hierarchy in an AppKit view tree, supporting incremental adoption without converting the owning window or controller. Verify fitting-size, focus, and responder-chain behavior in the containing AppKit layout. `SwiftUI` `AppKit`
- [NSViewRepresentable](https://developer.apple.com/documentation/swiftui/nsviewrepresentable) - Standard protocol for bringing an `NSView` into SwiftUI. Useful for mature text, canvas, media, and other AppKit assets whose capabilities exceed current SwiftUI controls. `SwiftUI` `AppKit`
- [SwiftUI Introspect](https://github.com/siteline/swiftui-introspect) - Finds the public UIKit or AppKit object behind selected SwiftUI views so missing platform configuration can be applied. Prefer native SwiftUI APIs, opt in to every supported OS version explicitly, and regression-test major OS upgrades. `SwiftUI` `UIKit` `AppKit` `MIT`
- [NSUI](https://github.com/mattmassicotte/NSUI) - A source-compatibility layer for UI code that differs mostly by UIKit/AppKit type names. It reduces conditional compilation but cannot erase semantic differences in layout, events, and lifecycle. `UIKit` `AppKit` `BSD-3-Clause`

## Layout, Components, and Interaction

- [SwiftUIX](https://github.com/SwiftUIX/SwiftUIX) - Broad collection of missing SwiftUI components and UIKit/AppKit bridges, including collection, text, picker, and hosting utilities. Its large 0.x API surface should be adopted component by component, not as an unquestioned foundation layer. `SwiftUI` `UIKit` `AppKit` `MIT`
- [Epoxy](https://github.com/airbnb/epoxy-ios) - Airbnb's declarative UIKit infrastructure for collection views, navigation, presentations, bars, and layout groups, used across many production screens. It is a substantial architectural layer and may be a transitional cost if a product is moving entirely to SwiftUI. `UIKit` `Apache-2.0`
- [Blueprint](https://github.com/square/Blueprint) - Value-type, declarative UIKit element tree with layout, transitions, and accessibility infrastructure. Strong as a component-system reference; SwiftUI can host Blueprint, but the inverse integration is intentionally limited. `UIKit` `SwiftUI` `Apache-2.0`
- [IGListKit](https://github.com/Instagram/IGListKit) - Mature data-driven `UICollectionView` architecture for heterogeneous, frequently updating feeds. Compare its section-controller model with native diffable data sources before adding a second list architecture. `UIKit` `MIT`
- [PinLayout](https://github.com/layoutBox/PinLayout) - Fluent manual layout for UIKit, AppKit, and `CALayer`, suited to animation-heavy or performance-sensitive hierarchies. Frame calculation remains the application's responsibility throughout the layout lifecycle. `UIKit` `AppKit` `MIT`
- [FlexLayout](https://github.com/layoutBox/FlexLayout) - Swift API over Yoga's Flexbox engine for complex UIKit component layout, commonly paired with PinLayout. Teams must deliberately adopt Flexbox semantics and explicit invalidation. `UIKit` `MIT`
- [Texture](https://github.com/TextureGroup/Texture) - Asynchronous node-based UI and list system that moves layout, text measurement, and image work away from the main thread. It can solve demanding feed performance, but requires a high-cost `ASDisplayNode` architecture and currently lacks Swift Package Manager support. `UIKit` `Apache-2.0`
- [HorizonCalendar](https://github.com/airbnb/HorizonCalendar) - Production calendar component with UIKit and SwiftUI interfaces built around the same declarative model. Useful both as a component and as a reference for dual-framework API design; it is not a general UI framework. `SwiftUI` `UIKit` `Apache-2.0`
- [charcoal-ios](https://github.com/pixiv/charcoal-ios) - A real brand design system with separate UIKit and SwiftUI modules plus shared typography and accessibility rules. Study its organization rather than treating pixiv-specific tokens and styling as a drop-in generic theme. `SwiftUI` `UIKit` `Design System` `Apache-2.0`

## Images, Media, and Text

- [Nuke and NukeUI](https://github.com/kean/Nuke) - Image loading, decoding, caching, prefetching, and SwiftUI `LazyImage` support across UIKit and AppKit. Version 13 requires a modern Swift/Xcode and deployment baseline; define cache, privacy, and cancellation policy at the application level. `SwiftUI` `UIKit` `AppKit` `MIT`
- [Lottie iOS](https://github.com/airbnb/lottie-ios) - Airbnb's vector-animation runtime with SwiftUI, UIKit, and macOS support. Complex animation files require package-size, CPU/GPU, memory, accessibility-label, and Reduce Motion review. `SwiftUI` `UIKit` `AppKit` `Apache-2.0`
- [STTextView](https://github.com/krzyzanowskim/STTextView) - TextKit 2 editor for AppKit, UIKit, and SwiftUI with line numbers, multiple cursors, search, and system text services. Its GPL-3.0-or-commercial license is a first-order adoption constraint, and it is not a transparent system text-view replacement. `SwiftUI` `UIKit` `AppKit` `GPL-3.0-or-commercial`
- [CodeEditTextView](https://github.com/CodeEditApp/CodeEditTextView) - Core Text-based editor optimized for fast first layout of large, line-oriented code documents on macOS. It deliberately does not match all `NSTextView` behaviors; syntax and indentation belong in higher layers. `AppKit` `macOS` `MIT`
- [RichTextKit](https://github.com/danielsaidi/RichTextKit) - Cross-platform rich-text editor and viewer over `UITextView` and `NSTextView` with a SwiftUI API. The maintainer is reassessing its direction as newer system attributed-text editing arrives, so isolate the dependency behind an application boundary. `SwiftUI` `UIKit` `AppKit` `MIT`

## Testing, Previews, and Accessibility

- [SnapshotTesting](https://github.com/pointfreeco/swift-snapshot-testing) - Extensible image and value snapshot testing for SwiftUI, UIKit, and AppKit. Pin simulator, OS, font, locale, appearance, and scale in CI or environment differences will masquerade as regressions. `SwiftUI` `UIKit` `AppKit` `MIT`
- [iOSSnapshotTestCase](https://github.com/uber/ios-snapshot-test-case) - Long-running UIKit and Core Animation image-regression framework, particularly relevant to existing Objective-C/Swift test estates. Its test-host and reference-directory conventions are more manual than newer alternatives. `UIKit` `MIT`
- [AccessibilitySnapshot](https://github.com/cashapp/AccessibilitySnapshot) - Visualizes the accessibility hierarchy, labels, traits, order, and activation points alongside UIKit snapshots. It catches regressions early but cannot replace VoiceOver, Switch Control, Dynamic Type, or manual assistive-technology testing. `UIKit` `Apache-2.0`
- [Prefire](https://github.com/BarredEwe/Prefire) - Reuses Xcode previews as snapshot cases, component playbooks, and living documentation for SwiftUI and UIKit. Validate build-plugin permissions and sandbox behavior in the intended CI system before adopting it broadly. `SwiftUI` `UIKit` `Apache-2.0`
- [Perform accessibility audits for your app](https://developer.apple.com/videos/play/wwdc2023/10035/) - Apple's XCTest accessibility-audit workflow for discovering common issues at UI-test time. Automated audits are a baseline, not proof of a usable experience. `Accessibility` `XCTest` `WWDC23`
- [Build accessible apps with SwiftUI and UIKit](https://developer.apple.com/videos/play/wwdc2023/10036/) - Practical Apple guidance on semantic grouping, actions, rotors, direct touch, and equivalent experiences across the two UI frameworks. `SwiftUI` `UIKit` `Accessibility` `WWDC23`
- [Record, replay, and review: UI automation with Xcode](https://developer.apple.com/videos/play/wwdc2025/344/) - Current Apple workflow for recording interactions, generating automation, and reviewing UI behavior. Generated steps still need stable accessibility identifiers and deliberate assertions. `XCTest` `UI Automation` `WWDC25`

## Performance, Debugging, and Inspection

- [SwiftUI Performance Analysis](https://developer.apple.com/documentation/swiftui/performance-analysis) - Apple's entry point for measuring long view updates and reducing unnecessary invalidation. Use it as a measurement workflow, not a checklist of speculative micro-optimizations. `SwiftUI` `Performance`
- [Optimize SwiftUI performance with Instruments](https://developer.apple.com/videos/play/wwdc2025/306/) - Demonstrates the SwiftUI instrument, long body and representable updates, hangs, and the Cause & Effect graph. Some trace features require the corresponding Xcode, Instruments, and OS versions. `SwiftUI` `Instruments` `WWDC25`
- [Demystify SwiftUI performance](https://developer.apple.com/videos/play/wwdc2023/10160/) - Explains dependency graphs, update scope, view identity, and list/table behavior—the model needed to interpret profiler output. Pair it with the newer Instruments workflow. `SwiftUI` `Performance` `WWDC23`
- [Profile, fix, and verify app responsiveness](https://developer.apple.com/videos/play/wwdc2026/268/) - A measure-fix-verify workflow for hangs and responsiveness using current Apple tooling. Apply the method to mixed UIKit, AppKit, and SwiftUI applications rather than profiling only isolated views. `Performance` `Instruments` `WWDC26`
- [Dive into lazy stacks and scrolling](https://developer.apple.com/videos/play/wwdc2026/321/) - Current Apple guidance for lazy layout, scrolling behavior, identity, and performance-sensitive SwiftUI collections. Confirm availability before transferring 2026 APIs to back-deployed code. `SwiftUI` `Scrolling` `WWDC26`
- [Inject](https://github.com/krzysztofzablocki/Inject) - Small integration layer for InjectionIII-powered hot reload in SwiftUI, UIKit, and AppKit development. It accelerates feedback but depends on Debug linker/build configuration and does not replace previews or automated testing. `SwiftUI` `UIKit` `AppKit` `MIT`
- [Build programmatic UI with Xcode Previews](https://developer.apple.com/videos/play/wwdc2023/10252/) - Shows `#Preview` across SwiftUI, UIKit, and AppKit, including multiple state variants. A preview is a development harness, not a substitute for full lifecycle, performance, device, or accessibility validation. `SwiftUI` `UIKit` `AppKit` `WWDC23`

## macOS and AppKit Engineering

- [Integrating AppKit](https://developer.apple.com/tutorials/app-dev-training/integrating-appkit) - Apple's worked example of exposing an `NSView` through `NSViewRepresentable`. It is a good bridge primer, but complex focus, sizing, coordinator, and reverse-hosting behavior needs additional design. `SwiftUI` `AppKit` `Tutorial`
- [Developing a Document-Based App](https://developer.apple.com/documentation/appkit/developing-a-document-based-app) - Canonical `NSDocument` sample covering open/save, document lifecycle, and window controllers. Do not assume its architecture maps directly to SwiftUI `DocumentGroup` or `FileDocument`. `AppKit` `Documents`
- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) - macOS-specific HIG covering windows, menus, keyboard, pointer, and desktop information density. It provides product constraints rather than implementation recipes. `macOS` `Design`
- [What's new in AppKit](https://developer.apple.com/videos/play/wwdc2024/10124/) - WWDC24 coverage of hosting menus, SwiftUI-driven AppKit animation, tiling, toolbars, text, and panels. Many examples are macOS 15-era additions, so annotate availability in production code. `AppKit` `WWDC24`
- [WindowSceneKit](https://github.com/Kyome22/WindowSceneKit) - Makes custom `NSWindow` types into SwiftUI scenes with typed payloads and programmatic open/close behavior. It is an emerging project with a modern Swift/Xcode baseline; validate it on a representative multi-window flow. `SwiftUI` `AppKit` `MIT`
- [Settings](https://github.com/sindresorhus/Settings) - Established multi-pane preferences-window framework supporting AppKit view controllers and SwiftUI, with native toolbar and segmented styles. Pure SwiftUI apps targeting only recent macOS releases may not need the extra controller layer. `SwiftUI` `AppKit` `MIT`
- [SettingsAccess](https://github.com/orchetect/SettingsAccess) - Opens and observes a SwiftUI Settings scene from contexts such as menu-bar apps where the default command is awkward. Newer macOS versions cover part of the need, and menu-style `MenuBarExtra` retains documented limitations. `SwiftUI` `AppKit` `MIT`
- [MenuBarExtraAccess](https://github.com/orchetect/MenuBarExtraAccess) - Adds programmatic visibility and access to the underlying `NSStatusItem` or popup window for a SwiftUI `MenuBarExtra`. It bridges system implementation details and therefore demands current-OS regression tests. `SwiftUI` `AppKit` `MIT`
- [KeyboardShortcuts](https://github.com/sindresorhus/KeyboardShortcuts) - User-customizable global shortcuts with SwiftUI and AppKit recorders, conflict feedback, sandbox, and Mac App Store support. It complements rather than replaces normal menu key equivalents and responder-chain commands. `SwiftUI` `AppKit` `MIT`
- [WelcomeWindow](https://github.com/CodeEditApp/WelcomeWindow) - Native welcome window for document apps with recent files, new/open actions, and drag and drop. Its conventions are intentionally narrow and should match the owning `NSDocumentController` lifecycle. `SwiftUI` `AppKit` `MIT`
- [AdvancedCollectionTableView](https://github.com/flocked/AdvancedCollectionTableView) - Registration, content configuration, diffable updates, and SwiftUI cell hosting for AppKit collection, table, and outline views. The project currently directs consumers toward its main branch, so pin and test the exact revision. `SwiftUI` `AppKit` `MIT`
- [VirtualBuddy](https://github.com/insidegui/VirtualBuddy) - Native macOS virtualization app useful for testing UI across macOS versions and beta releases, as well as a substantial AppKit case study. It requires Apple silicon and does not reproduce every physical-device condition. `AppKit` `Testing Tool` `BSD-2-Clause`

## Sample Apps and Case Studies

- [Using SwiftUI with UIKit](https://github.com/apple-sample-code/UsingSwiftUIWithUIKit) - Apple's WWDC22 sample for adding SwiftUI views and cell content to an existing UIKit application. Read it as an integration pattern, then update its data-flow choices for the current SDK. `SwiftUI` `UIKit` `Apple Sample Code`
- [Bringing Robust Navigation Structure to Your SwiftUI App](https://github.com/apple-sample-code/BringingRobustNavigationStructureToYourSwiftUIApp) - Apple's value-driven navigation, deep-linking, and restoration sample. It remains conceptually useful even though its 2022 model code predates Observation. `SwiftUI` `Navigation` `Apple Sample Code`
- [Bringing Multiple Windows to Your SwiftUI App](https://github.com/apple-sample-code/BringingMultipleWindowsToYourSwiftUIApp) - Compact Apple sample for scene state and multi-window behavior on iPadOS and macOS. Verify current scene APIs rather than copying its original project configuration verbatim. `SwiftUI` `iPadOS` `macOS` `Apple Sample Code`
- [Food Truck](https://github.com/apple/sample-food-truck) - Apple's multiplatform SwiftUI application demonstrating split navigation, custom layout, charts, widgets, and Live Activities from one codebase. It is an MIT-licensed WWDC22 sample, not a current production template. `SwiftUI` `Multiplatform` `MIT`
- [CodeEdit](https://github.com/CodeEditApp/CodeEdit) - Large native macOS editor for studying workspaces, multi-window UI, settings, terminal, text editing, and SwiftUI/AppKit boundaries. The project explicitly says it remains in development and is not recommended for production use. `SwiftUI` `AppKit` `MIT`
- [IINA](https://github.com/iina/iina) - Mature AppKit media player demonstrating complex windowing, menus, preferences, keyboard/mouse interaction, localization, plugins, and native media UI. Its GPL-3.0 license and external media stack matter if code is reused. `AppKit` `macOS` `GPL-3.0`
- [NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire) - Long-running MIT-licensed macOS and iOS feed reader with shared modules, platform-specific interfaces, widgets, tests, themes, and a sizable native codebase. Study decisions in context instead of treating longevity as universal architecture guidance. `UIKit` `AppKit` `iOS` `macOS` `MIT`
- [IceCubesApp](https://github.com/Dimillian/IceCubesApp) - Multiplatform Mastodon client built in SwiftUI with dedicated iPhone, iPad, macOS, visionOS, widget, and extension experiences. Its AGPL-3.0 license is important if adapting source, and product-specific tradeoffs should not be generalized blindly. `SwiftUI` `Multiplatform` `AGPL-3.0`

## License

© 2026 WalleV. Except where otherwise noted, the original text and curation in this repository are licensed under the [Creative Commons Attribution 4.0 International License](LICENSE).

Linked projects, trademarks, logos, and other third-party materials remain subject to their respective licenses and rights.
