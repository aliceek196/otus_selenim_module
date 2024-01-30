from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminPage(BasePage):
    ADMIN_ENDPOINT = "/administration"
    USERNAME_INPUT = (By.ID, "input-username")
    USER_ICON = (By.XPATH, "//i[@class='fa-solid fa-user']")
    PASSWORD_INPUT = (By.ID, "input-password")
    PASSWORD_ICON = (By.XPATH, "(//i[@class='fa-solid fa-lock'])[2]")
    LOGIN_BUTTON = (By.XPATH, "//*[text()=' Login']")
    USER_PROFILE = (By.ID, "nav-profile")
    LOGOUT_BUTTON = (By.XPATH, "//*[text()='Logout']")

    def open_admin(self):
        self.browser.get(self.base_url + self.ADMIN_ENDPOINT)
        return self

    def input_admin_credentials(self, username, password):
        self.input_value(self.USERNAME_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        return self

    def wait_logged_in(self):
        self.get_element(self.USER_PROFILE)
        return self

    def logout(self):
        self.get_element(self.LOGIN_BUTTON).click()
        self.get_element(self.USERNAME_INPUT)
        return self

    def search_username(self):
        self.get_element(self.USERNAME_INPUT)
        self.get_element(self.USER_ICON)
        return self

    def search_password(self):
        self.get_element(self.PASSWORD_INPUT)
        self.get_element(self.PASSWORD_ICON)
        return self

    def login_button(self):
        self.get_element(self.LOGIN_BUTTON)
        return self

