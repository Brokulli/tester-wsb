# -*- coding: utf-8" -*


import unittest
from selenium import webdriver


# Tworzę klasę WsbPlCheck dziedziczącą po klasie TestCase z modułu unittest
class WsbPlCheck(unittest.TestCase):

    # Instrukcje, które zostaną automatycznie wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Metody rozpoczynające się od słowa "test" - czyli moje testy
    def test_wsb_pl(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        # Sprawdzam, czy "Wyższe Szkoły Bankowe" znajdują się w tytule strony
        self.assertIn(u"Wyższe Szkoły Bankowe", driver.title)

    # Instrukcje, które zostaną automatycznie wykonane po każdym teście
    def tearDown(self):
        self.driver.quit()

# Początek mojego programu
# wywołuję funkcję main() z modułu unittest,
# która w automatyczny sposób będzie już wiedziała
# co dalej robić z utworzoną wyżej klasą
if __name__ == "__main__":
    unittest.main(verbosity=2)
