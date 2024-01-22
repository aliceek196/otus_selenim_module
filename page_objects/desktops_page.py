from selenium.webdriver.common.by import By


class DesktopsPage:
    HOME_BUTTON = (By.XPATH, "//i[@class='fas fa-home']")
    SORT_CONTROL = (By.ID, "input-sort")
    LEFT_MENU = (By.ID, "column-left")
    FIRST_ITEM = (By.XPATH, "(//div[@class='product-thumb'])[1]")
    LIST_VIEW_BUTTON = (By.ID, "button-list")