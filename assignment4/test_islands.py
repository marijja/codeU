import unittest
from count_islands import CountIslands

class TestIslands(unittest.TestCase):

    def testEmpty(self):
        m = [[False]*10 for i in range(10)]
        counter = CountIslands()
        self.assertEqual(0, counter.count(m))

    def testFull(self):
        m = [[True] * 10 for i in range(10)]
        counter = CountIslands()
        self.assertEqual(1, counter.count(m))

    def testDisjoint(self):
        m = [[True, False],
               [False, True]]

        counter = CountIslands()
        self.assertEqual(2, counter.count(m))

    def testSample(self):
        m = [[False, True, False, True],
               [True, True, False, False],
               [False, False, True, False],
               [False, False, True, False]]

        counter = CountIslands()
        self.assertEqual(3, counter.count(m))

    def testWeirdCase(self):
        m = [[True, False, True, False],
               [True, True, True, False],
               [True, False, True, True],
               [False, True, False, False]]

        counter = CountIslands()
        self.assertEqual(2, counter.count(m))

    def testSparse(self):
        m = [[False, False, True],
               [False, False, False],
               [True, False, False]]

        counter = CountIslands()
        self.assertEqual(2, counter.count(m))



if __name__ == '__main__':
    unittest.main()