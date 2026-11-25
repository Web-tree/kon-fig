---
title: "Scopes, contexts and profiles"
description: "Ownership, precedence and selection"
---

# Scopes, contexts and profiles

## Scope order

Lowest to highest:

1. Declaration defaults.
2. Optional system defaults.
3. Global user.
4. Each selected context: shared, then personal.
5. Project shared.
6. Project personal (across approved checkouts).
7. Checkout local.
8. Explicit environment bindings.
9. Invocation overrides.

Absent layers are skipped; invalid or unreadable present layers MUST be reported, not silently skipped. Security policy is independent of precedence. Non-applicable scopes MUST NOT be materialized.

## Context selection

A context has a stable ID, optional parent ID and matching rules. Definitions are registered outside the project. Matching rules are ORed. Parent contexts are included whenever a descendant matches. A context with no rules is abstract and applies only by explicit selection or ancestry. Parent cycles, missing parents and duplicate IDs are errors.

For format 1, rules are typed exact/prefix matches on canonical project IDs, canonical absolute paths (segment boundaries), or normalized Git remote host/path. Remote normalization lowercases the host, removes transport/user info and a final .git suffix, retains non-default ports and path case, and rejects ambiguous encodings. Git remote rules MAY select non-privileged shared defaults but MUST NOT authorize personal values or secrets. Personal applicability requires an operator-approved association of the current workspace/principal to the context.

Order selected roots by explicit operator-defined order, then ASCII ID order; visit each root depth-first, parents before children and siblings by explicit order then ASCII ID. Include each context once. Report overlapping writes by unrelated contexts, including ancestor/descendant key paths and unsets. Deterministic precedence still applies unless policy requires rejecting conflicts. An explicit context selector adds the named context and ancestors; it does not bypass trust. A no-context selector excludes all contexts.

## Profiles

Select zero or one profile by explicit request or a trusted operator-controlled environment binding. No project document may select its own profile. Within each applicable scope, base precedes its selected profile overlay; the next scope then follows. Other profiles MUST NOT be loaded. Unknown explicitly requested profiles MUST fail unless registered for the component. Profile names use lowercase ASCII letters, digits and hyphens, 1–64 characters. No implicit inheritance between profiles.

A production profile does not confer authority. Restrict it separately using policy.

## Environment and invocation

Only trusted declaration-defined environment bindings are considered. Each binding declares a JSON Pointer and encoding (string or JSON). Missing variables contribute nothing; an empty string is a value, not absence. Invalid encoding MUST fail. Invocation overrides use the same typed document operations. Neither source bypasses validation, allowed-scope rules or policy.
