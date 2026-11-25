---
title: "Integrating applications"
description: "Adopt the standard without coupling to a runtime"
---

# Integrating applications

Start with a stable component ID and a trusted declaration. Define a JSON Schema, explicit defaults, logical secret names, allowed scopes and sensitive destinations. Register the declaration through a trusted installation mechanism.

Three integration approaches are possible:

1. Existing application: an adapter maps explicitly declared values and authorized secrets to a narrowly scoped child environment.
2. CLI consumer: invoke a resolver through a documented non-secret JSON response and protected secret channel.
3. Native integration: use a library implementing the same resolution semantics.

The reference CLI is planned, not implemented. Example future commands such as konfig load and konfig explain are illustrative only. A consumer should distinguish missing configuration from provider failure and avoid automatic prompts in unattended mode. Verify service connectivity explicitly after configuration is valid.
