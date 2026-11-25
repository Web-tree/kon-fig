---
title: "Getting started"
description: "Understand configuration with a minimal example"
---

# Getting started

This is an illustrative example of the draft format, not an installation guide.

A tool declares its configuration in a trusted declaration. Suppose its ID is org.example.cli and it defaults to port 8080. A project may override the port with a layer document:

```json
{"formatVersion":1,"componentId":"org.example.cli","schemaVersion":1,"values":{"port":9000}}
```

A personal project layer may add a user preference. A checkout layer may override a local path. When a resolver combines these documents, each value has an identifiable source. The application receives the validated effective values; secrets are resolved separately only when needed.

Read [scopes](scopes.md), then [application integration](integration.md). Implementers should start with the [normative specification](../specification/index.md).
