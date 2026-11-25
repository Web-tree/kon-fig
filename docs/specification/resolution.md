---
title: "Validation and resolution"
description: "Deterministic validation and diagnostics"
---

# Validation and resolution

## Resolution stages

A resolver MUST validate the trusted declaration and each present layer envelope, resolve compatible schema versions, evaluate applicability and trust, compose values and bindings, normalize declared paths, validate effective values against the structural schema, and check policy before releasing results or resolving any secrets. It MUST NOT execute providers while inspecting, describing or validating configuration.

Partial layers need not satisfy required-property constraints for the full effective schema. Invalid final values MUST block load and execution. Invalid or disallowed authored operations MUST be rejected even if later overridden when they violate format, scope or security rules.

Distinguish configuration readiness from external connectivity. A valid secret reference is not proof a credential works; verification is an explicitly requested consumer operation.

## Diagnostics

Use stable machine-readable codes: invalid-document, unsupported-format, unknown-component, ambiguous-component, invalid-schema, stale-schema, future-schema, invalid-value, missing-value, missing-binding, policy-denied, untrusted-source, context-conflict, provider-unavailable, provider-timeout, provider-failed, path-denied, write-conflict, internal-error. Include severity, component ID and applicable pointers/layer IDs. Messages MUST be sanitized and MUST NOT contain resolved secrets or raw provider output.

Non-interactive resolution MUST NOT prompt, install software, migrate files or change trust. Inspection MAY return incomplete data with diagnostics, but successful load MUST return only validated data. A failed secret resolution MUST NOT release partial secret results. All limits and timeouts MUST be finite and documented.
