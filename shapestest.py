import unittest
from shapes import *

class TestShapes(unittest.TestCase):

    def test_stars(self):
        self.assertEqual(stars(1), '*')
        self.assertEqual(stars(2), '**')
        self.assertEqual(stars(5), '*****')
        self.assertEqual(stars(0), '')
        self.assertEqual(stars(-1), '')

if __name__ == '__main__':
    unittest.main()