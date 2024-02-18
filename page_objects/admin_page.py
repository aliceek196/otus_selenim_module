from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from allure import step


class AdminPage(BasePage):
    ADMIN_ENDPOINT = "/administration"
    USERNAME_INPUT = (By.ID, "input-username")
    USER_ICON = (By.XPATH, "//i[@class='fa-solid fa-user']")
    PASSWORD_INPUT = (By.ID, "input-password")
    PASSWORD_ICON = (By.XPATH, "(//i[@class='fa-solid fa-lock'])[2]")
    LOGIN_BUTTON = (By.XPATH, "//*[text()=' Login']")
    USER_PROFILE = (By.ID, "nav-profile")
    LOGOUT_BUTTON = (By.XPATH, "//*[text()='Logout']")
    CATALOG = (By.XPATH, "//*[text()=' Catalog']")
    PRODUCTS = (By.XPATH, "(//a[contains(text(), 'Products')])[1]")
    ADD_NEW_ITEM_BUTTON = (By.XPATH, "(//i[@class='fa-solid fa-plus'])[1]")
    PRODUCT_NAME_INPUT = (By.XPATH, "//input[@name='product_description[1][name]']")
    META_TAG_INPUT = (By.XPATH, "//input[@name='product_description[1][meta_title]']")
    DATA_TAB = (By.XPATH, "//a[@role='tab' and text()='Data']")
    MODEL_INPUT = (By.ID, "input-model")
    SEO_TAB = (By.XPATH, "//a[@role='tab' and text()='SEO']")
    SEO_KEYWORD_INPUT = (By.ID, "input-keyword-0-1")
    SAVE_PRODUCT_BUTTON = (By.XPATH, "//i[@class='fa-solid fa-floppy-disk']")
    SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    FILTER_PRODUCT_NAME_INPUT = (By.ID, "input-name")
    FILTER_BUTTON = (By.ID, "button-filter")
    SELECT_PRODUCT_CHECKBOX = (By.XPATH, "(//input[@type='checkbox'])[2]")
    DELETE_PRODUCT_BUTTON = (By.XPATH, "//i[@class='fa-regular fa-trash-can']")

    @step("Open admin auth page")
    def open_admin(self):
        self.browser.get(self.base_url + self.ADMIN_ENDPOINT)
        return self

    @step("Entering login and password from admin area")
    def input_admin_credentials(self, username, password):
        self.input_value(self.USERNAME_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        return self

    @step("Waiting for login to admin area")
    def wait_logged_in(self):
        self.get_element(self.USER_PROFILE)
        return self

    @step("Logging out of the admin area")
    def logout(self):
        self.get_element(self.LOGOUT_BUTTON).click()
        self.get_element(self.USERNAME_INPUT)
        return self

    @step("Checking availability of a field for entering username")
    def search_username(self):
        self.get_element(self.USERNAME_INPUT)
        self.get_element(self.USER_ICON)
        return self

    @step("Checking availability of a field for entering password")
    def search_password(self):
        self.get_element(self.PASSWORD_INPUT)
        self.get_element(self.PASSWORD_ICON)
        return self

    @step("Checking availability of login button")
    def search_login_button(self):
        self.get_element(self.LOGIN_BUTTON)
        return self

    @step("Checking login button has been clicked")
    def click_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()
        return self

    @step("Checking catalog menu has been clicked")
    def open_catalog_menu(self):
        self.get_element(self.CATALOG).click()
        return self

    @step("Checking products section has been clicked")
    def select_products_section(self):
        self.get_element(self.PRODUCTS).click()
        return self

    @step("Checking new item button has been clicked")
    def click_add_new_item(self):
        self.get_element(self.ADD_NEW_ITEM_BUTTON).click()
        return self

    @step("Checking product name has been input")
    def input_product_name(self, name):
        self.input_value(self.PRODUCT_NAME_INPUT, name)
        return self

    @step("Checking metatag has been input")
    def input_meta_tag_title(self, metatag):
        self.input_value(self.META_TAG_INPUT, metatag)
        return self

    @step("Checking switching to data tab")
    def switch_to_data_tab(self):
        self.get_element(self.DATA_TAB).click()
        return

    @step("Checking model name has been input")
    def input_model(self, model):
        self.input_value(self.MODEL_INPUT, model)
        return self

    @step("Checking switching to SEO tab")
    def switch_to_seo_tab(self):
        self.get_element(self.SEO_TAB).click()
        return self

    @step("Checking keyword has been input")
    def input_keyword(self, keyword):
        self.input_value(self.SEO_KEYWORD_INPUT, keyword)
        return self

    @step("Checking save button has been clicked")
    def click_save_button(self):
        self.get_element(self.SAVE_PRODUCT_BUTTON).click()
        return self

    @step("Checking success alert has been appears")
    def success_alert_appears(self):
        self.get_element(self.SUCCESS_ALERT)
        return self

    @step("Checking the filter setting by product name")
    def filtered_product_name(self, name):
        self.input_value(self.FILTER_PRODUCT_NAME_INPUT, name)
        self.get_element(self.FILTER_BUTTON).click()
        return self

    @step("Checking the product selection for removal")
    def select_deleting_product(self):
        self.get_element(self.SELECT_PRODUCT_CHECKBOX).click()
        return self

    @step("Check delete button has been clicked")
    def click_delete_button(self):
        self.get_element(self.DELETE_PRODUCT_BUTTON).click()
        return self

    @step("Checking for action confirmation on a page")
    def confirm_action(self):
        self.browser.switch_to.alert.accept()
        return self



