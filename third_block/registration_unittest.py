import time
import unittest

from selenium import webdriver


LINK_1 = "http://suninjuly.github.io/registration1.html"  # без бага
LINK_2 = "http://suninjuly.github.io/registration2.html"  # с багом


def fill_fields_and_send(browser):
    first_name = browser.find_element_by_css_selector(".first[required]")
    first_name.send_keys("Alex")
    last_name = browser.find_element_by_css_selector(".second[required]")
    last_name.send_keys("Chetverik")
    email = browser.find_element_by_class_name("third")
    email.send_keys("chet@mail.ru")
    phone = browser.find_element_by_xpath("//div[./label[text()='Phone:']]/input")
    phone.send_keys("+79999999999")
    address = browser.find_element_by_xpath("//div[./label[text()='Address:']]/input")
    address.send_keys("Test street, 90210")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)


class TestRegistration(unittest.TestCase):
    """Tests for registration"""

    def test_correct_registration(self):
        """Correct registration test"""
        browser = webdriver.Chrome()
        browser.get(LINK_1)
        fill_fields_and_send(browser)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_wrong_registration(self):
        """Wrong registration test"""
        browser = webdriver.Chrome()
        browser.get(LINK_2)
        fill_fields_and_send(browser)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()
