from time import sleep

import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    inp = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp)
    inp.send_keys(y)

    cb = browser.find_element_by_id("robotCheckbox")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", cb)
    cb.click()

    rb = browser.find_element_by_id("robotsRule")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
    rb.click()

    button = browser.find_element_by_css_selector("button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    sleep(15)
    browser.quit()
