from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    REGISTRATION_ENDPOINT = "/index.php?route=account/register"
    LOGIN_PAGE_LINK = (By.XPATH, "//a[contains(@href, 'route=account/login') and text()='login page']")
    ACCOUNT_DATA = (By.XPATH, "//fieldset[@ID='account']")
    RIGHT_MENU = (By.ID, "column-right")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//input[@name='agree']")
    CONTINUE_BUTTON = (By.XPATH, "//*[text()='Continue']")
    FIRST_NAME_INPUT = (By.ID, "input-firstname")
    LAST_NAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_REGISTRATION_TEXT = (By.XPATH, "//*[text()='Congratulations! Your new account has been successfully "
                                           "created!']")

    def open_registration_page(self):
        self.browser.get(self.base_url + self.REGISTRATION_ENDPOINT)
        return self

    def search_login_link(self):
        self.get_element(self.LOGIN_PAGE_LINK)
        return self

    def search_account_data(self):
        self.get_element(self.ACCOUNT_DATA)
        return self

    def search_right_menu(self):
        self.get_element(self.RIGHT_MENU)
        return self

    def search_privacy_policy(self):
        self.get_element(self.PRIVACY_POLICY_CHECKBOX)
        return self

    def search_continue_button(self):
        self.get_element(self.CONTINUE_BUTTON)
        return self

    def input_first_name(self, first_name):
        self.input_value(self.FIRST_NAME_INPUT, first_name)
        return self

    def input_last_name(self, last_name):
        self.input_value(self.LAST_NAME_INPUT, last_name)
        return self

    def input_email(self, email):
        self.input_value(self.EMAIL_INPUT, email)
        return self

    def input_password(self, password):
        self.input_value(self.PASSWORD_INPUT, password)
        return self

    def confirm_privacy_policy(self):
        self.get_element(self.PRIVACY_POLICY_CHECKBOX).click()
        return self

    def select_continue_button(self):
        self.get_element(self.CONTINUE_BUTTON).click()
        return self

    def confirm_registration(self):
        self.get_element(self.CONFIRM_REGISTRATION_TEXT)
        return self
