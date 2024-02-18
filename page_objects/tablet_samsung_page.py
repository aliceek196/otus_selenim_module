from allure import step
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class TabletSamsungPage(BasePage):
    TABLET_SAMSUNG_ENDPOINT = "/en-gb/product/tablet/samsung-galaxy-tab-10-1"
    IMAGE_TITLE = (By.XPATH, "//div[@class='image magnific-popup']/a[@title='Samsung Galaxy Tab 10.1']")
    WISH_LIST_BUTTON = (By.XPATH, "//button[@type='submit']/i[@class='fa-solid fa-heart']")
    QUANITY_INPUT = (By.ID, "input-quantity")
    ADD_CART_BUTTON = (By.XPATH, "//*[text()='Add to Cart']")
    REVIEWS_TAB = (By.XPATH, "//a[contains(@href, '#tab-review')]")

    @step("Open Samsung Tablet page")
    def open_tablet_samsung(self):
        self.browser.get(self.base_url + self.TABLET_SAMSUNG_ENDPOINT)
        return self

    @step("Checking availability of an image title")
    def search_image_title(self):
        self.get_element(self.IMAGE_TITLE)
        return self

    @step("Checking availability of an add to wish list button")
    def search_wish_list_button(self):
        self.get_element(self.WISH_LIST_BUTTON)
        return self

    @step("Checking availability of a quantity button")
    def search_quanity_input(self):
        self.get_element(self.QUANITY_INPUT)
        return self

    @step("Checking availability of an add to cart button")
    def search_add_cart_button(self):
        self.get_element(self.ADD_CART_BUTTON)
        return self

    @step("Checking availability of a reviews tab")
    def search_reviews_tab(self):
        self.get_element(self.REVIEWS_TAB)
        return self


