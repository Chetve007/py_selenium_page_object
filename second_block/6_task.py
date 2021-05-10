from time import sleep

import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element_by_css_selector("button.btn").click()
    browser.switch_to.alert.accept()

    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))

    browser.find_element_by_css_selector("button.btn").click()

finally:
    sleep(15)
    browser.quit()
