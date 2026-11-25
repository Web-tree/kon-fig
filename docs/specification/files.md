---
title: "Files and paths"
description: "Portable storage and path semantics"
---

# Files and paths

## Storage layout

Use a platform-appropriate user config root K (Linux: $XDG_CONFIG_HOME/konfig, fallback ~/.config/konfig; macOS: ~/Library/Application Support/Kon-Fig; Windows: %APPDATA%/Kon-Fig). An explicit operator override MAY select a different root. State such as journals and locks uses a separate platform state location; the root is never selected by project input.

Recommended layout (implementations claiming the filesystem profile MUST use these relative names):

```text
K/
  registry.json
  components/<component-id>/config.json
  components/<component-id>/projects/<encoded-project-id>/config.json
  contexts/<context-id>/context.json
  contexts/<context-id>/context.me.json
  contexts/<context-id>/components/<component-id>/config.json
  contexts/<context-id>/components/<component-id>/config.me.json
<checkout>/.konfig/
  project.json
  components/<component-id>/config.json
  components/<component-id>/config.local.json
```

For every base document named X.json, profile P uses sibling X.profile.P.json (including config.me.profile.P.json and config.local.profile.P.json). System storage uses the platform administrator-controlled root with the same components layout. Checkout-local files SHOULD be ignored by version control and MUST NOT be trusted merely because ignored. Shared and personal stores MUST be kept distinct. Registry serialization is implementation-specific in this draft; exchanging registry authorization is not supported.

## File and folder values

A trusted declaration may classify a property as an input file or folder. The winning value's relative path resolves against the document that supplied it; defaults resolve against the declaration directory. Environment/invocation path bindings require an explicitly supplied trusted base. Relative path semantics MUST NOT depend on process cwd. Absolute paths require permission. Untrusted sources are confined to their approved document directory after canonicalization. Require the declared file/folder kind and existence. Output destinations and executable files require separate policy; an input file grant is not an execution grant.

Do not merge file contents or automatically read them into configuration. Return normalized paths plus provenance only. Consumers must enforce containment when actually opening a file, including nested accesses within folders.
