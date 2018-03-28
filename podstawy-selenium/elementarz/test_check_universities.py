# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WsbPlSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_universities_options(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        # Oczekiwane opcje
        exp_options = [u"Grupa WSB", u"Bydgoszcz", u"Chorzów / Katowice",
                       u"Gdańsk", u"Gdynia", u"Opole", u"Poznań", u"Szczecin",
                       u"Toruń", u"Wrocław"]
        # Pusta lista na dostępne opcje z menu rozwijanego
        act_options = []
        # menu rozwijane jako instancja klasy Select
        select_university = \
            Select(self.driver.find_element_by_id("miasto-wsb"))

        # Sprawdź liczbę dostępnych w menu opcji
        self.assertEqual(10, len(select_university.options))

        # Stwórz listę opcji
        for option in select_university.options:
            act_options.append(option.text)

        # Sprawdź, czy listy opcji oczekiwanych i rzeczywistych są takie same
        self.assertListEqual(exp_options, act_options)

        # Sprawdź, czy pierwszą opcją jest "Grupa WSB"
        self.assertEqual("Grupa WSB",
                         select_university.first_selected_option.text)

        # Wybierz Chorzów / Katowice
        select_university.select_by_visible_text(u"Chorzów / Katowice")

        WebDriverWait(self.driver, 20)\
            .until(expected_conditions.title_contains(u"Chorzów"))
        # Sprawdź, czy otworzyła się strona WSB Chorzów
        print self.driver.current_url
        self.assertTrue("chorzow" in self.driver.current_url)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
