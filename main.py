import unittest


def sum_of_x(x):
    return x + 1


def sum_of_three_x(x1, x2, x3):
    s1 = sum_of_x(x1)
    s2 = sum_of_x(x2)
    s3 = sum_of_x(x3)
    return s1 + s2 + s3


class TestSumOfThreeX(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_of_three_x(3, 8, 4), 18)


def letters_combination(x1, x2, x3):
    return "result of"" " + x1 + x2 + x3


class TestLettersCombination(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(letters_combination("A", "B", "C"), "result of ABC")

    def test_string(self):
        self.assertEqual(letters_combination("v", "n", "c"), "result of vnc")