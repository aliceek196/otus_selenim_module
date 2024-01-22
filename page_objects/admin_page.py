from selenium.webdriver.common.by import By


class AdminPage:
    USERNAME_INPUT = (By.ID, "input-username")
    USER_ICON = (By.XPATH, "//i[@class='fa-solid fa-user']")
    PASSWORD_INPUT = (By.ID, "input-password")
    PASSWORD_ICON = (By.XPATH, "(//i[@class='fa-solid fa-lock'])[2]")
    LOGIN_BUTTON = (By.XPATH, "//*[text()=' Login']")
    USER_PROFILE = (By.ID, "nav-profile")
    LOGOUT_BUTTON = (By.XPATH, "//*[text()='Logout']")

    def login(self, username, password):
        self.input_value(self.USERNAME_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def wait_logged_in(self):
        self.get_element(self.USER_PROFILE)
        return self
