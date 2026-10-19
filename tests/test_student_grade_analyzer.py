"""Unit tests for the Student Grade Analyzer."""

import unittest

from projects.student_grade_analyzer import get_grade


class TestGetGrade(unittest.TestCase):
    def test_grade_boundaries(self):
        cases = [
            (100, "A+"),
            (90, "A+"),
            (89.99, "A"),
            (80, "A"),
            (70, "B"),
            (60, "C"),
            (50, "D"),
            (49.99, "F"),
            (0, "F"),
        ]
        for mark, expected in cases:
            with self.subTest(mark=mark):
                self.assertEqual(get_grade(mark), expected)


if __name__ == "__main__":
    unittest.main()
