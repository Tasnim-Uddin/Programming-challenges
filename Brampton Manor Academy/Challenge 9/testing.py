import unittest
from turtle_angle_calc import *

class all_tests(unittest.TestCase):

    def test_input(self):
        dictionary = user_input()
        self.assertIsNotNone(dictionary,'')
        x_cord = dictionary[1][0]
        self.assertTrue(x_cord,123)




if __name__ == '__main__':
    unittest.main()
