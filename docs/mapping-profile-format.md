# Mapping Profile Format

A mapping profile is a version-scoped record of how one protocol/project concept maps to another. It is not a universal compatibility score.

## Required top-level fields

- profile_id: stable identifier for the assessment.
- status: illustrative, draft, reviewed, or validated.
- assessment_date: ISO date or null when not yet assessed.
- source and target: project name, exact version/commit, and authoritative references.
- direction: source-to-target, target-to-source, or bidirectional.
- features: one or more independently assessed concepts.
- review: reviewer identities and review timestamp, or empty/null values while unreviewed.

## Feature fields

Each feature records a stable feature_id, source_concept, target_concept, outcome, transformation, losses, constraints, evidence_level, tests, and notes.

Allowed outcomes follow the mapping methodology:
- direct
- transformed
- partial
- lossy
- ambiguous
- unsupported
- not-tested

Evidence levels:
- E0: assertion or proposal
- E1: specification review
- E2: fixture/schema validation
- E3: repeatable implementation test
- E4: independent review

Evidence levels are descriptive, not certification. Security review is separate.

## Validation

- JSON Schema: [mapping-profile.schema.json](../schemas/mapping-profile.schema.json)
- Dependency-free structural validator: run python scripts/validate_mapping_profiles.py
- Unit tests: run python -m unittest discover -s tests -v

The script validates the example profiles in examples/. It checks required fields, allowed outcomes and evidence levels, unique feature identifiers, and expected data types. It does not validate source truth, semantic equivalence, or runtime behavior.

## Authoring guidance

Pin source versions. Prefer authoritative references. Document information loss and uncertainty. Do not upgrade a profile to reviewed or validated without the corresponding evidence and review record.
