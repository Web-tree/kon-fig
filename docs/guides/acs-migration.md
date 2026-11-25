---
title: "Migrating from Agent Config Standard"
description: "Preserve existing agent behavior"
---

# Migrating from Agent Config Standard

Kon-Fig builds on ACS 2.2, maintained in [Max-Levitskiy/skills](https://github.com/Max-Levitskiy/skills/blob/main/standards/agent-config.md).

The planned adapter keeps .agents paths, legacy declaration discovery, contexts, file keys, existing exit behavior and existing null-deletion/default semantics until a user explicitly migrates. Native format 1 uses literal null and explicit unset pointers instead. Never merge both stores silently.

Migration must map legacy names to registered component IDs, preserve layer ownership and context order, translate null operations according to observed legacy effective behavior (including default resurrection), separate credentials into atomic bindings, and require approval for new trust grants. Existing Git remote matches do not prove authorization. Legacy action files and harness hooks remain in the agent adapter.

Use a dry-run effective-value comparison, then migrate only approved layers, retaining recoverable backups. No migration tool is available in this repository yet.
