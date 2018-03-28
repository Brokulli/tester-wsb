# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

"""
WebDriver zawiera szereg metod wyszukiwania elementów zawartych na stronie.
Wszystkie zaczynają się od "find_element_by..." i zwracają obiekt klasy
WebElement. W przypadku, gdy chcemy wyszukać wiele elementów, korzystamy
z metod "find_elements_by_..." - otrzymujemy wówczas listę złożoną
z obiektów klasy WebElement
"""


class WSBPlSelectors(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.wsb.pl/chorzow")
	driver.set_page_load_timeout(4)

    def test_find_element_by_tag_name(self):
	driver = self.driver
        # Wyszukuję ciało strony (to co widać) - cała strona
	moj_tag = "body"
        driver.find_element_by_tag_name(moj_tag)
	
    def test_find_element_by_id(self):
	driver = self.driver
	driver.find_element_by_id("edit-search-block-form--2")

    def test_find_element_by_class_name(self):
	driver = self.driver
	driver.find_element_by_class_name("custom-search-box")

    def test_find_element_by_link_text(self):
	driver = self.driver
	driver.find_element_by_link_text("Studia I stopnia")

    def test_find_element_by_partial_link_text(self):
	driver = self.driver
	driver.find_element_by_partial_link_text("Studia I sto")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    

