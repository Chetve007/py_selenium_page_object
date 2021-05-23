link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser_fix):
    browser_fix.get(link)
    browser_fix.find_element_by_css_selector("#login_link")
