import unittest

from The_99_Trick import *

class gameTest(unittest.TestCase):

    def test_you(self):
        self.assertEqual(factorCalculate(15),84)

    def test_you_not_range(self):
        self.assertEqual(answerInput(69),"*YOU* --> This will be the answer. Select a number between 1-49: ")

    def test_friend_main_num(self):
        self.assertEqual(friendNum(72,84),156)

    def test_friend_not_range(self):
        eslf.assertEqual(

    def test_convert_friend_num(self):
        self.assertEqual(friendNumCalculation(156),57)

    def test_friend_answer(self):
        self.assertEqual(result(72,57),15)

if __name__ == "__main__":
    unittest.main()
