import os
import unittest
from .prod import partA, partB, roundScore

class DayTestCase(unittest.TestCase):
    def testRoundscore(self):
        self.assertEqual(roundScore('Rock', 'Rock'), 4)
        self.assertEqual(roundScore('Paper', 'Rock'), 1)
        self.assertEqual(roundScore('Scissors', 'Rock'), 7)
        self.assertEqual(roundScore('Rock', 'Scissors'), 3)
        self.assertEqual(roundScore('Scissors', 'Scissors'), 6)

    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 15)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 11906)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 12)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 11186)
if __name__ == '__main__':
    unittest.main()

