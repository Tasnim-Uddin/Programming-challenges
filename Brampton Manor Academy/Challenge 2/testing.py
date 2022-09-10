import unittest

from Richter import *

class richterEquivalences(unittest.TestCase):

    def test_energy(self):
        energy = 6.309573444801943e+19
        self.assertEqual(energyCalculation(10),energy)

    def test_tnt(self):
        tnt = 476879.13837688405
        self.assertEqual(tntCalculation(7),tnt)

if __name__ == "__main__":
    unittest.main()
