import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):  # обработчик опции
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Supported browsers are: chrome")  # в дальнейшем будет расширена поддержка других браузеров
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose language: '--language=en', '--language=es', etc.")


@pytest.fixture(scope="function")  # обрабатывает переданные в опции данные
def browser(request):
    browser_name = request.config.getoption(
        "browser_name")  # логика обработки командной строки
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        # в дальнейшем будет расширена поддержка других браузеров
        raise pytest.UsageError("--browser_name should be chrome or empty")
    yield browser
    print("\nquit browser..")
    browser.quit()
