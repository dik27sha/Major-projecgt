
import unittest

from src.skill_gap_analyzer import analyze_skill_gaps


class TestSkillGapAnalyzer(unittest.TestCase):

    def test_all_skills_matched(self):
        result = analyze_skill_gaps(
            ["Python", "SQL"],
            ["Python", "SQL"]
        )

        self.assertEqual(result["matched_skills"], ["Python", "SQL"])
        self.assertEqual(result["missing_skills"], [])
        self.assertEqual(result["match_percentage"], 100.0)

    def test_some_skills_missing(self):
        result = analyze_skill_gaps(
            ["Python", "SQL"],
            ["Python", "SQL", "Java", "Django"]
        )

        self.assertEqual(result["matched_skills"], ["Python", "SQL"])
        self.assertEqual(result["missing_skills"], ["Java", "Django"])
        self.assertEqual(result["match_percentage"], 50.0)

    def test_no_skills_matched(self):
        result = analyze_skill_gaps(
            ["HTML", "CSS"],
            ["Python", "Java"]
        )

        self.assertEqual(result["matched_skills"], [])
        self.assertEqual(result["missing_skills"], ["Python", "Java"])
        self.assertEqual(result["match_percentage"], 0.0)

    def test_case_insensitive_matching(self):
        result = analyze_skill_gaps(
            ["python", "SQL"],
            ["Python", "sql"]
        )

        self.assertEqual(result["match_percentage"], 100.0)

    def test_duplicate_skills(self):
        result = analyze_skill_gaps(
            ["Python", "Python", "SQL"],
            ["Python", "SQL", "SQL"]
        )

        self.assertEqual(result["total_required_skills"], 2)
        self.assertEqual(result["match_percentage"], 100.0)

    def test_empty_required_skills(self):
        result = analyze_skill_gaps(["Python"], [])

        self.assertEqual(result["missing_skills"], [])
        self.assertEqual(result["match_percentage"], 100.0)

    def test_invalid_candidate_skills(self):
        with self.assertRaises(ValueError):
            analyze_skill_gaps("Python", ["Python"])

    def test_invalid_required_skills(self):
        with self.assertRaises(ValueError):
            analyze_skill_gaps(["Python"], "Python")


if __name__ == "__main__":
    unittest.main()
