import unittest
from sorter import Sorter


class TestParking(unittest.TestCase):
    def testSample(self):
        permutation = [1, 2, 0, 3]
        order = [3, 1, 2, 0]

        sorter = Sorter(permutation, order)
        result = sorter.sort()

        self.assertEqual(result, order)


if __name__ == '__main__':
    unittest.main()
