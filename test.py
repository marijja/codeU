import unittest
from alphabet import Alphabet


class TestAlphabet(unittest.TestCase):
    def testEmpty(self):
        dictionary = []
        alphabet = Alphabet()

        result = alphabet.get_alphabet(dictionary)
        self.assertEqual(result, [])

    def testOneLetter(self):
        dictionary = ['a', 'aa', 'aaa', 'aaaa']
        alphabet = Alphabet()

        result = alphabet.get_alphabet(dictionary)
        self.assertEqual(result, ['a'])

    def testSample(self):
        dictionary = ['ART', 'RAT', 'CAT', 'CAR']
        alphabet = Alphabet()

        result = alphabet.get_alphabet(dictionary)
        self.assertEqual(result, ['A', 'T', 'R', 'C'])

if __name__ == '__main__':
    unittest.main()