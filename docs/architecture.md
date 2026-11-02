# Architecture and boundaries

## Role

Open Agent Compatibility (OAC) is a neutral research and evidence repository between existing agent protocols and integration projects. It documents how concepts correspond—and where they do not.

OAC should not own the runtime behavior of upstream systems. Where an adapter or canonical schema already exists upstream, OAC links to it and evaluates the boundary rather than reimplementing it.

## Layers

1. **Source registry** — authoritative source URLs, versions, dates, and status.
2. **Concept inventory** — capabilities and concepts described by each source.
3. **Mapping profiles** — direction-aware correspondences, transformations, constraints, and loss.
4. **Fixtures** — small, versioned examples illustrating mappings.
5. **Conformance evidence** — repeatable checks, results, environment, and known limitations.
6. **Reports** — human-readable compatibility matrix and open gaps.

## Boundary rules

- No new universal wire protocol.
- No duplicate adapter implementation unless a narrowly scoped test harness is justified.
- No independent identity, trust, policy, or schema registry product.
- No claims of upstream endorsement.
- Security-sensitive behavior is reviewed as a separate dimension; shape compatibility is not security compatibility.

## Dependencies and authority

OAC is downstream of the specifications it maps. Source projects retain authority over their own protocol semantics. If OAC finds an ambiguity, it records it and may open an issue upstream.

## Proposed lifecycle

idea → research → draft mapping → fixture → reviewed evidence → published report

A mapping should not be called stable until source versions, review, test coverage, known limitations, and maintenance ownership are documented.
