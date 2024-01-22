from selenium.webdriver.common.by import By


class TabletSamsungPage:
    IMAGE_TITLE = (By.XPATH, "//div[@class='image magnific-popup']/a[@title='Samsung Galaxy Tab 10.1']")
    WISH_LIST_BUTTON = (By.XPATH, "//button[@type='submit']/i[@class='fa-solid fa-heart']")
    QUANITY_INPUT = (By.ID, "input-quantity")
    ADD_CART_BUTTON = (By.XPATH, "//*[text()='Add to Cart']")
    REVIEWS_TAB = (By.XPATH, "//a[contains(@href, '#tab-review')]")
