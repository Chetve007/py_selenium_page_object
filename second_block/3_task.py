from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    # browser.get("http://suninjuly.github.io/selects1.html")
    browser.get("http://suninjuly.github.io/selects2.html")

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum_ = int(num1) + int(num2)

    select = Select(browser.find_element_by_class_name('custom-select'))
    select.select_by_value(str(sum_))

    browser.find_element_by_css_selector("button.btn").click()

finally:
    sleep(30)
    browser.quit()
