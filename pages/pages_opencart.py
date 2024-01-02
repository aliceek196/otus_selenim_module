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


class DesktopsPage:
    HOME_BUTTON = (By.XPATH, "//i[@class='fas fa-home']")
    SORT_CONTROL = (By.ID, "input-sort")
    LEFT_MENU = (By.ID, "column-left")
    FIRST_ITEM = (By.XPATH, "(//div[@class='product-thumb'])[1]")
    LIST_VIEW_BUTTON = (By.ID, "button-list")


class TabletSamsungPage:
    IMAGE_TITLE = (By.XPATH, "//div[@class='image magnific-popup']/a[@title='Samsung Galaxy Tab 10.1']")
    WISH_LIST_BUTTON = (By.XPATH, "//button[@type='submit']/i[@class='fa-solid fa-heart']")
    QUANITY_INPUT = (By.ID, "input-quantity")
    ADD_CART_BUTTON = (By.XPATH, "//*[text()='Add to Cart']")
    REVIEWS_TAB = (By.XPATH, "//a[contains(@href, '#tab-review')]")


class AdminPage:
    USERNAME_INPUT = (By.ID, "input-username")
    USER_ICON = (By.XPATH, "//i[@class='fa-solid fa-user']")
    PASSWORD_INPUT = (By.ID, "input-password")
    PASSWORD_ICON = (By.XPATH, "(//i[@class='fa-solid fa-lock'])[2]")
    LOGIN_BUTTON = (By.XPATH, "//*[text()=' Login']")
    USER_PROFILE = (By.ID, "nav-profile")
    LOGOUT_BUTTON = (By.XPATH, "//*[text()='Logout']")


class RegistrationPage:
    LOGIN_PAGE_LINK = (By.XPATH, "//a[contains(@href, 'route=account/login') and text()='login page']")
    ACCOUNT_DATA = (By.XPATH, "//fieldset[@ID='account']")
    RIGHT_MENU = (By.ID, "column-right")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//input[@name='agree']")
    CONTINUE_BUTTON = (By.XPATH, "//*[text()='Continue']")
