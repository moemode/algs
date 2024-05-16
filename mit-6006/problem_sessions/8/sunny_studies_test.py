"""
Tests for sunny_studies.py
"""

import unittest
from sunny_studies import maximize_happiness_memo, maximize_happiness_iterative


class TestSunnyStudies(unittest.TestCase):
    """
    This class contains unit tests for the functions
    maximize_happiness_memo and maximize_happiness_iterative
    in the sunny_studies module.
    """

    def test_alternating_weather(self):
        # Scenario: Alternating sunny and rainy days
        weather = [-3, -4, -1]
        expected = 0
        result_memo = maximize_happiness_memo(weather)
        result_iterative = maximize_happiness_iterative(weather)
        self.assertEqual(result_memo, expected)
        self.assertEqual(result_iterative, expected)

    def test_all_sunny_days(self):
        # Scenario: All days are sunny, testing happiness maximization
        weather = [5, 6, 7, 8, 9]
        expected = 28
        result_memo = maximize_happiness_memo(weather)
        result_iterative = maximize_happiness_iterative(weather)
        self.assertEqual(result_memo, expected)
        self.assertEqual(result_iterative, expected)

    def test_all_rainy_days(self):
        # Scenario: All days are rainy, testing happiness maximization
        weather = [-5, -6, -7, -8, -9]
        expected = 0
        result_memo = maximize_happiness_memo(weather)
        result_iterative = maximize_happiness_iterative(weather)
        self.assertEqual(result_memo, expected)
        self.assertEqual(result_iterative, expected)

    def test_mixed_weather_no_consecutive_limit(self):
        # Scenario: Mixed weather, no more than 2 consecutive play days
        weather = [4, 5, -2, 6, 7, 3, -1]
        expected = 22
        result_memo = maximize_happiness_memo(weather)
        result_iterative = maximize_happiness_iterative(weather)
        self.assertEqual(result_memo, expected)
        self.assertEqual(result_iterative, expected)

    def test_edge_case_single_day_positive(self):
        # Scenario: Single day with positive happiness
        weather = [5]
        expected = 5
        result_memo = maximize_happiness_memo(weather)
        result_iterative = maximize_happiness_iterative(weather)
        self.assertEqual(result_memo, expected)
        self.assertEqual(result_iterative, expected)

    def test_edge_case_single_day_negative(self):
        # Scenario: Single day with negative happiness
        weather = [-5]
        expected = 0
        result_memo = maximize_happiness_memo(weather)
        result_iterative = maximize_happiness_iterative(weather)
        self.assertEqual(result_memo, expected)
        self.assertEqual(result_iterative, expected)

    def test_complex_weather_pattern(self):
        # Scenario: Complex pattern with varying weather
        weather = [3, -4, 2, 5, -6, 4, 1, -2, 7, 6]
        expected = 28
        result_memo = maximize_happiness_memo(weather)
        result_iterative = maximize_happiness_iterative(weather)
        self.assertEqual(result_memo, expected)
        self.assertEqual(result_iterative, expected)

    def test_additional_case(self):
        # Scenario: Additional test case
        weather = [2, 4, -1, 3, 3, 100]
        expected = 109
        result_memo = maximize_happiness_memo(weather)
        result_iterative = maximize_happiness_iterative(weather)
        self.assertEqual(result_memo, expected)
        self.assertEqual(result_iterative, expected)


if __name__ == "__main__":
    unittest.main()
