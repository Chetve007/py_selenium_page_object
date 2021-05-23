from time import sleep

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_is_displayed(browser):
    browser.get(LINK)
    sleep(5)
    btn = browser.find_element_by_class_name("btn-add-to-basket")
    assert btn
