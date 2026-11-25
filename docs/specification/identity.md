---
title: "Identity and discovery"
description: "Stable component and project identities"
---

# Identity and discovery

## Component identity

A component ID MUST be a lowercase reverse-domain-style identifier with at least two dot-separated ASCII segments, each matching `[a-z0-9](?:[a-z0-9-]*[a-z0-9])?`. Maximum length 253 characters. IDs are stable across package names, versions and runtimes. A local alias is only a lookup convenience and MUST NOT be used for authorization. Duplicate registrations with distinct publishers MUST fail until the operator selects an authorized declaration.

An identifier is not proof of domain ownership. Declaration authenticity MUST be established by trusted registration, installation or a verified digest pinned by the operator. Project files MUST NOT replace a registered declaration or change its trust policy.

## Project identity

A project ID is an opaque, locally registered UUID or a stable publisher-assigned ID mapped by the operator to an approved workspace. A project manifest and Git remotes are discovery hints, not authorization. IDs MUST NOT be used as unchecked filesystem paths. Use a reversible safe encoding or collision-resistant digest for path components, with explicit collision detection. A changed origin or cloned project MUST NOT automatically inherit privileged authorization.

## Discovery

The caller MAY explicitly select a registered declaration and workspace. Otherwise discover the nearest ancestor containing .konfig/project.json, stopping at the filesystem root; if absent, a Git adapter MAY discover the current repository. Nested project manifests take precedence over enclosing manifests. Without a workspace, project and checkout layers are absent, but applicable path contexts can still apply. Worktree and clone associations are maintained by the registry, not inferred as authority from Git metadata.

Explicit selection MUST resolve conflicts deterministically. Missing declarations, ambiguous identities and invalid manifests MUST produce structured errors. Discovery MUST NOT run project code, follow unapproved declaration links or fetch remote schemas.
