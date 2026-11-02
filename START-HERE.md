# Start Here — Open Agent Compatibility (OAC)

Welcome. OAC is neutral research and documentation for understanding where existing agent protocols and integrations align, differ, or lose meaning when mapped.

## What belongs here
Protocol inventories, source-version pinning, semantic mapping profiles, compatibility methodology, mismatch analysis, and evidence-backed conformance guidance. Reusable test payloads belong in [Open-Agent-Compatibility-Fixtures](https://github.com/HuffmanRepositories/Open-Agent-Compatibility-Fixtures).

## First 15 minutes
1. Read [README.md](README.md) and [docs/architecture.md](docs/architecture.md).
2. Review [docs/protocol-matrix.md](docs/protocol-matrix.md) to understand the current comparison scope.
3. Read [docs/mapping-methodology.md](docs/mapping-methodology.md) before making compatibility claims.
4. Inspect [examples/mapping-profile.json](examples/mapping-profile.json) and [conformance/README.md](conformance/README.md).
5. Check source versions and dates; upstream protocols change.

## How to contribute
Document one specific mapping or mismatch at a time. Cite authoritative upstream specifications, pin versions, identify semantic loss and ambiguity, and include a reproducible example when useful. If the work is implementation-specific, contribute upstream or to the relevant adapter project instead.

## For AI agents
Read [AGENTS.md](AGENTS.md). Never infer equivalence from similar field names. Separate exact matches, partial mappings, unsupported behavior, and unknowns. Do not claim certification, universal compatibility, security, or conformance from a mapping document alone.

## Validation
This repository is primarily a research and documentation project. Follow any checks documented in the target contribution. Validate JSON examples and links, and report when no automated conformance test exists.

— Robert Huffman