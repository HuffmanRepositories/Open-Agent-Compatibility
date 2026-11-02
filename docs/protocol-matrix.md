# Protocol and project matrix

This inventory tracks assessment work; it is not a blanket compatibility verdict.

| Source | Primary role | OAC should examine | Boundary / caution |
|---|---|---|---|
| [Open Intelligence Exchange (OIX)](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange) | Open agent exchange protocol and Python reference implementation | Agent cards, task messages, provenance, capability representation, lifecycle | Do not reproduce OIX protocol definitions here; link to source version and test mapping |
| [MCP](https://modelcontextprotocol.io/) | Model/context/tool integration protocol | Tool/resource concepts, invocation, errors, lifecycle | MCP is not automatically equivalent to agent-to-agent task exchange |
| [A2A](https://github.com/a2aproject/A2A) | Agent-to-agent communication | Agent capabilities, task lifecycle, messages, artifacts, status | Preserve distinctions in task and artifact semantics |
| [Agent Ecosystem Integration](https://github.com/PCakes303/agent-ecosystem-integration) | Integration profiles/adapters | Profile alignment, adapter assumptions, supported pairs | Prefer upstream adapter/profile implementations |
| [Agent Foundation Spec](https://github.com/PCakes303/agent-foundation-spec) | Shared agent requirements | Common vocabulary and normative constraints | Do not redefine foundation requirements |
| [Agent Schema Registry](https://github.com/PCakes303/agent-schema-registry) | Versioned schemas | Schema references, version compatibility, migration | Do not fork registry schemas into OAC |

## Research status

| Pair / subject | Status | Evidence |
|---|---|---|
| OIX v0.1 ↔ A2A v1.0.0 | **Assessed at specification-review level (E1); no runtime conformance claim** | [OIX↔A2A assessment](oix-a2a-assessment-v0.1.md) |
| OIX ↔ MCP | Not yet assessed | None |
| MCP ↔ A2A | Not yet assessed | None |
| PCakes integration profiles ↔ above protocols | Not yet assessed | None |

## Required before marking a pair assessed

- Exact source versions and citations.
- Feature-by-feature mapping in each direction.
- Transformation requirements and data loss.
- Error, cancellation, streaming, and lifecycle behavior.
- Authentication/authorization assumptions, explicitly separate from semantic mapping.
- Reproducible fixtures and tests where feasible.
- Reviewer and assessment date.
