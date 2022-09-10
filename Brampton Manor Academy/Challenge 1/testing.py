import unittest

from Rod_Conversions import *

class testConversions(unittest.TestCase):
    
    def test_meters(self):
        self.assertEqual(metersConvert(10), 50.292)
        
    def test_feet(self):
        self.assertEqual(feetConvert(50), 825.0)

    def test_miles(self):
        self.assertEqual(milesConvert(6), 0.018750000000000003)
        
    def test_furlongs(self):
        self.assertEqual(furlongsConvert(5), 0.125)

    def test_walk(self):
        self.assertEqual(walkConvert(70), 4.233879503789322)

if __name__ == '__main__':
    unittest.main()
