import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--base_url")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def browser(request, base_url):
    browser_name = request.config.getoption("--browser")

    _browser = None
    if browser_name == "chrome":
        service = ChromeService()
        _browser = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService()
        _browser = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        service = EdgeService()
        _browser = webdriver.Edge(service=service)

    _browser.maximize_window()

    yield _browser

    _browser.close()
