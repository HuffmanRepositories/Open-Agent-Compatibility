# Open Agent Compatibility

[Start here](START-HERE.md) · [Whitepaper](WHITEPAPER.md) · [AI agent guidance](AGENTS.md)


**Neutral interoperability research, mapping, and conformance work for open agent ecosystems.**

Open Agent Compatibility (OAC) helps existing agent protocols, schemas, and integration projects work together by documenting their semantics, identifying compatibility gaps, and creating reproducible mapping and conformance artifacts.

This project is a **compatibility layer of documentation and test methodology—not another agent protocol or runtime**.

## Why this exists

The open agent ecosystem already has valuable protocols and implementations. Fragmentation often appears at the boundaries: similar concepts have different names, lifecycle assumptions, data shapes, error behavior, or security expectations.

OAC aims to make those differences explicit and testable without replacing the projects that already own them.

## Scope

- Compare existing protocol and integration specifications.
- Document mappings, mismatches, and information loss.
- Define a transparent methodology for compatibility claims.
- Create small, reproducible fixtures and tests for documented mappings.
- Track upstream versions and changes.
- Publish limitations and unresolved questions.

## Non-goals

OAC does **not** aim to:
- invent a universal agent message protocol;
- replace Open Intelligence Exchange (OIX), MCP, A2A, or other upstream protocols;
- become another adapter runtime, schema registry, identity provider, trust system, or policy engine;
- claim official certification or conformance without evidence and permission;
- imply that a mapping guarantees security, semantic equivalence, or interoperability in every implementation.

## Relationship to neighboring projects

- [Open Intelligence Exchange (OIX)](https://github.com/HuffmanMainNode/Open-Intelligence-Exchange): protocol and implementation work.
- [Agent Ecosystem Integration](https://github.com/PCakes303/agent-ecosystem-integration): integration profiles and adapters.
- [Agent Foundation Spec](https://github.com/PCakes303/agent-foundation-spec): shared agent requirements.
- [Agent Schema Registry](https://github.com/PCakes303/agent-schema-registry): versioned schemas.

OAC is intended to complement these efforts through **cross-project mapping, independent compatibility evidence, and neutral reporting**. If an issue belongs in an upstream project, we will link or contribute there rather than duplicate it.

## Project status

**Stage: research / early foundation.** This repository is not a stable compatibility standard, certification program, or production adapter. Initial work should establish the source inventory, mapping format, versioning policy, and test methodology before making compatibility claims.

## Start here

- [Architecture and boundaries](docs/architecture.md)
- [Protocol matrix](docs/protocol-matrix.md)
- [Mapping methodology](docs/mapping-methodology.md)
- [Mapping format example](examples/mapping-profile.json)
- [Mapping profile format and validation](docs/mapping-profile-format.md)
- [Conformance evidence](conformance/README.md)
- [Contributing](CONTRIBUTING.md)

## Validate locally

```bash
python scripts/validate_mapping_profiles.py
python -m unittest discover -s tests -v
```

These checks validate the example profile structure; they do not test live implementations or establish runtime conformance.

## Principles

1. **Respect upstream ownership.** Link to authoritative sources and preserve their terminology.
2. **Version everything.** A mapping is only meaningful for specific source versions.
3. **Preserve semantics.** Record loss, ambiguity, and unsupported behavior explicitly.
4. **Evidence over labels.** Compatibility statements must link to reproducible evidence.
5. **No false certainty.** Do not claim perfect equivalence, security, or universal support.
6. **Human-readable first.** Explain the trade-offs before automating them.
7. **Open and reviewable.** Use public discussion and documented decisions.

## License

MIT. See [LICENSE](LICENSE).

## Ecosystem directory

This project is part of the [HuffmanRepositories public ecosystem](https://github.com/HuffmanRepositories/Huffman-Ecosystem-Root). Use the directory for project routing, human and AI onboarding, shared terminology, governance, and related workstreams. This repository's own README and specifications remain authoritative for its scope, maturity, and validation status.
