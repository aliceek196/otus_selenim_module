import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import AdminPage, MainPage


def test_login_admin_page(browser, base_url):
    username = 'user'
    password = 'bitnami'
    browser.get(f"{base_url}/administration")
    wait = WebDriverWait(browser, 2)
    browser.find_element(*AdminPage.USERNAME_INPUT).send_keys(username)
    browser.find_element(*AdminPage.PASSWORD_INPUT).send_keys(password)
    browser.find_element(*AdminPage.LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(AdminPage.USER_PROFILE))
    browser.find_element(*AdminPage.LOGOUT_BUTTON).click()
    wait.until(EC.visibility_of_element_located(AdminPage.USERNAME_INPUT))


def test_add_item_to_cart(browser, base_url):
    browser.get(f"{base_url}")
    wait = WebDriverWait(browser, 2)
    browser.find_element(*MainPage.ADD_FIRST_ITEM_TO_CART_BUTTON).click()
    wait.until(EC.visibility_of_element_located(MainPage.CHECK_FIRST_ITEM_IN_CART))


@pytest.mark.parametrize("page", ["", "en-gb/catalog/desktops"])
def test_currency_change(browser, base_url, page):
    browser.get(f"{base_url}/{page}")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(MainPage.DOLLAR_CURRENCY))
    dollar_price = browser.find_element(*MainPage.FIRST_ITEM_PRICE).get_property("textContent")
    browser.find_element(*MainPage.CURRENCY_BUTTON).click()
    wait.until(EC.visibility_of_element_located(MainPage.SELECT_EURO_CURRENCY_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(MainPage.EURO_CURRENCY))
    euro_price = browser.find_element(*MainPage.FIRST_ITEM_PRICE).get_property("textContent")
    assert euro_price != dollar_price
