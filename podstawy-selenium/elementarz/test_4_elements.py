# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Na obiektach klasy WebElement możemy podejmować przeróżne akcje.
Przykłady:
clear() - czyści tekst
send_keys() - wpisuje zadany tekst
click() - klika w element
submit() - wysyła formularz
"""


class WsbPlSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
	self.driver.get("http://www.wsb.pl/chorzow")
	self.driver.find_element_by_link_text(u"AKCEPTUJĘ").click()

    def test_click_on_link(self):
	WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT,u"Studia podyplomowe")))
        podyplomowe_link = self.driver.find_element_by_link_text("Studia podyplomowe")
        podyplomowe_link.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
