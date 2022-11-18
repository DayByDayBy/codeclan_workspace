import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):  
    
    def test_latest_score(self,):
        scores = [350, 275, 125, 400]
        self.assertEqual(400, latest(scores))

    def test_personal_best(self):
        scores = [100, 200, 300, 425]
        output = personal_best(scores)
        self.assertEqual(425, output)

    def test_top_three_scores(self):
        scores = [100, 200, 300, 425, 375, 225]
        output = personal_top_three(scores)
        self.assertEqual([425, 375, 300], output)

    def test_high_low_sort(self):
        scores = [100, 200, 300, 425, 375, 225]
        output = personal_top_three(scores)
        self.assertEqual([425, 375, 300], output)

    def test_top_three_including_tie(self):
        scores = [100, 200, 300, 425, 375, 225]
        output = personal_top_three(scores)
        self.assertEqual([425, 375, 300], output)


    def test_top__when_less_than_three(self):
        scores = [300, 425]
        output = personal_top_three(scores)
        self.assertEqual([425, 300], output)
    
    def test_top_three_when_only_one(self):
        scores = [300]
        output = personal_top_three(scores)
        self.assertEqual([300], output)