---
title: "Lifecycle and migration"
description: "Safe updates, compatibility and portability"
---

# Lifecycle and migration

## Editing

Distinguish set (including literal null), reset (remove the operation at this layer), and unset (suppress inheritance). Edits require an explicit scope and, where relevant, profile. Validate proposed documents before persisting. Never silently edit a different scope. Use atomic replacement, restricted permissions for personal files, conflict detection using expected revision/digest, and locking or equivalent concurrency control. Multi-file transactions MUST be recoverable; a partial update cannot appear as a successful transaction.

## Schema evolution

Each layer declares the schema version it targets. A resolver MUST reject stale and future versions unless the trusted declaration explicitly describes compatibility. Migration is a separate authorized operation; load must not mutate files. Migration must preserve component identity, scope, profile, secret classification and authored intent. A dry run describes changes without secrets; deterministic migrations are preferred. Executable migration code is a privileged operation. Rollback must check current revisions and must not overwrite concurrent edits.

Retain a schema snapshot or immutable schema digest with sufficient access to reconstruct prior meaning. State records and backups MUST exclude resolved secrets and be access-controlled. Version changes to the standard do not imply component migrations.

## Import/export

Export shared, non-sensitive configuration and portable context definitions by default. Personal settings, provider references, machine-specific paths and trust grants are excluded unless explicitly selected and authorized; resolved secrets are never exported. Imports validate identity, schema and paths, preview changes, preserve ownership boundaries, and never grant trust automatically. Synchronization transport is out of scope; Git or other mechanisms may distribute shared documents.
