---
title: "Design decisions"
description: "Draft decisions requiring maintainer review"
---

# Design decisions

The following are proposed design decisions, not historical claims.

| Decision | Draft choice | Reason |
| --- | --- | --- |
| Data model | JSON, RFC 6901 pointers | Portable, deterministic |
| Deletion | Explicit unset; literal null preserved | Avoid overloaded null/default resurrection |
| Identity | Reverse-domain component ID; registered project identity | Prevent collisions and spoofing |
| Precedence | Scope-first, profile overlay within scope | Ownership independent of environment |
| Trust | Independent capability policy | Prevent project-controlled secret release |
| Validation | JSON Schema 2020-12 | Existing interoperable vocabulary |
| Discovery | Explicit registry, project manifest, optional Git | Support non-agent and non-Git consumers |
| Paths | Origin-relative, policy-constrained | Portable and safer |
| Context match | Exact/segment-prefix in native v1 | Avoid cross-runtime glob ambiguity; ACS adapter retains old globs |
| License | Proposed split CC BY/Apache | Requires approval |
| Site | Plain Markdown plus YAML metadata/navigation | No framework lock-in |

Open design work: canonical registry/policy exchange format, provider-specific contracts beyond env, wire protocol, richer match language, declarative migration format, secret transport details, formal threat-model vectors, naming/package availability and license approval. These are not prerequisites to reviewing this initial draft, but unresolved normative requirements must be settled before stable release.
