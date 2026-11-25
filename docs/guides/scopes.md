---
title: "Working with scopes"
description: "Choose where a configuration value belongs"
---

# Working with scopes

| Setting | Recommended scope |
| --- | --- |
| Preferred editor | Global user |
| Organization tracker URL | Context shared |
| Personal tracker account | Context personal |
| Project service port | Project shared |
| Personal project preference across worktrees | Project personal |
| Machine-specific checkout path | Checkout local |
| CI token binding | Trusted execution environment |

A context groups projects and optionally inherits from another context. Profiles select environments such as development or production independently of ownership. A production overlay within the project scope can still be overridden by a permitted personal scope; enforce production restrictions through policy rather than relying on precedence.

To remove your own override, reset it. To suppress an inherited value, unset it. To represent a deliberately null value, set null. See [composition](../specification/composition.md).
