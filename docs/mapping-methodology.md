# Mapping methodology

## Unit of assessment

Every mapping assessment identifies:

- source protocol/project and exact version or commit;
- target protocol/project and exact version or commit;
- direction (A → B, B → A, or bidirectional);
- concept/feature under examination;
- authoritative references;
- transformation rules;
- semantic loss or ambiguity;
- validation approach and results;
- maintainer/reviewer and assessment date.

## Mapping outcomes

Use one of these outcomes per feature:

- **direct** — semantics and required constraints are preserved without transformation;
- **transformed** — a defined conversion is needed and preserves documented semantics;
- **partial** — only a subset can be represented;
- **lossy** — information or behavior is lost; document exactly what;
- **ambiguous** — sources do not provide enough information for a reliable mapping;
- **unsupported** — no mapping is currently available;
- **not tested** — analysis or evidence is incomplete.

Do not use a single broad “compatible” label where individual features differ.

## Evidence levels

- **E0 — assertion:** unverified claim or proposal.
- **E1 — specification review:** documented source-to-source analysis.
- **E2 — fixture validation:** reproducible static examples or schema checks.
- **E3 — implementation test:** repeatable tests against named implementations and versions.
- **E4 — independent review:** another reviewer reproduces or audits the evidence.

Evidence levels are descriptive, not a certification. Security review is separate and must not be inferred from E0–E4.

## Review checklist

- [ ] Sources are authoritative and version-pinned.
- [ ] Both directions are considered where relevant.
- [ ] Required vs optional fields and capability constraints are recorded.
- [ ] Lifecycle, errors, cancellation, events/streaming, and artifacts are considered.
- [ ] Unknown fields and extension behavior are documented.
- [ ] Loss and unsupported cases are explicit.
- [ ] Security/privacy assumptions are recorded separately.
- [ ] Tests and reproduction steps are included.
- [ ] Upstream owners and relevant issue links are identified.
- [ ] Changes to upstream sources trigger review.

## Version changes

Never silently update a mapping to a new source version. Open a change, compare relevant source sections, rerun tests, and preserve historical results where practical.
