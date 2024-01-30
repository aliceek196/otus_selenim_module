from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Search')]")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='btn btn-light btn-lg']")
    CART_BUTTON = (By.CLASS_NAME, "btn btn-inverse btn-block dropdown-toggle")
    MENU_TABS = (By.ID, "menu")
    ADD_FIRST_ITEM_TO_CART_BUTTON = (By.XPATH, "(//i[@class='fa-solid fa-shopping-cart'])[1]")
    CHECK_FIRST_ITEM_IN_CART = (By.XPATH, "//button[contains(text(),' 1 item(s) - $')]")
    EURO_CURRENCY = (By.XPATH, "//*[text()='€']")
    SELECT_EURO_CURRENCY_BUTTON = (By.XPATH, "//*[text()='€ Euro']")
    DOLLAR_CURRENCY = (By.XPATH, "//*[text()='$']")

    def search_button(self):
        self.get_element(self.SEARCH_BUTTON)
        return self

    def search_input(self):
        self.get_element(self.SEARCH_INPUT)
        return self

    def search_menu_tabs(self):
        self.get_element(self.MENU_TABS)
        return self

    def add_first_item_to_cart(self):
        self.get_element(self.ADD_FIRST_ITEM_TO_CART_BUTTON).click()
        return self

    def check_first_item_in_cart(self):
        self.get_element(self.CHECK_FIRST_ITEM_IN_CART)
        return self
