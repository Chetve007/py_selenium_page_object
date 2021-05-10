import os
from time import sleep

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element_by_name('firstname').send_keys('Alex')
    browser.find_element_by_name('lastname').send_keys('Chet')
    browser.find_element_by_name('email').send_keys('AChet@ma.ru')

    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'text.txt')
    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    sleep(15)
    browser.quit()
