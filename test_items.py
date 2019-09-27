import pytest
import time


@pytest.mark.parametrize('language', ["es", "fr"])
def test_button_visible(browser, language):
    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    time.sleep(30)
    button = browser.find_element_by_css_selector("[class*='btn-add-to-basket']")
    assert button, "Button is present"
