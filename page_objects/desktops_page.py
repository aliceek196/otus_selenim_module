from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from allure import step


class DesktopsPage(BasePage):
    DESKTOP_ENDPOINT = "/en-gb/catalog/desktops"
    HOME_BUTTON = (By.XPATH, "//i[@class='fas fa-home']")
    SORT_CONTROL = (By.ID, "input-sort")
    LEFT_MENU = (By.ID, "column-left")
    FIRST_ITEM = (By.XPATH, "(//div[@class='product-thumb'])[1]")
    LIST_VIEW_BUTTON = (By.ID, "button-list")

    @step("Opening Desktops section")
    def open_desktops(self):
        self.browser.get(self.base_url + self.DESKTOP_ENDPOINT)
        return self

    @step("Checking availability of home button")
    def search_home_button(self):
        self.get_element(self.HOME_BUTTON)
        return self

    @step("Checking availability of sorting buttons")
    def search_sort_controll(self):
        self.get_element(self.SORT_CONTROL)
        return self

    @step("Checking availability of first item")
    def search_first_item(self):
        self.get_element(self.FIRST_ITEM)
        return self

    @step("Checking availability of left menu")
    def search_left_menu(self):
        self.get_element(self.LEFT_MENU)
        return self

    @step("Checking availability of list button")
    def search_list_view(self):
        self.get_element(self.LIST_VIEW_BUTTON)
        return self



