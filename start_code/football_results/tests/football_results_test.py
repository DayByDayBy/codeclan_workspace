import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def test_get_result_home_win(self):
        final_score = {"home_score": 2, "away_score": 0}
        self.assertEqual("Home win", get_result(final_score))

    def test_get_result_away_win(self):
        final_score = {"home_score": 0, "away_score": 2}
        self.assertEqual("Away win", get_result(final_score))

    def test_get_result_draw(self):
        final_score = {"home_score": 2, "away_score": 2}
        self.assertEqual("Draw", get_result(final_score))

    def test_get_results(self):
        results = [
            {"home_score": 2, "away_score": 0},
            {"home_score": 0, "away_score": 2},
            {"home_score": 2, "away_score": 2}
            ]
        self.assertEqual(["Home win", "Away win", "Draw"], get_results(results))

 