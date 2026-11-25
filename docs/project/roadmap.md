---
title: "Roadmap"
description: "From ACS extraction to an independent standard"
---

# Roadmap

## Draft phase
- Review the normative decisions and threat model.
- Complete machine-readable schemas and conformance vectors.
- Harden ACS regressions: provider timeouts, sanitized diagnostics, credential atomicity, validation, path safety and trust.

## Reference implementation
Extract reusable TypeScript core from ACS. Publish a standalone resolver/CLI; keep agent-specific discovery and onboarding in an adapter. Preserve legacy behavior through compatibility tests.

## Adoption
Validate with existing ACS consumers, an independent non-agent CLI (Runspore is a candidate), a CI use case and a no-code-change application adapter. Test on Linux, macOS and Windows.

## Stable release
Resolve open design decisions, perform security review, run conformance vectors against independent implementations, publish versioned documentation and schemas. No release date is committed.

## Later
Additional providers, native SDKs, standalone settings UI, synchronization adapters and deployment integrations. A hosted service, custom configuration language and mandatory daemon are not initial goals.
