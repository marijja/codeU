import unittest
from count_islands import CountIslands

class TestIslands(unittest.TestCase):

    def testEmpty(self):
        map = [[False]*10 for i in range(10)]
        counter = CountIslands()
        self.assertEqual(0, counter.count(map))

    def testFull(self):
        map = [[True] * 10 for i in range(10)]
        counter = CountIslands()
        self.assertEqual(1, counter.count(map))

    def testDisjoint(self):
        map = [[True, False],
               [False, True]]

        counter = CountIslands()
        self.assertEqual(2, counter.count(map))

    def testSample(self):
        map = [[False, True, False, True],
               [True, True, False, False],
               [False, False, True, False],
               [False, False, True, False]]

        counter = CountIslands()
        self.assertEqual(3, counter.count(map))

    def testWeirdCase(self):
        map = [[True, False, True, False],
               [True, True, True, False],
               [True, False, True, True],
               [False, True, False, False]]

        counter = CountIslands()
        self.assertEqual(2, counter.count(map))

    def testSparse(self):
        map = [[False, False, True],
               [False, False, False],
               [True, False, False]]

        counter = CountIslands()
        self.assertEqual(2, counter.count(map))



if __name__ == '__main__':
    unittest.main()