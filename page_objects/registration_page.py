from selenium.webdriver.common.by import By


class RegistrationPage:
    LOGIN_PAGE_LINK = (By.XPATH, "//a[contains(@href, 'route=account/login') and text()='login page']")
    ACCOUNT_DATA = (By.XPATH, "//fieldset[@ID='account']")
    RIGHT_MENU = (By.ID, "column-right")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//input[@name='agree']")
    CONTINUE_BUTTON = (By.XPATH, "//*[text()='Continue']")
