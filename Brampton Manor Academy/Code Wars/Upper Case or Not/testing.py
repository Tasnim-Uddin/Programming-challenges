import unittest

from Upper_Case import *

class checkingIfUpper(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(checkUpper("hello"),False)
        self.assertEqual(checkUpper("AMAZING"),True)
        self.assertEqual(checkUpper("FLABbERGASTED"),False)

if __name__ == "__main__":
    unittest.main()
