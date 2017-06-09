import unittest
from bs4 import BeautifulSoup
from happycowler import HappyCowler
from happycowler.happycowler import parse_restaurant_page
import os

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'test_pages/')

class SingleRestaurant(unittest.TestCase):

    def test_parse_restaurant_page(self):
        single_restaurant_test_file = data_path + "BarCeloneta Sangria Bar - Barcelona : Vegan Restaurant Reviews and Ratings - HappyCow.htm"
        with open(single_restaurant_test_file, 'r') as f:
            text = f.read()
        parsed_text = BeautifulSoup(text, "html.parser")
        results = parse_restaurant_page(parsed_text)
        self.assertTrue(results == ('41.376865', '2.189974'))


class SingleResultsPage(unittest.TestCase):

    def test_singe_results_page(self):
        single_restaurant_test_file = data_path + "Vegan & Vegetarian Restaurants in Worms, Germany.htm"
        with open(single_restaurant_test_file, 'r') as f:
            text = f.read()
        parsed_text = BeautifulSoup(text, "html.parser")
        hc = HappyCowler("")
        hc._parse_results_page(parsed_text, page_no='', deep_crawl=False)
        self.assertTrue(hc.total_entries == 2)
        self.assertTrue(hc.names == ['Frollein Elfriede', 'Eis Vannini'])

if __name__ == '__main__':
    test_main()
