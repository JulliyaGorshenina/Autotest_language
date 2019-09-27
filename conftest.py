import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def language_choice(request, browser=None):
    language = request.config.getoption("language")
    browser = None
    if language == "es":
        browser.get("http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    elif language == "fr":
        browser.get("http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    else:
        raise pytest.UsageError("--language should be es or fr")

