---
title: "Documents and schemas"
description: "Normative configuration envelopes and declarations"
---

# Documents and schemas

## Layer document

A layer document contains the formatVersion, componentId, schemaVersion, values, optional unset pointers and optional bindings. Metadata never merges into application values.

```json
{
  "formatVersion": 1,
  "componentId": "org.example.cli",
  "schemaVersion": 2,
  "values": {"server": {"port": 8080, "proxy": null}},
  "unset": ["/server/legacyEndpoint"]
}
```

See [layer schema](../../schemas/layer.schema.json). Empty values are allowed. Unknown top-level properties MUST fail in format 1. A shared document MUST NOT contain literal secrets or personal-only fields. A schema cannot detect arbitrary secrets hidden in ordinary strings; publishers and operators must classify sensitive fields correctly.

## Declaration

The trusted declaration defines component ID, schema version, structural schema, defaults, per-path metadata and logical secret requirements.

```json
{
  "formatVersion": 1,
  "id": "org.example.cli",
  "schemaVersion": 2,
  "schema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {"port": {"type": "integer", "minimum": 1}},
    "required": ["port"],
    "additionalProperties": false
  },
  "defaults": {"port": 8080}
}
```

See [declaration schema](../../schemas/declaration.schema.json). The structural schema uses JSON Schema Draft 2020-12. Full validation is required for the core profile; format is annotation-only unless a supported assertion vocabulary is declared. Only local references within the declaration schema are supported by format 1. Unsupported vocabularies or unresolved references MUST fail. Schema annotations never materialize defaults; the separate defaults object does.

Metadata keys are RFC 6901 JSON Pointers identifying object properties, not array elements. Metadata can describe allowed scopes, recommended scope, atomic merge, personal-only or security-sensitive classification, and input file/folder type. Recommendations never override policy. Restrictions on an ancestor apply to descendants and cannot be relaxed by child metadata. Unknown properties in metadata MUST fail.

A declaration default may be partial; the effective result must satisfy the full schema. Implementations MUST validate the declaration's own structure, schema, metadata and default types before accepting it. Secrets are declared separately and never embedded in values or defaults.
