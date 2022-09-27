import unittest
from scrape_singles import *

class testing_scrapes(unittest.TestCase):

    def test_position(self):
        url = "https://www.officialcharts.com/charts/singles-chart"
        html = scrape(url)
        position = find_position(html)
        self.assertEqual(position,['1','2','3','4','5','6','7','8','9','10'])
        self.assertEqual(position[0], '1')
        self.assertEqual(position[9], '10')

    def test_title(self):
        url = "https://www.officialcharts.com/charts/singles-chart"
        html = scrape(url)
        title = find_title(html)
        self.assertEqual(title[1], 'FORGET ME')

    def test_artist(self):
        url = "https://www.officialcharts.com/charts/singles-chart"
        html = scrape(url)
        artist = find_artist(html)
        artist[0] = 'KSI'
        assert artist[0] 
        self.assertEqual(artist[0], 'KSI')

        
if __name__ == '__main__':
    unittest.main()
