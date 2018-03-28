# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
Rejestracja nowego użytkownika na stronie wizzair.com

Przypadki testowe:
I Rejestracja nowego użytkownika używając adresu email - dane niepoprawne (niekompletny email)
Kroki:
"1. Wejdz na https://wizzair.com/pl-pl/main-page#/
2. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
3. Wybierz rejestracja
4. Wprowadź imię
5. Wprowadź nazwisko
6. Wybierz płeć
7. Wprowadź nr tel
8. Wprowadź błędny adres email - brak znaku @
9. Wprowadź hasło
10. Wybierz kraj
11. Akceptuj politykę prywatności
12. Kliknij przycisk ZAREJESTRUJ SIĘ"

Oczekiwany rezultat:
Przycisk "zarejestruj się" jest nieaktywny
Uzytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny

"""

valid_name = "Dick"
valid_surname = "Laurent"
telephone = "123123123"
invalid_email = "hhjkjpl"
valid_password = "Qshiukk12"

class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_registration_valid_email(self):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl/main-page#/")
        zaloguj_btn = driver.find_element_by_css_selector("ul.navigation__container>li:nth-child(7) > button")
	# //button[contains(text(), "Zaloguj się")] - są 3
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')
        rejestracja_btn.click()
        imie_field = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        imie_field.send_keys(valid_name)
        nazwisko_field = driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        nazwisko_field.send_keys(valid_surname)
        gender_switch = driver.find_element_by_id("register-gender-male")
        driver.execute_script("arguments[0].click()", gender_switch)
        telefon_field = driver.find_element_by_css_selector("input[type=tel]")
        telefon_field.send_keys(telephone)
        email_field = driver.find_element_by_css_selector("input[data-test=booking-register-email]")
        email_field.send_keys(invalid_email)
        password_field = driver.find_element_by_css_selector("input[data-test=booking-register-password]")
        password_field.send_keys(valid_password)
        country_field = driver.find_element_by_css_selector("input[data-test=booking-register-country]")
        country_field.click()
        country_to_choose = driver.find_element_by_xpath('//*[@class="register-form__country-container__locations"]/label[164]')
        country_to_choose.location_once_scrolled_into_view
        country_to_choose.click()
        privacy_policy = driver.find_element_by_xpath('//*[@for="registration-privacy-policy-checkbox"]')
        privacy_policy.click()
        zarejestruj_btn = driver.find_element_by_css_selector("button[type=submit][data-test=booking-register-submit]") # szukanie po dwóch atrybutach (niezbyt ładne)
        #self.assertFalse(zarejestruj_btn.is_enabled(), "Szlag rafił!")
        error_notice = driver.find_element_by_css_selector("#regmodal-scroll-hook-4 > div.rf-input__error > span")
        print(error_notice.text)
	assert error_notice.is_displayed()
        self.assertEqual(error_notice.text, u"Nieprawidłowy adres e-mail")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
