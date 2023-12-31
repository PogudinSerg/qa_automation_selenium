import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from .pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


