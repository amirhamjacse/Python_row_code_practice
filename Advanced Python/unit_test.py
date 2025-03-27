## this is not unit test
def sum_of_num(a, b):
    sums = a + b
    return sums

# def test_sum_of_num():
#     arr = [1, 2, 3, 4, 5]
#     arr2 = [3, 4, 5, 6, 7]
#     for i, j in zip(arr, arr2):
#         res = sum_of_num(i, j)
#         print(res)

# test_sum_of_num()
"""
This was not unit test
"""

# import pytest
import unittest

class TestSumFunc(unittest.TestCase):
    def test_sum_of_num(self):
        self.assertEqual(sum_of_num(1, 3), 4)
        self.assertEqual(sum_of_num(2, 4), 6)
        self.assertEqual(sum_of_num(3, 5), 8)
        self.assertEqual(sum_of_num(4, 6), 10)
        self.assertEqual(sum_of_num(5, 7), 12)

if __name__ == "__main__":
    unittest.main()



# def test_sum_of_num():
#     assert sum_of_num(1, 3) == 4
#     assert sum_of_num(2, 4) == 6
#     assert sum_of_num(3, 5) == 8
#     assert sum_of_num(4, 6) == 10
#     assert sum_of_num(5, 7) == 12

