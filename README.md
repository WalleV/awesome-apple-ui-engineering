# Awesome Apple UI Engineering

<!-- markdownlint-disable MD013 -->

> A curated field guide to production SwiftUI, UIKit, and AppKit engineering.

This guide is for engineers building, modernizing, or maintaining production Apple-platform interfaces with SwiftUI, UIKit, AppKit, or a mix of them.

## Contents

- [Start Here](#start-here)
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

## Start Here

- **Migrating UIKit/AppKit to SwiftUI** — Begin with [Interoperability and Migration](#interoperability-and-migration), then use Apple's [UIKit Integration](https://developer.apple.com/documentation/swiftui/uikit-integration) or [AppKit Integration](https://developer.apple.com/documentation/swiftui/appkit-integration) guidance to choose a hosting or representable bridge.
- **Choosing a UI architecture** — Start with the platform's built-in state tools, then use [Architecture and State](#architecture-and-state) when side effects, navigation, dependencies, or deterministic testing justify an additional layer.
- **Diagnosing performance problems** — Start with [SwiftUI Performance Analysis](https://developer.apple.com/documentation/swiftui/performance-analysis), then follow [Performance, Debugging, and Inspection](#performance-debugging-and-inspection) for hangs, scrolling, and mixed UI stacks.
- **Establishing UI testing** — Use [Testing, Previews, and Accessibility](#testing-previews-and-accessibility) to combine [Xcode UI automation](https://developer.apple.com/videos/play/wwdc2025/344/) for critical flows, [SnapshotTesting](https://github.com/pointfreeco/swift-snapshot-testing) for visual regressions, and accessibility audits with manual assistive-technology testing.

## Selection Policy

Resources in this guide should have a clear engineering purpose, first-party documentation, an identifiable license when code is distributed, and evidence that they remain useful with current Apple-platform development. Recent commits are a signal, not an absolute requirement: small, finished libraries may be stable without frequent changes.

This guide excludes generic Swift infrastructure, trivial visual demos, repositories without a usable license, and resources whose only differentiator is popularity.

### Entry Format

Each entry uses a short description followed by **Use when**, **Watch for**, and metadata. Metadata always follows this order: **Frameworks → Platforms → Requirements → License**.

Omit fields that do not apply or cannot be verified. Use canonical framework and platform names, explicit deployment, toolchain, or hardware requirements, and SPDX license identifiers—or the exact upstream license name when no SPDX identifier exists. Topics, content types, and conference years belong in the description rather than the metadata line.

## Official Foundations

- [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui) — Apple's primary SwiftUI API reference.
  - **Use when:** Verifying SwiftUI APIs before adopting compatibility packages or introspection.
  - **Watch for:** Confirm API availability for every deployment target.
  - **Metadata:** `Frameworks: SwiftUI` · `Platforms: All Apple platforms`

- [UIKit Documentation](https://developer.apple.com/documentation/uikit) — Apple's primary reference for UIKit interface infrastructure.
  - **Use when:** Working with view controllers, responders, collection views, or presentation on UIKit platforms.
  - **Watch for:** Confirm platform and OS-version availability for the APIs you adopt.
  - **Metadata:** `Frameworks: UIKit` · `Platforms: iOS, iPadOS, tvOS`

- [AppKit Documentation](https://developer.apple.com/documentation/appkit) — Apple's primary reference for native macOS interfaces.
  - **Use when:** Building windows, controls, menus, documents, text systems, or event handling with AppKit.
  - **Watch for:** Confirm macOS-version availability for the APIs you adopt.
  - **Metadata:** `Frameworks: AppKit` · `Platforms: macOS`

- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) — Apple's platform design guidance.
  - **Use when:** Evaluating whether a reusable component behaves like a native control, not merely whether it looks similar.
  - **Watch for:** Treat the guidance as product constraints rather than implementation code.
  - **Metadata:** `Platforms: All Apple platforms`

- [SwiftUI Tutorials](https://developer.apple.com/tutorials/swiftui) — Apple's maintained SwiftUI learning path.
  - **Use when:** Learning composition, data flow, navigation, drawing, animation, and cross-platform adaptation.
  - **Watch for:** Use it as a canonical foundation, not as a production architecture guide.
  - **Metadata:** `Frameworks: SwiftUI`

- [UIKit Integration](https://developer.apple.com/documentation/swiftui/uikit-integration) — Apple's index for SwiftUI and UIKit interoperability.
  - **Use when:** Hosting SwiftUI in UIKit or wrapping UIKit views and controllers for SwiftUI.
  - **Watch for:** Choose the bridge that matches whether you are integrating a view, controller, cell, or screen.
  - **Metadata:** `Frameworks: SwiftUI, UIKit`

- [AppKit Integration](https://developer.apple.com/documentation/swiftui/appkit-integration) — Apple's index for SwiftUI and AppKit interoperability.
  - **Use when:** Hosting SwiftUI in AppKit or wrapping AppKit views, menus, and scenes.
  - **Watch for:** Test sizing, focus, lifecycle, and responder behavior at the framework boundary.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS`

- [Use SwiftUI with AppKit and UIKit](https://developer.apple.com/videos/play/wwdc2026/272/) — WWDC26 guidance for incremental SwiftUI adoption.
  - **Use when:** Sharing observable models or introducing SwiftUI into an existing AppKit or UIKit application.
  - **Watch for:** Some capabilities require the 2026 OS releases or explicit back-deployment configuration.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `Requirements: 2026 OS releases for some capabilities, or explicit back-deployment configuration`

- [What's New in SwiftUI](https://developer.apple.com/videos/play/wwdc2026/269/) — WWDC26 overview of SwiftUI features and tooling.
  - **Use when:** Surveying the current SwiftUI release before reading feature-specific documentation.
  - **Watch for:** Treat it as a version-specific entry point and check API availability separately.
  - **Metadata:** `Frameworks: SwiftUI`

## Architecture and State

- [The Composable Architecture](https://github.com/pointfreeco/swift-composable-architecture) — An opinionated architecture for state, effects, navigation, dependencies, and testing.
  - **Use when:** Complex feature domains need deterministic behavior and a consistent composition model across SwiftUI and UIKit.
  - **Watch for:** Its concepts, macros, and framework-wide adoption cost are excessive for many small apps.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `License: MIT`

- [Dependencies](https://github.com/pointfreeco/swift-dependencies) — Controllable live, preview, and test dependencies inspired by SwiftUI's environment.
  - **Use when:** You need deterministic previews and tests with or without The Composable Architecture.
  - **Watch for:** Key-based registration can hide dependencies unless the team defines clear boundaries.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: MIT`

- [Sharing](https://github.com/pointfreeco/swift-sharing) — Shared-state tools for memory, app storage, files, and custom persistence.
  - **Use when:** State must cross SwiftUI and UIKit feature boundaries with explicit test support.
  - **Watch for:** Indiscriminate global sharing can increase coupling.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `License: MIT`

- [Perception](https://github.com/pointfreeco/swift-perception) — A back-port of Observation-style modeling and bindability.
  - **Use when:** Supporting deployment targets that predate native Observation.
  - **Watch for:** It adds annotations and tracking wrappers; projects targeting only modern systems should prefer platform APIs.
  - **Metadata:** `Frameworks: SwiftUI` · `License: MIT`

## Navigation and Presentation

- [Swift Navigation](https://github.com/pointfreeco/swift-navigation) — State-driven navigation and presentation primitives.
  - **Use when:** Stacks, sheets, popovers, alerts, or deep links must be modeled and tested across UI frameworks.
  - **Watch for:** The additional domain modeling may be unnecessary for a small NavigationStack app.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: MIT`

- [RouteComposer](https://github.com/ekazaev/route-composer) — Protocol-oriented routing for large UIKit controller hierarchies.
  - **Use when:** Navigation steps must compose while validating an existing controller hierarchy.
  - **Watch for:** Its configuration vocabulary and abstraction layer require deliberate team adoption.
  - **Metadata:** `Frameworks: UIKit` · `Platforms: iOS` · `License: MIT`

- [Navigator](https://github.com/hmlongco/Navigator) — Modular SwiftUI routing built on NavigationStack.
  - **Use when:** You need deep links, restoration, checkpoints, logging, or navigation debugging.
  - **Watch for:** Version 2 introduces its own stack and destination abstractions.
  - **Metadata:** `Frameworks: SwiftUI` · `Platforms: iOS` · `Requirements: iOS 17+` · `License: MIT`

## Interoperability and Migration

- [UIHostingController](https://developer.apple.com/documentation/swiftui/uihostingcontroller) — Hosts a SwiftUI hierarchy inside UIKit.
  - **Use when:** Incrementally adding a SwiftUI screen to an existing UIKit controller tree.
  - **Watch for:** Containment, traits, sizing, lifecycle, and state ownership remain integration responsibilities.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `Platforms: iOS` · `Requirements: iOS 13+`

- [UIHostingConfiguration](https://developer.apple.com/documentation/swiftui/uihostingconfiguration) — Places SwiftUI content in UIKit list cells.
  - **Use when:** Table or collection cells use UIContentConfiguration and need lightweight SwiftUI content.
  - **Watch for:** It targets cell content, not whole-screen controller hosting.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `Platforms: iOS` · `Requirements: iOS 16+`

- [UIViewRepresentable](https://developer.apple.com/documentation/swiftui/uiviewrepresentable) — Wraps an existing UIView for use in SwiftUI.
  - **Use when:** A mature UIKit view has behavior that SwiftUI does not provide directly.
  - **Watch for:** Make creation, updates, delegates, sizing, and bidirectional state flow explicit.
  - **Metadata:** `Frameworks: SwiftUI, UIKit`

- [UIViewControllerRepresentable](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable) — Wraps an existing UIViewController for use in SwiftUI.
  - **Use when:** Integrating camera, document picker, media, or business controllers that cannot be expressed as one view.
  - **Watch for:** Dismissal and controller lifecycle remain the integrator's responsibility.
  - **Metadata:** `Frameworks: SwiftUI, UIKit`

- [NSHostingView](https://developer.apple.com/documentation/swiftui/nshostingview) — Hosts a SwiftUI hierarchy inside an AppKit view tree.
  - **Use when:** Adopting SwiftUI without converting the owning AppKit window or controller.
  - **Watch for:** Verify fitting size, focus, and responder-chain behavior in the containing layout.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS`

- [NSViewRepresentable](https://developer.apple.com/documentation/swiftui/nsviewrepresentable) — Wraps an existing NSView for use in SwiftUI.
  - **Use when:** Mature AppKit text, canvas, media, or other views exceed current SwiftUI capabilities.
  - **Watch for:** Make lifecycle, sizing, coordinator behavior, and state synchronization explicit.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS`

- [SwiftUI Introspect](https://github.com/siteline/swiftui-introspect) — Exposes selected public UIKit or AppKit objects behind SwiftUI views.
  - **Use when:** A required platform configuration is still missing from native SwiftUI APIs.
  - **Watch for:** Prefer native APIs, opt in to each supported OS version, and regression-test major OS upgrades.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: MIT`

- [NSUI](https://github.com/mattmassicotte/NSUI) — A source-compatibility layer for UIKit and AppKit type-name differences.
  - **Use when:** Shared UI code differs mainly by UIKit and AppKit type names.
  - **Watch for:** It cannot erase semantic differences in layout, events, and lifecycle.
  - **Metadata:** `Frameworks: UIKit, AppKit` · `License: BSD-3-Clause`

## Layout, Components, and Interaction

- [SwiftUIX](https://github.com/SwiftUIX/SwiftUIX) — A broad collection of SwiftUI components and UIKit/AppKit bridges.
  - **Use when:** Filling a specific SwiftUI component or integration gap.
  - **Watch for:** Its large 0.x surface should be adopted component by component, not as an unquestioned foundation.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: MIT`

- [Epoxy](https://github.com/airbnb/epoxy-ios) — Airbnb's declarative UIKit infrastructure for screens and components.
  - **Use when:** Building collection views, navigation, presentations, bars, or layout groups in a large UIKit codebase.
  - **Watch for:** It is a substantial architectural layer and can become migration cost for a product moving entirely to SwiftUI.
  - **Metadata:** `Frameworks: UIKit` · `License: Apache-2.0`

- [Blueprint](https://github.com/square/Blueprint) — A value-type declarative UIKit element tree.
  - **Use when:** Studying or building a component system with layout, transitions, and accessibility infrastructure.
  - **Watch for:** SwiftUI can host Blueprint, but the inverse integration is intentionally limited.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `License: Apache-2.0`

- [IGListKit](https://github.com/Instagram/IGListKit) — A mature data-driven UICollectionView architecture.
  - **Use when:** Building heterogeneous, frequently updating feeds in UIKit.
  - **Watch for:** Compare its section-controller model with native diffable data sources before adding a second list architecture.
  - **Metadata:** `Frameworks: UIKit` · `License: MIT`

- [PinLayout](https://github.com/layoutBox/PinLayout) — Fluent manual layout for UIKit, AppKit, and CALayer.
  - **Use when:** Animation-heavy or performance-sensitive hierarchies benefit from explicit frame calculation.
  - **Watch for:** Frame calculation remains the application's responsibility throughout the layout lifecycle.
  - **Metadata:** `Frameworks: UIKit, AppKit` · `License: MIT`

- [FlexLayout](https://github.com/layoutBox/FlexLayout) — A Swift API over Yoga's Flexbox engine.
  - **Use when:** Complex UIKit components benefit from Flexbox layout, often alongside PinLayout.
  - **Watch for:** Teams must deliberately adopt Flexbox semantics and explicit invalidation.
  - **Metadata:** `Frameworks: UIKit` · `License: MIT`

- [Texture](https://github.com/TextureGroup/Texture) — An asynchronous node-based UI and list system.
  - **Use when:** Demanding feeds need layout, text measurement, and image work moved away from the main thread.
  - **Watch for:** It requires a high-cost ASDisplayNode architecture and currently lacks Swift Package Manager support.
  - **Metadata:** `Frameworks: UIKit` · `License: Apache-2.0`

- [HorizonCalendar](https://github.com/airbnb/HorizonCalendar) — A production calendar with UIKit and SwiftUI interfaces.
  - **Use when:** You need a calendar component or a reference for dual-framework API design.
  - **Watch for:** It is a focused component, not a general UI framework.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `License: Apache-2.0`

- [charcoal-ios](https://github.com/pixiv/charcoal-ios) — A real-world design system with UIKit and SwiftUI modules.
  - **Use when:** Studying how shared typography and accessibility rules can span two UI frameworks.
  - **Watch for:** Its pixiv-specific tokens and styling are not a drop-in generic theme.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `License: Apache-2.0`

## Images, Media, and Text

- [Nuke and NukeUI](https://github.com/kean/Nuke) — Image loading, decoding, caching, prefetching, and SwiftUI presentation.
  - **Use when:** Building an application-level image pipeline across SwiftUI, UIKit, or AppKit.
  - **Watch for:** Version 13 has a modern Swift/Xcode and deployment baseline; define cache, privacy, and cancellation policy yourself.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: MIT`

- [Lottie iOS](https://github.com/airbnb/lottie-ios) — Airbnb's vector-animation runtime for SwiftUI, UIKit, and macOS.
  - **Use when:** Rendering designer-authored vector animations in SwiftUI, UIKit, or macOS applications.
  - **Watch for:** Review complex files for package size, CPU/GPU use, memory, accessibility labels, and Reduce Motion.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: Apache-2.0`

- [STTextView](https://github.com/krzyzanowskim/STTextView) — A TextKit 2 editor with advanced editing features.
  - **Use when:** You need line numbers, multiple cursors, search, or system text services across AppKit, UIKit, and SwiftUI.
  - **Watch for:** Its GPL-3.0-or-commercial license is a first-order constraint, and it is not a transparent system text-view replacement.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: GPL-3.0-or-commercial`

- [CodeEditTextView](https://github.com/CodeEditApp/CodeEditTextView) — A Core Text editor optimized for large code documents.
  - **Use when:** Fast first layout matters for line-oriented text editing on macOS.
  - **Watch for:** It does not match every NSTextView behavior; syntax and indentation belong in higher layers.
  - **Metadata:** `Frameworks: AppKit` · `Platforms: macOS` · `License: MIT`

- [RichTextKit](https://github.com/danielsaidi/RichTextKit) — A cross-platform rich-text editor and viewer with a SwiftUI API.
  - **Use when:** Editing attributed text through UITextView and NSTextView from a shared interface.
  - **Watch for:** The maintainer is reassessing its direction as newer system attributed-text editing arrives; isolate the dependency.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: MIT`

## Testing, Previews, and Accessibility

- [SnapshotTesting](https://github.com/pointfreeco/swift-snapshot-testing) — Extensible image and value snapshot testing.
  - **Use when:** SwiftUI, UIKit, or AppKit output needs deterministic visual or value regression tests.
  - **Watch for:** Pin simulator, OS, font, locale, appearance, and scale in CI to avoid environmental false positives.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: MIT`

- [iOSSnapshotTestCase](https://github.com/uber/ios-snapshot-test-case) — A long-running UIKit image-regression framework.
  - **Use when:** Maintaining existing Objective-C or Swift snapshot test estates built around UIKit and Core Animation.
  - **Watch for:** Test-host and reference-directory conventions are more manual than newer alternatives.
  - **Metadata:** `Frameworks: UIKit` · `License: MIT`

- [AccessibilitySnapshot](https://github.com/cashapp/AccessibilitySnapshot) — Visualizes accessibility metadata alongside UIKit snapshots.
  - **Use when:** Catching regressions in hierarchy, labels, traits, order, and activation points.
  - **Watch for:** It cannot replace VoiceOver, Switch Control, Dynamic Type, or manual assistive-technology testing.
  - **Metadata:** `Frameworks: UIKit` · `License: Apache-2.0`

- [Prefire](https://github.com/BarredEwe/Prefire) — Reuses Xcode previews as tests and component documentation.
  - **Use when:** Turning SwiftUI or UIKit previews into snapshot cases, playbooks, or living documentation.
  - **Watch for:** Validate build-plugin permissions and sandbox behavior in the intended CI system.
  - **Metadata:** `Frameworks: SwiftUI, UIKit` · `License: Apache-2.0`

- [Perform accessibility audits for your app](https://developer.apple.com/videos/play/wwdc2023/10035/) — Apple's WWDC23 XCTest accessibility-audit workflow.
  - **Use when:** Discovering common accessibility issues during UI tests.
  - **Watch for:** Automated audits are a baseline, not proof of a usable experience.
  - **Metadata:** `Frameworks: XCTest`

- [Build accessible apps with SwiftUI and UIKit](https://developer.apple.com/videos/play/wwdc2023/10036/) — WWDC23 guidance for accessible semantics and interaction.
  - **Use when:** Designing grouping, actions, rotors, direct touch, and equivalent experiences across SwiftUI and UIKit.
  - **Watch for:** Validate the result with the assistive technologies and interaction modes your users rely on.
  - **Metadata:** `Frameworks: SwiftUI, UIKit`

- [Record, replay, and review: UI automation with Xcode](https://developer.apple.com/videos/play/wwdc2025/344/) — Apple's WWDC25 workflow for generating and reviewing UI automation.
  - **Use when:** Recording interactions to bootstrap Xcode UI tests.
  - **Watch for:** Generated steps still need stable accessibility identifiers and deliberate assertions.
  - **Metadata:** `Frameworks: XCTest`

## Performance, Debugging, and Inspection

- [SwiftUI Performance Analysis](https://developer.apple.com/documentation/swiftui/performance-analysis) — Apple's entry point for analyzing SwiftUI updates.
  - **Use when:** Measuring long view updates and unnecessary invalidation.
  - **Watch for:** Use it as a measurement workflow, not a checklist of speculative micro-optimizations.
  - **Metadata:** `Frameworks: SwiftUI`

- [Optimize SwiftUI performance with Instruments](https://developer.apple.com/videos/play/wwdc2025/306/) — A practical WWDC25 SwiftUI profiling workflow in Instruments.
  - **Use when:** Investigating long body updates, representable updates, hangs, or Cause & Effect relationships.
  - **Watch for:** Some trace features require the corresponding Xcode, Instruments, and OS versions.
  - **Metadata:** `Frameworks: SwiftUI`

- [Demystify SwiftUI performance](https://developer.apple.com/videos/play/wwdc2023/10160/) — A WWDC23 conceptual model for SwiftUI performance.
  - **Use when:** Interpreting profiler output through dependency graphs, update scope, identity, and list behavior.
  - **Watch for:** Pair the concepts with the newer Instruments workflow.
  - **Metadata:** `Frameworks: SwiftUI`

- [Profile, fix, and verify app responsiveness](https://developer.apple.com/videos/play/wwdc2026/268/) — A WWDC26 measure-fix-verify workflow for app hangs with Instruments.
  - **Use when:** Diagnosing responsiveness across mixed SwiftUI, UIKit, and AppKit applications.
  - **Watch for:** Profile integrated application flows, not only isolated views.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit`

- [Dive into lazy stacks and scrolling](https://developer.apple.com/videos/play/wwdc2026/321/) — WWDC26 guidance for SwiftUI lazy layout and scrolling.
  - **Use when:** Investigating identity, layout, or performance in scrolling collections.
  - **Watch for:** Confirm availability before transferring 2026 APIs to back-deployed code.
  - **Metadata:** `Frameworks: SwiftUI`

- [Inject](https://github.com/krzysztofzablocki/Inject) — An integration layer for InjectionIII-powered hot reload.
  - **Use when:** Shortening the SwiftUI, UIKit, or AppKit development feedback loop.
  - **Watch for:** It depends on Debug linker and build configuration and does not replace previews or automated testing.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit` · `License: MIT`

- [Build programmatic UI with Xcode Previews](https://developer.apple.com/videos/play/wwdc2023/10252/) — WWDC23 guidance for previewing programmatic interfaces.
  - **Use when:** Building #Preview harnesses for multiple SwiftUI, UIKit, or AppKit states.
  - **Watch for:** Previews do not replace lifecycle, performance, device, or accessibility validation.
  - **Metadata:** `Frameworks: SwiftUI, UIKit, AppKit`

## macOS and AppKit Engineering

- [Integrating AppKit](https://developer.apple.com/tutorials/app-dev-training/integrating-appkit) — Apple's worked NSViewRepresentable example.
  - **Use when:** Learning the basic shape of exposing an AppKit view through SwiftUI.
  - **Watch for:** Complex focus, sizing, coordinator, and reverse-hosting behavior needs additional design.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS`

- [Developing a Document-Based App](https://developer.apple.com/documentation/appkit/developing-a-document-based-app) — Apple's canonical NSDocument sample.
  - **Use when:** Learning open/save, document lifecycle, and window-controller patterns in AppKit.
  - **Watch for:** Do not assume its architecture maps directly to SwiftUI DocumentGroup or FileDocument.
  - **Metadata:** `Frameworks: AppKit` · `Platforms: macOS`

- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) — The macOS-specific Human Interface Guidelines.
  - **Use when:** Designing windows, menus, keyboard interaction, pointer behavior, or desktop information density.
  - **Watch for:** It provides product constraints rather than implementation recipes.
  - **Metadata:** `Platforms: macOS`

- [What's new in AppKit](https://developer.apple.com/videos/play/wwdc2024/10124/) — WWDC24 coverage of current AppKit capabilities.
  - **Use when:** Reviewing hosting menus, SwiftUI-driven animation, tiling, toolbars, text, and panels.
  - **Watch for:** Many examples are macOS 15-era additions; annotate availability in production code.
  - **Metadata:** `Frameworks: AppKit` · `Platforms: macOS`

- [WindowSceneKit](https://github.com/Kyome22/WindowSceneKit) — Turns custom NSWindow types into SwiftUI scenes.
  - **Use when:** You need typed window payloads and programmatic open or close behavior.
  - **Watch for:** It is an emerging project with a modern Swift/Xcode baseline; validate a representative multi-window flow.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS` · `License: MIT`

- [Settings](https://github.com/sindresorhus/Settings) — A multi-pane preferences-window framework.
  - **Use when:** AppKit view controllers and SwiftUI need native toolbar or segmented settings styles.
  - **Watch for:** Pure SwiftUI apps targeting only recent macOS releases may not need the extra controller layer.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS` · `License: MIT`

- [SettingsAccess](https://github.com/orchetect/SettingsAccess) — Opens and observes a SwiftUI Settings scene.
  - **Use when:** A menu-bar app or similar context cannot conveniently use the default Settings command.
  - **Watch for:** Newer macOS versions cover part of the need, and menu-style MenuBarExtra retains documented limitations.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS` · `License: MIT`

- [MenuBarExtraAccess](https://github.com/orchetect/MenuBarExtraAccess) — Adds programmatic access to SwiftUI MenuBarExtra internals.
  - **Use when:** Controlling visibility or reaching the underlying NSStatusItem or popup window is necessary.
  - **Watch for:** It bridges system implementation details and therefore demands current-OS regression tests.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS` · `License: MIT`

- [KeyboardShortcuts](https://github.com/sindresorhus/KeyboardShortcuts) — User-customizable global shortcuts for macOS.
  - **Use when:** Users need shortcut recording, conflict feedback, sandbox support, or Mac App Store compatibility.
  - **Watch for:** It complements rather than replaces menu key equivalents and responder-chain commands.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS` · `License: MIT`

- [WelcomeWindow](https://github.com/CodeEditApp/WelcomeWindow) — A native welcome window for document apps.
  - **Use when:** Presenting recent files, new/open actions, and drag and drop in an NSDocument application.
  - **Watch for:** Its narrow conventions should match the owning NSDocumentController lifecycle.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS` · `License: MIT`

- [AdvancedCollectionTableView](https://github.com/flocked/AdvancedCollectionTableView) — AppKit list infrastructure with SwiftUI cell hosting.
  - **Use when:** You need registration, content configuration, diffable updates, or hosted SwiftUI cells in AppKit lists.
  - **Watch for:** The project directs consumers to its main branch, so pin and test the exact revision.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS` · `License: MIT`

- [VirtualBuddy](https://github.com/insidegui/VirtualBuddy) — A native macOS virtualization app and AppKit case study.
  - **Use when:** Testing UI across macOS versions or studying a substantial native application.
  - **Watch for:** It does not reproduce every physical-device condition.
  - **Metadata:** `Frameworks: AppKit` · `Platforms: macOS` · `Requirements: Apple silicon` · `License: BSD-2-Clause`

## Sample Apps and Case Studies

- [Using SwiftUI with UIKit](https://github.com/apple-sample-code/UsingSwiftUIWithUIKit) — Apple's WWDC22 SwiftUI-in-UIKit sample.
  - **Use when:** Learning to add SwiftUI views and cell content to an existing UIKit application.
  - **Watch for:** Update its data-flow choices for the current SDK rather than copying them unchanged.
  - **Metadata:** `Frameworks: SwiftUI, UIKit`

- [Bringing Robust Navigation Structure to Your SwiftUI App](https://github.com/apple-sample-code/BringingRobustNavigationStructureToYourSwiftUIApp) — Apple's value-driven SwiftUI navigation sample.
  - **Use when:** Studying deep links, restoration, and navigation modeled as values.
  - **Watch for:** Its 2022 model code predates Observation.
  - **Metadata:** `Frameworks: SwiftUI`

- [Bringing Multiple Windows to Your SwiftUI App](https://github.com/apple-sample-code/BringingMultipleWindowsToYourSwiftUIApp) — Apple's compact SwiftUI multi-window sample.
  - **Use when:** Studying scene state and multi-window behavior on iPadOS and macOS.
  - **Watch for:** Verify current scene APIs instead of copying the original project configuration verbatim.
  - **Metadata:** `Frameworks: SwiftUI` · `Platforms: iPadOS, macOS`

- [Food Truck](https://github.com/apple/sample-food-truck) — Apple's multiplatform SwiftUI sample application.
  - **Use when:** Studying split navigation, custom layout, charts, widgets, and Live Activities in one codebase.
  - **Watch for:** It is a WWDC22 sample, not a current production template.
  - **Metadata:** `Frameworks: SwiftUI` · `License: MIT`

- [CodeEdit](https://github.com/CodeEditApp/CodeEdit) — A large native macOS editor case study.
  - **Use when:** Studying workspaces, multi-window UI, settings, terminals, text editing, and SwiftUI/AppKit boundaries.
  - **Watch for:** The project remains in development and is not recommended for production use.
  - **Metadata:** `Frameworks: SwiftUI, AppKit` · `Platforms: macOS` · `License: MIT`

- [IINA](https://github.com/iina/iina) — A mature native macOS media player.
  - **Use when:** Studying complex windows, menus, preferences, input handling, localization, plugins, and media UI.
  - **Watch for:** Its GPL-3.0 license and external media stack matter if code is reused.
  - **Metadata:** `Frameworks: AppKit` · `Platforms: macOS` · `License: GPL-3.0`

- [NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire) — A long-running native feed reader for macOS and iOS.
  - **Use when:** Studying shared modules, platform-specific interfaces, widgets, tests, and themes in a large codebase.
  - **Watch for:** Study decisions in context instead of treating longevity as universal architecture guidance.
  - **Metadata:** `Frameworks: UIKit, AppKit` · `Platforms: iOS, macOS` · `License: MIT`

- [IceCubesApp](https://github.com/Dimillian/IceCubesApp) — A multiplatform Mastodon client built in SwiftUI.
  - **Use when:** Studying dedicated iPhone, iPad, macOS, visionOS, widget, and extension experiences.
  - **Watch for:** Its AGPL-3.0 license matters when adapting source, and product-specific tradeoffs should not be generalized blindly.
  - **Metadata:** `Frameworks: SwiftUI` · `Platforms: iOS, iPadOS, macOS, visionOS` · `License: AGPL-3.0`

## License

© 2026 WalleV. Except where otherwise noted, the original text and curation in this repository are licensed under the [Creative Commons Attribution 4.0 International License](LICENSE).

Linked projects, trademarks, logos, and other third-party materials remain subject to their respective licenses and rights.
