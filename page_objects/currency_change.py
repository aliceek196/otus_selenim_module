from selenium.webdriver.common.by import By


class CurrencyPage:
    CURRENCY_BUTTON = (By.XPATH, "//*[text()='Currency']")
    EURO_CURRENCY = (By.XPATH, "//*[text()='€']")
    SELECT_EURO_CURRENCY_BUTTON = (By.XPATH, "//*[text()='€ Euro']")
    DOLLAR_CURRENCY = (By.XPATH, "//*[text()='$']")

    def currency_memorization(self):
        self.find_element(self.FIRST_ITEM_PRICE).get_property("textContent")
