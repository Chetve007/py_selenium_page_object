link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser_fix):
    browser_fix.get(link)
    browser_fix.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser_fix):
    browser_fix.get(link)
    browser_fix.find_element_by_css_selector("#magic_link")


# pytest -v --tb=line --reruns 1 --browser_name=CHROME third_block/test_rerun.py
