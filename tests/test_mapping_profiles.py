import copy
import json
import unittest
from pathlib import Path

from scripts.validate_mapping_profiles import validate_profile


class MappingProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads(Path("examples/mapping-profile.json").read_text(encoding="utf-8"))

    def test_example_profile_is_valid(self):
        self.assertEqual(validate_profile(self.example), [])

    def test_non_object_is_rejected(self):
        self.assertIn("profile must be a JSON object", validate_profile([]))

    def test_missing_feature_id_is_rejected(self):
        profile = copy.deepcopy(self.example)
        del profile["features"][0]["feature_id"]
        self.assertTrue(any("feature_id" in error for error in validate_profile(profile)))

    def test_unknown_outcome_is_rejected(self):
        profile = copy.deepcopy(self.example)
        profile["features"][0]["outcome"] = "probably-compatible"
        self.assertTrue(any("outcome" in error for error in validate_profile(profile)))

    def test_duplicate_feature_ids_are_rejected(self):
        profile = copy.deepcopy(self.example)
        profile["features"].append(copy.deepcopy(profile["features"][0]))
        self.assertTrue(any("duplicates" in error for error in validate_profile(profile)))

    def test_invalid_direction_is_rejected(self):
        profile = copy.deepcopy(self.example)
        profile["direction"] = "universal"
        self.assertTrue(any("direction" in error for error in validate_profile(profile)))


if __name__ == "__main__":
    unittest.main()
