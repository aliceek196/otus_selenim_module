from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from allure import step


class CurrencyPage(BasePage):
    CURRENCY_BUTTON = (By.XPATH, "//*[text()='Currency']")
    EURO_CURRENCY = (By.XPATH, "//*[text()='€']")
    SELECT_EURO_CURRENCY_BUTTON = (By.XPATH, "//*[text()='€ Euro']")
    DOLLAR_CURRENCY = (By.XPATH, "//*[text()='$']")
    FIRST_ITEM_PRICE = (By.XPATH, "(//span[@class='price-new'])[1]")

    @step("Get and memorize the price of the first item, excluding currency")
    def currency_memorization(self):
        first_item_price = self.scroll_and_get_element(self.FIRST_ITEM_PRICE)
        price_text = self.get_element_property(first_item_price, "textContent")
        return price_text

    @step("Change currency to euro")
    def change_currency_to_euro(self):
        self.get_element(self.CURRENCY_BUTTON).click()
        self.get_element(self.SELECT_EURO_CURRENCY_BUTTON).click()
        return self




