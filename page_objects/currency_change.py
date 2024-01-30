from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CurrencyPage(BasePage):
    CURRENCY_BUTTON = (By.XPATH, "//*[text()='Currency']")
    EURO_CURRENCY = (By.XPATH, "//*[text()='€']")
    SELECT_EURO_CURRENCY_BUTTON = (By.XPATH, "//*[text()='€ Euro']")
    DOLLAR_CURRENCY = (By.XPATH, "//*[text()='$']")
    FIRST_ITEM_PRICE = (By.XPATH, "(//span[@class='price-new'])[1]")

    def currency_memorization(self):
        self.get_element(self.FIRST_ITEM_PRICE).get_property("textContent")
        return self

    def search_currency(self):
        self.get_element(self.CURRENCY_BUTTON)
        return self


