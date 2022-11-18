import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    def test_10_percent_for_20_years(self, principal, interest, time):
        principal = 100
        total = compound(principal, interest, time)
        self.assertEqual(732.81, total)

    def test_6_percent_for_10_years(self):
        principal = 100
        total = compound(principal, interest, time)
        self.assertEqual(181.94, total)

    def test_5_percent_for_8_years(self):
        # principal = 100000
        total = compound(principal, interest, time)
        self.assertEqual(149,058.55, total)

    def test_10_percent_for_1_year(self):
        principal = 0
        total = compound(principal, interest, time)
        self.assertEqual(0.00, total)

    def test_0_percent_for_10_years(self):
        principal = 100
        total = compound(principal, interest, time)
        self.assertEqual(100.00, total)





    # Tests
    # Should return 732.81 given 100 principal, 10 percent, 20 years
    # Should return 181.94 given 100 principal, 6 percent, 10 years
    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    # Should return 0.00 given 0 principal, 10 percent, 1 year
    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month
    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

