import unittest
from functools import reduce

def array_calculation(items):
    # return reduce(lambda x, y: x + y, items)
    return reduce(reduce_sum, items, 0)
def reduce_sum(x, y):
    print(x, y)
    return x + 1 + y




class TestArrayCalculation(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(array_calculation([3, 7, 8, 12]), 34)

    # def test_sum_2(self):
    #     self.assertEqual(array_calculation([3]), 4)

