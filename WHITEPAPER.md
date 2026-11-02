# Open Agent Compatibility: Neutral Mapping and Evidence

**Author:** Robert Huffman  
**Status:** Research whitepaper, version 0.1

## Abstract

Open Agent Compatibility (OAC) is a neutral research project for documenting how existing agent protocols and integrations relate. It focuses on semantic compatibility, not superficial field matching. Its central premise is that interoperability claims must be tied to exact source versions and supported by reproducible evidence.

## Problem statement

Protocols can use similar words for different concepts or different words for similar concepts. Lifecycle states, error models, streaming behavior, artifact references, cancellation, identity, and authorization can vary in ways that break assumptions at integration boundaries. A simple JSON transformation may preserve syntax while losing meaning.

## Method

OAC uses a version-pinned, evidence-led workflow:

1. Identify authoritative upstream specifications and versions.
2. Extract the relevant concepts and lifecycle semantics.
3. Compare fields, states, errors, and operational assumptions.
4. Classify mappings as exact, partial, lossy, unsupported, or unknown.
5. Record examples and expected behavior in the companion fixture repository.
6. Review claims independently before promoting maturity.

## How to use OAC

Start with [START-HERE.md](START-HERE.md), then read the [protocol matrix](docs/protocol-matrix.md) and [mapping methodology](docs/mapping-methodology.md). Use the mapping profile example as a structure guide. Add reusable synthetic test data to [OAC Fixtures](https://github.com/HuffmanRepositories/Open-Agent-Compatibility-Fixtures), not as an ad hoc payload buried in the analysis document.

## Non-goals

OAC is not a universal protocol, runtime, adapter, identity provider, policy engine, certification program, or replacement for MCP, A2A, OIX, or other upstream projects.

## Evaluation and limitations

A mapping document can reveal compatibility gaps but cannot prove that two production implementations interoperate. Fixture validation does not establish semantic equivalence or security. Strong claims require version-specific evidence and implementation-level testing.

## Outlook

The project should prioritize narrow, high-value mappings and transparent mismatch reporting. When a question belongs upstream, OAC should link or contribute there rather than create a competing abstraction.

— Robert Huffman