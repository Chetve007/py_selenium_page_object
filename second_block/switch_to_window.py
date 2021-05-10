from selenium import webdriver


browser = webdriver.Chrome()

window_name = ''
browser.switch_to.window(window_name)
new_window = browser.window_handles[1]
first_window = browser.window_handles[0]
