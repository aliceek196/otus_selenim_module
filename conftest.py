import os

import pytest
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--drivers", action="store",
                     default=os.path.expanduser("C:/drivers/"),
                     help="Path to drivers")
    parser.addoption("--base_url")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="93.183.72.83")
    parser.addoption("--bv", action="store", default="105.0")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def browser(request, base_url, _browser=None):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(request.node.name,
                                                    datetime.datetime.now()))

    if executor == "localhost":
        capabilities = {'goog:chromeOptions': {}}

        if browser_name == "chrome":
            service = ChromeService(executable_path=drivers + "/chromedriver")
            _browser = webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FirefoxService(executable_path=drivers + "/geckodriver")
            _browser = webdriver.Firefox(service=service)
        elif browser_name == "edge":
            service = EdgeService(executable_path=drivers + "/msedgedriver")
            _browser = webdriver.Edge(service=service)
        else:
            raise ValueError(f"Browser {browser_name} is not supported.")
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        capabilities = {
            "browserName": browser_name,
            "browserVersion": version,
            "name": "test_opencart",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableLog": logs
            }
        }

        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)

        driver.log_level = log_level
        driver.logger = logger
        driver.test_name = request.node.name

        _browser.maximize_window()

    yield _browser

    _browser.close()
