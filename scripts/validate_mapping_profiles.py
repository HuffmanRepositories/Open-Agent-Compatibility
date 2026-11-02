"""Dependency-free structural validator for OAC mapping profile examples."""

import json
from pathlib import Path
from typing import Any


OUTCOMES = {"direct", "transformed", "partial", "lossy", "ambiguous", "unsupported", "not-tested"}
EVIDENCE = {"E0", "E1", "E2", "E3", "E4"}
DIRECTIONS = {"source-to-target", "target-to-source", "bidirectional"}


def _is_string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def validate_profile(profile: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(profile, dict):
        return ["profile must be a JSON object"]

    required = {"profile_id", "status", "assessment_date", "source", "target", "direction", "features", "review"}
    missing = sorted(required - profile.keys())
    if missing:
        errors.append(f"missing top-level fields: {', '.join(missing)}")

    if not isinstance(profile.get("profile_id"), str) or not profile.get("profile_id", "").strip():
        errors.append("profile_id must be a non-empty string")
    if profile.get("status") not in {"illustrative", "draft", "reviewed", "validated"}:
        errors.append("status must be illustrative, draft, reviewed, or validated")
    if profile.get("assessment_date") is not None and not isinstance(profile.get("assessment_date"), str):
        errors.append("assessment_date must be a string or null")
    if profile.get("direction") not in DIRECTIONS:
        errors.append("direction is not a supported mapping direction")

    for side in ("source", "target"):
        item = profile.get(side)
        if not isinstance(item, dict):
            errors.append(f"{side} must be an object")
            continue
        for field in ("project", "version"):
            if not isinstance(item.get(field), str) or not item.get(field, "").strip():
                errors.append(f"{side}.{field} must be a non-empty string")
        if not _is_string_list(item.get("references")):
            errors.append(f"{side}.references must be an array of strings")

    features = profile.get("features")
    if not isinstance(features, list) or not features:
        errors.append("features must be a non-empty array")
    else:
        seen: set[str] = set()
        for index, feature in enumerate(features):
            prefix = f"features[{index}]"
            if not isinstance(feature, dict):
                errors.append(f"{prefix} must be an object")
                continue
            for field in ("feature_id", "source_concept", "target_concept", "notes"):
                if not isinstance(feature.get(field), str) or not feature.get(field, "").strip():
                    errors.append(f"{prefix}.{field} must be a non-empty string")
            feature_id = feature.get("feature_id")
            if isinstance(feature_id, str):
                if feature_id in seen:
                    errors.append(f"{prefix}.feature_id duplicates {feature_id}")
                seen.add(feature_id)
            if feature.get("outcome") not in OUTCOMES:
                errors.append(f"{prefix}.outcome is not supported")
            if feature.get("evidence_level") not in EVIDENCE:
                errors.append(f"{prefix}.evidence_level must be E0 through E4")
            if feature.get("transformation") is not None and not isinstance(feature.get("transformation"), str):
                errors.append(f"{prefix}.transformation must be a string or null")
            for field in ("losses", "constraints", "tests"):
                if not _is_string_list(feature.get(field)):
                    errors.append(f"{prefix}.{field} must be an array of strings")

    review = profile.get("review")
    if not isinstance(review, dict):
        errors.append("review must be an object")
    else:
        if not _is_string_list(review.get("reviewers")):
            errors.append("review.reviewers must be an array of strings")
        if review.get("reviewed_at") is not None and not isinstance(review.get("reviewed_at"), str):
            errors.append("review.reviewed_at must be a string or null")

    return errors


def main() -> int:
    files = sorted(Path("examples").glob("*.json"))
    if not files:
        print("ERROR: no mapping profile examples found")
        return 1
    failed = False
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL: {path}: {exc}")
            failed = True
            continue
        errors = validate_profile(data)
        if errors:
            print(f"FAIL: {path}")
            for error in errors:
                print(f"  - {error}")
            failed = True
        else:
            print(f"OK: {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
