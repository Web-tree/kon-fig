---
title: "Consumer interfaces"
description: "Language-independent interaction contract"
---

# Consumer interfaces

The standard does not require a CLI, SDK, server or daemon. A conforming resolver exposes the semantic operations inspect, validate, load and resolve requested secrets. A management implementation additionally supports edit, explain, migration and trust management.

## Requests and responses

A request identifies component ID, trusted declaration reference, workspace selection, profile, context selection, principal and optional typed overrides. Principal and grants MUST come from trusted runtime context, not untrusted request data. A successful load returns effective values, provenance and nonfatal diagnostics; it never returns resolved secrets in ordinary configuration output. An unsuccessful load returns diagnostics and no consumable configuration. Secret release is a separate authorized operation tied to the validated snapshot.

Example logical response:

```json
{
  "status": "ok",
  "componentId": "org.example.cli",
  "schemaVersion": 2,
  "values": {"port": 8080},
  "provenance": {"/port": {"layer": "project-shared", "profile": null}},
  "diagnostics": []
}
```

The transport and serialization of provenance source handles are implementation-specific in this draft. CLI adapters SHOULD use JSON on stdout for non-secret responses, sanitized stderr for diagnostics and documented nonzero exit codes on failure. Never put secrets in argv or normal stdout. On POSIX a dedicated descriptor is one possible transport; Windows and native SDKs may use equivalent protected channels.

## Interactive behavior

Interactive tools MAY render schema-driven forms or ask questions. Background services and CI use noninteractive mode. Onboarding prompts, agent actions, installation hooks and application-specific verification are integration concerns. A resolver MUST NOT execute instructions embedded in a schema or configuration merely because it is processing them.
