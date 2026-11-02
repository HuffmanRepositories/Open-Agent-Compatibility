# OIX v0.1 ↔ A2A v1.0.0 specification assessment

**Assessment type:** E1 — specification review  
**Assessment date:** 2026-11-02  
**Status:** Preliminary; no runtime conformance or independent review

## Version pins and sources

- OIX protocol version **0.1**: [protocol specification](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange/blob/8c25c3b014eddaf074d5c86f0244e22140617728/protocol/oix-v0.1.md). OIX v0.1 is experimental, not a ratified standard. The source is pinned to immutable commit `8c25c3b014eddaf074d5c86f0244e22140617728`.
- A2A **v1.0.0**: [official versioned specification](https://a2a-protocol.org/v1.0.0/specification). This uses a versioned release URL, not moving main.
- Supporting source: [OIX README](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange/blob/main/README.md), [A2A v1.0 migration notes](https://github.com/a2aproject/A2A/blob/main/docs/whats-new-v1.md).

## Summary

**OIX v0.1 and A2A v1.0.0 overlap in agent communication, but are not interchangeable.**

OIX is a transport-independent signed message envelope with key-derived agent identity, capability labels, replay defenses, explicit local authorization, and evidence/provenance records. A2A defines richer Agent Cards, messages/parts, stateful tasks, artifacts, task operations, and streaming/push update mechanisms.

A bridge can translate some identity/capability/message concepts, but needs state and model conversion for A2A task/artifact semantics. Translating A2A into OIX v0.1 can flatten task events and lose structured artifacts, task context, stream behavior, and cancellation. A2A Agent Card authentication metadata and optional signatures are not equivalent to OIX’s signed card/message envelope. Security must be assessed separately.

## Concept-by-concept comparison

| Concept | OIX v0.1 | A2A v1.0.0 | OIX → A2A | A2A → OIX | Gap |
|---|---|---|---|---|---|
| Agent identity | Ed25519 fingerprint; signed card | Agent Card, service/interface identity; optional signature and web security | Transformed | Partial | Requires explicit trust/key binding. |
| Capability | String labels; local allowlist | Skills, interfaces, capability and auth metadata | Partial | Partial | Labels cannot represent full skill descriptions, endpoints, modalities and auth requirements. |
| Message | Signed envelope with sender/recipient/type/time/nonce/capability/payload | Message role, context/task association, Parts | Transformed | Transformed | OIX envelope metadata requires bridge-specific handling. |
| Task lifecycle | Message types for request/accepted/progress/result/error; no first-class task state machine | Task ID/context, defined states, retrieval/list/cancel/subscription | Partial | Lossy | OIX lacks A2A canonical task state and operation model. |
| Artifact/result | JSON payload; evidence is distinct | Artifact composed of Parts, task-associated | Partial | Lossy/partial | File/MIME/binary/url/grouping semantics require conventions. Evidence is not synonymous with artifact. |
| Progress/status | task.progress type, payload-defined details | TaskStatus and status-update events | Partial | Lossy | OIX has no equivalent normalized state enum/event contract. |
| Streaming | Single envelope; transport-neutral | Ordered streaming task/status/artifact events and subscriptions | Unsupported without extension | Lossy | One OIX envelope cannot model stream lifecycle/reconnect semantics. |
| Cancellation | No native cancel operation in v0.1 | Cancel Task with defined state semantics | Unsupported/application extension | Unsupported natively | App-level request does not guarantee A2A cancellation behavior. |
| Errors | error message; payload details not normalized | Protocol errors and task error/status details | Partial | Partial | Error taxonomy, correlation and retryability need rules. |
| Provenance/evidence | Explicit hash/source/time/method/collector/status/limitations fields | Artifact/Parts/task context; no equivalent universal evidence record | Partial | Lossy unless extension | Requires shared extension/schema to preserve evidence semantics. |
| Authentication/authorization | Ed25519 signatures, nonce/expiry/replay checks, capability allowlist; auth ≠ authorization | Binding security schemes, Agent Card auth requirements, optional card signatures | Not directly mapped | Not directly mapped | Transport auth, key trust, signatures, replay defense and policy are distinct controls. |
| Transport | Transport-independent envelope | JSON-RPC, gRPC, HTTP/REST bindings; streaming/push | Binding-specific | Binding-specific | Transport neutrality does not imply binding interoperability. |
| Extensions | Strict protocol version/type checks; JSON payload | A2A extension mechanism and versioned model | Not tested | Not tested | Need unknown-field/extension preservation policy. |

## Directional interpretation

### OIX → A2A

A bridge could validate OIX card/signature/TTL/nonce/recipient/capability; map configured OIX capability labels to A2A skills; translate task.request into an A2A SendMessage request; and correlate OIX message IDs with A2A task/context IDs.

**Caution:** A2A task updates, artifacts, streaming and cancellation are not representable faithfully by OIX v0.1 core alone. Do not claim native OIX support for bridge-defined conventions.

### A2A → OIX

A bridge could map a selected A2A skill to an OIX capability, create a signed request using a bridge identity and local authorization, then correlate OIX messages with A2A task/context and translate results.

**Caution:** A2A lifecycle, event history, artifact Parts, streaming and cancellation are not native OIX v0.1 concepts. Discrete OIX messages lose information unless bridge state/extensions preserve it.

## Companion fixture coverage

The [Open-Agent-Compatibility-Fixtures repository](https://github.com/HuffmanRepositories/Open-Agent-Compatibility-Fixtures) currently contains seven illustrative draft cases: text request mapping, cancellation unsupported, capability mapping, artifact versus evidence, task lifecycle/correlation, protocol error versus task failure, and streaming/push semantics. Fixture expectations document gaps rather than inventing universal field names.

These are static examples only. They have not been validated against live protocol implementations; do not treat them as conformance evidence.

## Security review boundary

This is not a deployment security assessment, certification, or conformance claim. It does not compare vulnerability status, key custody, card trust/discovery, or authorization correctness. An OIX signature authenticates signed bytes under a key; it does not establish truth, authorization, or operator identity. Do not treat it as equivalent to A2A transport/security controls.

## Fixture work

Initial draft examples are tracked in the companion [Open-Agent-Compatibility-Fixtures repository](https://github.com/HuffmanRepositories/Open-Agent-Compatibility-Fixtures): a text task-request mapping, cancellation-unsupported negative case, capability mapping case, artifact-versus-evidence case, and task-lifecycle/correlation case. They are illustrative only and have not been validated against implementations.

## Evidence and next steps

- Evidence: **E1 — specification review** only.
- Fixture files are illustrative drafts; validator/CI execution and runtime implementation tests remain unconfirmed.
- No certification or independent review claimed.
- Before E2: pin OIX to an immutable commit permalink, cite exact A2A sections, review mapping with maintainers, and choose a bridge-profile owner.
- Before E3: name implementation/version pairs, define bridge behavior, add fixtures, test both directions, and record loss.
- Reassess on upstream version changes; do not silently update source versions.

## References

- [OIX v0.1 spec](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange/blob/main/protocol/oix-v0.1.md)
- [OIX interoperability notes](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange/blob/main/docs/INTEROPERABILITY.md)
- [A2A v1.0.0 specification](https://a2a-protocol.org/v1.0.0/specification)
- [A2A migration notes](https://github.com/a2aproject/A2A/blob/main/docs/whats-new-v1.md)
