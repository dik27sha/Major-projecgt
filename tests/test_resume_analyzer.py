
import json
import sys
import types
import unittest
from unittest.mock import patch

# Mock helper before importing resume_analyzer.
# This avoids requiring an OpenAI API key during tests.
mock_helper = types.ModuleType("src.helper")
mock_helper.ask_openai = lambda prompt, max_tokens=2000: "{}"
sys.modules["src.helper"] = mock_helper

from src.resume_analyzer import analyze_resume


class TestResumeAnalyzer(unittest.TestCase):

    def test_empty_resume(self):
        with self.assertRaises(ValueError):
            analyze_resume("")

    def test_valid_resume_analysis(self):
        mock_response = {
            "summary": "Python developer",
            "skills": ["Python", "SQL"],
            "education": ["B.Tech"],
            "experience": ["Python project"],
            "skill_gaps": ["Machine Learning"],
            "roadmap": ["Learn ML"],
            "job_keywords": ["Python Developer"]
        }

        with patch(
            "src.resume_analyzer.ask_openai",
            return_value=json.dumps(mock_response)
        ):
            result = analyze_resume("Python developer resume")

        self.assertEqual(result["summary"], "Python developer")
        self.assertIn("Python", result["skills"])

    def test_invalid_json_response(self):
        with patch(
            "src.resume_analyzer.ask_openai",
            return_value="Invalid response"
        ):
            with self.assertRaises(ValueError):
                analyze_resume("Sample resume")

    def test_missing_required_field(self):
        incomplete_response = {
            "summary": "Python developer",
            "skills": ["Python"]
        }

        with patch(
            "src.resume_analyzer.ask_openai",
            return_value=json.dumps(incomplete_response)
        ):
            with self.assertRaises(ValueError):
                analyze_resume("Sample resume")

    # Day 2 additional tests

    def test_none_resume(self):
        with self.assertRaises(ValueError):
            analyze_resume(None)

    def test_non_dict_response(self):
        with patch(
            "src.resume_analyzer.ask_openai",
            return_value=json.dumps(["invalid", "data"])
        ):
            with self.assertRaises(ValueError):
                analyze_resume("Sample resume")

    def test_summary_must_be_string(self):
        invalid_response = {
            "summary": ["Python developer"],
            "skills": ["Python"],
            "education": [],
            "experience": [],
            "skill_gaps": [],
            "roadmap": [],
            "job_keywords": []
        }

        with patch(
            "src.resume_analyzer.ask_openai",
            return_value=json.dumps(invalid_response)
        ):
            with self.assertRaises(ValueError):
                analyze_resume("Sample resume")

    def test_skills_must_be_list(self):
        invalid_response = {
            "summary": "Python developer",
            "skills": "Python, SQL",
            "education": [],
            "experience": [],
            "skill_gaps": [],
            "roadmap": [],
            "job_keywords": []
        }

        with patch(
            "src.resume_analyzer.ask_openai",
            return_value=json.dumps(invalid_response)
        ):
            with self.assertRaises(ValueError):
                analyze_resume("Sample resume")

    def test_all_analysis_lists_must_be_valid(self):
        invalid_response = {
            "summary": "Python developer",
            "skills": ["Python"],
            "education": "B.Tech",
            "experience": [],
            "skill_gaps": [],
            "roadmap": [],
            "job_keywords": []
        }

        with patch(
            "src.resume_analyzer.ask_openai",
            return_value=json.dumps(invalid_response)
        ):
            with self.assertRaises(ValueError):
                analyze_resume("Sample resume")


if __name__ == "__main__":
    unittest.main()
