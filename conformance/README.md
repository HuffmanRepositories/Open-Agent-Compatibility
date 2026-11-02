# Conformance and compatibility evidence

This directory contains reproducible fixtures and tests supporting **specific, version-scoped** mapping claims.

## Important

- A passing JSON/schema test proves only what that test checks.
- Static fixture validation does not prove runtime interoperability.
- Runtime interoperability does not establish security or upstream certification.
- Do not use “certified,” “fully compliant,” or “secure” unless there is a separately defined, authorized, and rigorous basis.

## Evidence record

Every published result should include:

- source and target project versions/commits;
- implementation names and versions, if runtime tests are involved;
- test environment and commands;
- test cases and expected behavior;
- pass/fail/skip details;
- known limitations and unresolved issues;
- date and reviewer.

Keep tests deterministic where possible. Avoid network-dependent tests in the default suite unless they are explicitly marked as integration tests.
