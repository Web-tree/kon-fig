---
title: "Conformance"
description: "Implementation profiles and release gates"
---

# Conformance

## Claims

A conformance claim MUST name the exact specification version and profiles implemented. The draft defines the following profiles:

- Core: data model, identity inputs, deterministic scope ordering, composition, schema validation, provenance and diagnostics.
- Filesystem: Core plus discovery, paths and storage conventions.
- Secrets: Core plus policy enforcement, atomic bindings, authorized resolution and env provider.
- Management: Filesystem plus edits, migration, conflict detection and import/export.

A profile does not imply support for every optional provider or integration. No implementation has been certified. Implementations must document resource limits and platform deviations.

## Test vectors

The [fixture collection](../../conformance/README.md) is implementation-independent. The initial fixtures exercise composition only. Before a stable release, fixtures MUST also cover contexts, profiles, malformed JSON, pointer escaping, numeric boundaries, schema dialects, validation, unauthorized bindings, audience restrictions, identity spoofing, path containment, provider timeout and output leakage, concurrent writes and migration.

## Release gate

A stable standard requires schemas and normative prose to agree, complete positive and negative vectors for each required feature, at least two independently tested consumers (including a non-agent consumer), and an adversarial security review. Cross-platform claims require relevant OS testing. Passing only the initial fixtures is insufficient for a full conformance claim.
