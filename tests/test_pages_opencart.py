from selenium.webdriver.support.wait import WebDriverWait
from pages import MainPage, DesktopsPage, TabletSamsungPage, AdminPage, RegistrationPage
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_search(browser, base_url):
    browser.get(f"{base_url}")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(MainPage.CURRENCY_BUTTON))
    wait.until(EC.visibility_of_element_located(MainPage.SEARCH_INPUT))
    wait.until(EC.visibility_of_element_located(MainPage.SEARCH_BUTTON))
    wait.until(EC.visibility_of_element_located(MainPage.MENU_TABS))


def test_desktops_page(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(DesktopsPage.HOME_BUTTON))
    wait.until(EC.visibility_of_element_located(DesktopsPage.SORT_CONTROL))
    wait.until(EC.visibility_of_element_located(DesktopsPage.LIST_VIEW_BUTTON))
    wait.until(EC.visibility_of_element_located(DesktopsPage.FIRST_ITEM))
    wait.until(EC.visibility_of_element_located(DesktopsPage.LEFT_MENU))


def test_tablet_samsung_page(browser, base_url):
    browser.get(f"{base_url}/en-gb/product/tablet/samsung-galaxy-tab-10-1")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(TabletSamsungPage.REVIEWS_TAB))
    wait.until(EC.visibility_of_element_located(TabletSamsungPage.IMAGE_TITLE))
    wait.until(EC.visibility_of_element_located(TabletSamsungPage.WISH_LIST_BUTTON))
    wait.until(EC.visibility_of_element_located(TabletSamsungPage.ADD_CART_BUTTON))
    wait.until(EC.visibility_of_element_located(TabletSamsungPage.QUANITY_INPUT))


def test_admin_page(browser, base_url):
    browser.get(f"{base_url}/administration")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(AdminPage.USERNAME_INPUT))
    wait.until(EC.visibility_of_element_located(AdminPage.USER_ICON))
    wait.until(EC.visibility_of_element_located(AdminPage.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(AdminPage.PASSWORD_ICON))
    wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))


def test_registration_page(browser, base_url):
    browser.get(f"{base_url}/index.php?route=account/register")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(RegistrationPage.LOGIN_PAGE_LINK))
    wait.until(EC.visibility_of_element_located(RegistrationPage.ACCOUNT_DATA))
    wait.until(EC.visibility_of_element_located(RegistrationPage.RIGHT_MENU))
    wait.until(EC.visibility_of_element_located(RegistrationPage.PRIVACY_POLICY_CHECKBOX))
    wait.until(EC.visibility_of_element_located(RegistrationPage.CONTINUE_BUTTON))
