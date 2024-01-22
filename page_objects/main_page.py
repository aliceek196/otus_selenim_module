from selenium.webdriver.common.by import By


class MainPage:
    CURRENCY_BUTTON = (By.XPATH, "//*[text()='Currency']")
    SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Search')]")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='btn btn-light btn-lg']")
    CART_BUTTON = (By.CLASS_NAME, "btn btn-inverse btn-block dropdown-toggle")
    MENU_TABS = (By.ID, "menu")
    ADD_FIRST_ITEM_TO_CART_BUTTON = (By.XPATH, "(//i[@class='fa-solid fa-shopping-cart'])[1]")
    CHECK_FIRST_ITEM_IN_CART = (By.XPATH, "//button[contains(text(),' 1 item(s) - $')]")
    FIRST_ITEM_PRICE = (By.XPATH, "(//span[@class='price-new'])[1]")
    EURO_CURRENCY = (By.XPATH, "//*[text()='€']")
    SELECT_EURO_CURRENCY_BUTTON = (By.XPATH, "//*[text()='€ Euro']")
    DOLLAR_CURRENCY = (By.XPATH, "//*[text()='$']")
