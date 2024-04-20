from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from allure import step


class MainPage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Search')]")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='btn btn-light btn-lg']")
    CART_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-inverse btn-block dropdown-toggle']")
    MENU_TABS = (By.ID, "menu")
    ADD_FIRST_ITEM_TO_CART_BUTTON = (By.XPATH, "(//i[@class='fa-solid fa-shopping-cart'])[1]")
    CHECK_FIRST_ITEM_IN_CART = (By.XPATH, "//button[contains(text(),' 1 item(s) - $')]")
    EURO_CURRENCY = (By.XPATH, "//*[text()='€']")
    SELECT_EURO_CURRENCY_BUTTON = (By.XPATH, "//*[text()='€ Euro']")
    DOLLAR_CURRENCY = (By.XPATH, "//*[text()='$']")
    STORE_NAME = (By.CSS_SELECTOR, "img[alt='Your Store']")

    @step("Checking availability of a store name")
    def search_store_name(self):
        self.get_element(self.STORE_NAME)
        return self

    @step("Checking availability of a search button")
    def search_button(self):
        self.get_element(self.SEARCH_BUTTON)
        return self

    @step("Checking availability of a search input")
    def search_input(self):
        self.get_element(self.SEARCH_INPUT)
        return self

    @step("Checking availability of tabs menu")
    def search_menu_tabs(self):
        self.get_element(self.MENU_TABS)
        return self

    @step("Checking availability of a cart button")
    def search_cart_button(self):
        self.get_element(self.CART_BUTTON)
        return self

    @step("Adding the first item to the cart")
    def add_first_item_to_cart(self):
        self.scroll_and_get_element(self.ADD_FIRST_ITEM_TO_CART_BUTTON)
        return self

    @step("Check availability of the first item in the cart")
    def check_first_item_in_cart(self):
        self.get_element(self.CHECK_FIRST_ITEM_IN_CART)
        return self
