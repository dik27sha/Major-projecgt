
import unittest

from src.learning_roadmap import generate_learning_roadmap


class TestLearningRoadmap(unittest.TestCase):

    def test_generate_roadmap_for_multiple_skills(self):
        result = generate_learning_roadmap(
            ["Java", "Spring Boot", "SQL"]
        )

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["skill"], "Java")
        self.assertEqual(result[1]["skill"], "Spring Boot")
        self.assertEqual(result[2]["skill"], "SQL")

    def test_roadmap_contains_learning_tasks(self):
        result = generate_learning_roadmap(["Python"])

        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]["learning_tasks"]), 3)
        self.assertIn("Python", result[0]["practical_project"])

    def test_roadmap_contains_milestones(self):
        result = generate_learning_roadmap(["Java"])

        self.assertIn("milestone", result[0])
        self.assertIn("Java", result[0]["milestone"])

    def test_empty_skill_list(self):
        result = generate_learning_roadmap([])

        self.assertEqual(result, [])

    def test_duplicate_skills(self):
        result = generate_learning_roadmap(
            ["Python", "Python", "SQL"]
        )

        self.assertEqual(len(result), 2)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            generate_learning_roadmap("Python")

    def test_empty_skill_name(self):
        with self.assertRaises(ValueError):
            generate_learning_roadmap(["Python", ""])

    def test_week_numbers_are_sequential(self):
        result = generate_learning_roadmap(
            ["Python", "Java", "SQL"]
        )

        self.assertEqual(
            [item["week"] for item in result],
            [1, 2, 3]
        )


if __name__ == "__main__":
    unittest.main()
