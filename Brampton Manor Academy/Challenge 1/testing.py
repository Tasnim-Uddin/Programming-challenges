import unittest

from Rod_Conversions import *

class testConversions(unittest.TestCase):
    
    def test_meters(self):
        rods = 10
        meters = metersConvert(rods)
        self.assertEqual(meters, 50.292)
        
    def test_feet(self):
        rods = 50
        feet = feetConvert(rods)
        self.assertEqual(feet, 825.0)

    def test_miles(self):
        rods = 6
        miles = milesConvert(rods)
        self.assertEqual(miles, 0.018750000000000003)
        
    def test_furlongs(self):
        rods = 5
        furlongs = furlongsConvert(rods)
        self.assertEqual(furlongs, 0.125)

    def test_walk(self):
        rods = 70
        minutes = walkConvert(rods)
        self.assertEqual(minutes, 4.233879503789322)

if __name__ == '__main__':
    unittest.main()
