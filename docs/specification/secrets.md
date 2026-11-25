---
title: "Secrets and providers"
description: "Logical secrets, references and safe delivery"
---

# Secrets and providers

A trusted declaration defines named logical secrets, their required status and optional intended audience. Bindings live separately from values. A binding MUST be a provider reference, never a literal secret. Bindings are atomically replaced by higher scopes, not recursively merged.

Example of a personal binding:

```json
{
  "formatVersion": 1,
  "componentId": "org.example.cli",
  "schemaVersion": 2,
  "values": {},
  "bindings": {"apiToken": {"provider": "env", "parameters": {"name": "EXAMPLE_API_TOKEN"}}}
}
```

## Providers

The core defines the reference contract; implementations MAY offer named providers. A provider declares and validates its parameter schema and capabilities. Unknown providers MUST fail on resolution. Provider identifiers are lowercase ASCII names; third-party identifiers SHOULD be namespaced.

| Provider | Parameters | Capability |
| --- | --- | --- |
| env | name | Read approved environment variable |
| dotenv | path, name | Read approved local file with documented parsing rules |
| 1password | ref, optional account | Read approved vault reference |
| keychain | service, account | Read approved OS credential |
| command | executable, args | Execute explicitly approved executable |

The env provider MUST be supported by the secret-resolution conformance profile. Its name MUST match [A-Za-z_][A-Za-z0-9_]*; missing variables are errors, empty values are valid unless the declaration prohibits them. Other providers are optional; parameter semantics and executable behavior require separate provider specifications before interoperability claims. No implicit shell invocation is allowed.

## Resolution and delivery

Resolve only requested logical secrets for an authorized principal, component, context/project and profile. Validate the binding and audience policy against the same effective snapshot before invoking a provider. Providers MUST use bounded time, bounded output and sanitized errors. Noninteractive mode MUST fail if authentication requires user interaction.

Never store resolved secrets in configuration, journals, exports, logs, diagnostics, command-line arguments or ordinary stdout. Deliver via a native API, dedicated protected channel or narrowly scoped child-process environment. Cache is optional, memory-only by default, scoped to principal, component, binding identity and authorization, and invalidated on relevant changes. Do not treat ambient environment caching as a security boundary.

A consumer receiving a secret can misuse it; the resolver does not sandbox arbitrary applications. Enforce destination/audience at the consumer or a controlled transport when required.
