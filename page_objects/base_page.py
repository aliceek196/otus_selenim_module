import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


class BasePage:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def open_browser(self):
        self.browser.get(self.base_url)

    def get_element(self, locator: tuple, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    def scroll_into_view(self, locator):
        self.browser.execute_script("arguments[0].click();", locator)

    def scroll_and_get_element(self, locator: tuple, timeout=3):
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        self.scroll_into_view(element)
        return element

    def element_disappeared(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element(locator))

    def get_element_property(self, element, property_name):
        return element.get_property(property_name)

