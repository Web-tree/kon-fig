---
title: "Composition and provenance"
description: "Deterministic merge and deletion semantics"
---

# Composition and provenance

## Composition algorithm

1. Start with a fresh copy of the trusted declaration defaults.
2. Enumerate layers in [scope order](scopes.md), including the selected profile overlay within each scope.
3. Check source eligibility, format, schema version, policy and scope restrictions before applying each layer.
4. Recursively merge the layer values. If both values are objects, merge member by member; otherwise replace with the higher value. Arrays, scalars, null and objects marked atomic replace wholesale. If the lower value is not an object and the higher is an object, start with an empty object.
5. Apply the layer's unset pointers after its values. A higher layer may explicitly set an unset value again.
6. Compose secret bindings separately; each logical binding is atomic. An explicit binding null suppresses inherited binding. Unsets in values do not affect bindings.
7. Validate the effective document and policy.

A pointer MUST use [RFC 6901](https://www.rfc-editor.org/rfc/rfc6901) escaping. Unset pointers MUST target non-root object properties only; traversal through arrays or scalars is invalid. Removing an absent property is a no-op. Overlapping unsets are applied shortest pointer first, then lexicographically. Unsets never delete array members. Defaults are never reapplied after composition. Reset removes an authored operation from the selected layer rather than setting an unset.

For each layer, conflicting set and unset at the same path is valid and unset wins. A higher layer setting a parent object may reintroduce children explicitly included in that object. All object access MUST operate on own data properties without prototype semantics.

## Provenance

Track the source for each surviving scalar, null, array and empty object, and for each leaf of ordinary objects. Track an atomic object at its root. Removing or replacing a subtree MUST discard stale descendant provenance. Include layer ID, profile, source document and pointer. Maintain diagnostics for discarded, blocked or unset operations without exposing sensitive contents. An explain operation SHOULD report the sequence of contributing/overridden operations.

## Example

Defaults: {"port": 80, "features": ["a","b"], "proxy": "auto"}.
Project: {"port": 8080, "features": ["c"], "proxy": null}.
Personal unset: ["/port"].
Result: {"features": ["c"], "proxy": null}. If port is required, validation fails; the default must not return.
