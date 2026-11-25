---
title: "Security and trust"
description: "Threat model, capabilities and policy"
---

# Security and trust

## Threat model

Assume cloned projects, imported shared configuration, remote identifiers, symlinks, malformed documents and provider output can be attacker-controlled. A compromised operating system or authorized malicious consumer is outside the resolver's ability to protect.

## Source and authority

Trust is assigned by the local operator or authenticated administrative policy, not by document claims, Git tracking status, filenames or matching remote URLs. Personal storage requires ownership/access checks and explicit approval of project associations. Untracked checkout files are not inherently trusted.

Untrusted shared documents may contribute ordinary permitted values. They MUST NOT supply secret bindings, personal-only fields, executable actions, arbitrary local paths, or security-sensitive destination changes without explicit authorized policy. Reject violations rather than silently granting them. Shared team policy is not automatically trusted just because it is in a team file.

## Capabilities

Policy decisions are independent of configuration precedence and cannot be relaxed by ordinary layers. Deny by default for secret release, arbitrary file access, command execution, network/schema fetching and extension loading. Approval identifies principal, component/declaration identity, capability, resource, workspace association, profile and content digest where executable content is involved. Revocation or changed approved content invalidates the grant. A grant to read a secret is not a grant to execute a command.

Bind credentials to an approved audience, account and destination where applicable. Validate security-sensitive effective fields before release; reject an unauthorized endpoint even when a secret reference itself is trusted. The consumer MUST enforce downstream audience restrictions that the resolver cannot verify.

## Filesystem and process safety

Validate all identifiers and pointer operations. Reject traversal, unsafe symlink escapes, prototype manipulation, duplicate keys and ambiguous encodings. Resolve paths within approved roots and avoid check/use races by using secure file handles or revalidation at consumption. Apply resource limits. Provider executable resolution MUST use a trusted executable path or trusted search path and a minimized environment. Do not forward unrelated credentials or raw stderr. Avoid exposing secrets in process metadata, temporary files, telemetry and crash diagnostics.

## Disclosure

Report suspected vulnerabilities privately via the repository's security contact once established. Until then, do not include exploit details or real credentials in public issues; ask maintainers for a private channel.
