import unittest
from pathlib import Path

from friendly_faces import *


class initial_csv_tests(unittest.TestCase):

    def test_check_file_exists(self):
        csv_file = Path('south.csv')
        csv_file.is_file()

    def test_read_csv(self):
        csv_file = Path('south.csv')
        self.assertGreaterEqual(len(read_csv(csv_file)),1)
        
        path = 'south.csv'
        csv = read_csv(path)
        self.assertEqual(csv[0][1], 'IB')


class initial_html_tests(unittest.TestCase):
    
    def test_html_exists(self):
        html_file = Path('south.html')
        html_file.is_file()

    def test_read_html(self):
        html_file = Path('south.html')
        self.assertGreaterEqual(len(read_html(html_file)),1)


class main_tests(unittest.TestCase):

    def test_process(self):
        csv = read_csv(path = 'south.csv')
        html = read_html(path = 'south.html')
        process(csv, html)
        
        link_csv = csv[0][0]
        html = html.replace(f'link1', link_csv)
        
        link_find = 'background-image: url("'
        link_start = html.find(link_find)
        link_end = html.find('");', link_start)
        link = html[link_start+len(link_find):link_end]

        self.assertEqual(link, 'https://i.imgur.com/iDrhbZX.png')

    def test_final_html(self):
        csv = read_csv(path = 'south.csv')
        html = read_html(path = 'south_final.html')
        
        html_file = Path('south_final.html')
        self.assertGreaterEqual(len(read_html(html_file)),1)

        previous_link = 0
        previous_initial = 0
        previous_name = 0
        
        for column in csv:
            link_csv, initial_csv, name_csv = column[0], column[1], column [2]
            
            link_find = 'background-image: url("'
            link_start = html.find(link_find, previous_link)
            link_end = html.find('");', link_start)
            link = html[link_start+len(link_find):link_end]
            previous_link = link_end
            self.assertEqual(link, link_csv)

            initial_find = '<h2 class="el__heading">'
            initial_start = html.find(initial_find, previous_initial)
            initial_end = html.find('</h2>', initial_start)
            initial = html[initial_start+len(initial_find):initial_end]
            previous_initial = initial_end
            self.assertEqual(initial, initial_csv)

            name_find = '<div class="el__text">'
            name_start = html.find(name_find, previous_name)
            name_end = html.find('</div>', name_start)
            name = html[name_start+len(name_find):name_end]
            previous_name = name_end
            self.assertEqual(name, name_csv)




if __name__ == '__main__':
    unittest.main()
        
        
