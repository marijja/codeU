import unittest
from sorter import Sorter


class TestParking(unittest.TestCase):
    def testEmpty(self):
        permutation = []
        order = []

        print("Empty list: ")

        sorter = Sorter(permutation, order)
        result = sorter.sort()

        print('---')

        self.assertEqual(result, order)

    def testNonZero(self):
        permutation = [1]
        order = [1]

        print("Single non-zero character: ")

        sorter = Sorter(permutation, order)
        result = sorter.sort()

        print('---')

        self.assertEqual(result, order)

    def testSorted(self):
        permutation = list(range(10))
        order = list(range(10))

        print("Already sorted: ")

        sorter = Sorter(permutation, order)
        result = sorter.sort()

        print('---')

        self.assertEqual(result, order)

    def testReversed(self):
        permutation = list(range(10))
        order = list(reversed(range(10)))

        print("Reversed list: ")

        sorter = Sorter(permutation, order)
        result = sorter.sort()

        print('---')

        self.assertEqual(result, order)

    def testSample(self):
        permutation = [1, 2, 0, 3]
        order = [3, 1, 2, 0]

        print("Sample from assignment: ")

        sorter = Sorter(permutation, order)
        result = sorter.sort()

        print('---')

        self.assertEqual(result, order)


if __name__ == '__main__':
    unittest.main()
