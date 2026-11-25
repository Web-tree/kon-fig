---
title: "Core model and terminology"
description: "Scope, design goals and data model"
---

# Core model and terminology

## Scope

Kon-Fig defines the configuration contract between a component, a resolver and an operator. It covers discovery, layered composition, schema validation, provenance, secret binding and safe lifecycle operations. It does not prescribe a programming language, process architecture, password manager, hosted control plane or configuration programming language.

## Terms

| Term | Meaning |
| --- | --- |
| Component | Stable logical consumer of configuration; several interfaces may intentionally share it |
| Declaration | Trusted, versioned description of a component's configuration |
| Layer | One ordered source of authored values, unsets and bindings |
| Scope | Ownership and applicability of a layer |
| Context | Named grouping of workspaces with optional parent |
| Project | Logical workspace identity shared across checkouts |
| Checkout | Physical instance of a project |
| Profile | Explicit execution-environment selector |
| Effective configuration | Composed and validated non-secret values |
| Binding | Reference to a provider for a logical secret |
| Principal | Operator, service identity or other authorized consumer |
| Policy | Non-overridable restrictions on resolution and delivery |

## Resolution request

A request identifies a component, declaration, principal, project/checkout (if any), selected profile (if any), applicable contexts and invocation overrides. The resolver MUST snapshot these inputs before composition. It MUST NOT infer an authenticated principal from a project file.

## Data model

Normative documents use UTF-8 JSON objects as defined in [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259). Reject duplicate keys, malformed UTF-8, non-finite numbers and integers outside the interoperable safe integer range (±9007199254740991). Other numeric values use IEEE 754 binary64 semantics. Keys are case-sensitive Unicode strings; identifier restrictions are separate. No implicit interpolation, evaluation, network fetching or type coercion is permitted. YAML/TOML adapters are optional and must map to this model without semantic loss.

## Versioning

The standard version, document format version, component schema version, and implementation version are independent. This draft specifies document format version 1. An unsupported format or schema dialect MUST fail rather than be guessed. Extensions MUST be explicitly negotiated; unknown security-critical extensions MUST fail.
