# Initial conformance vectors

composition.json is a JSON array of cases. Each case contains id, defaults, optional atomic pointers, layers ordered lowest to highest, and expected effective values or a stable error code. Layers are operation fragments, not full envelopes; the runner supplies a valid declaration/envelope and an authorized test context. Compare JSON structures independent of object member order. Do not execute providers in these fixtures.

These vectors are an initial subset, not a complete conformance suite. See [conformance requirements](../docs/specification/conformance.md).
