from selenium import webdriver


browser = webdriver.Chrome()
alert = browser.switch_to.alert
alert.accept()

alert = browser.switch_to.alert
alert_text = alert.text

confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
