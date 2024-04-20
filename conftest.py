import datetime
import logging
import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--base_url", action="store")
    parser.addoption("--executor", action="store")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--bv")

#
@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    logs = request.config.getoption("--logs")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bv")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'{__name__}.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    executor_url = f"http://{executor}:4444/wd/hub"

    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()

    caps = {
        "browserName": browser,
        "browserVersion": version,
        # "selenoid:options": {
        #     "enableVNC": vnc,
        #     "name": os.getenv("BUILD_NUMBER", str(random.randint(9000, 10000))),
        #     "screenResolution": "1280x2000",
        #     "enableVideo": video,
        #     "enableLog": logs,
        #     "timeZone": "Europe/Moscow",
        #     "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]

    }

    for k, v in caps.items():
        options.set_capability(k, v)

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )
    # driver.log_level = log_level
    # driver.logger = logger
    # driver.test_name = request.node.name

    driver.maximize_window()

    def fin():
        driver.quit()
        # requests.delete(f'http://{executor}:4444/wd/hub/session/{driver.session_id}', verify=False)
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    return driver
