from selenium.webdriver.support.wait import WebDriverWait
from page_objects import main_page, desktops_page, tablet_samsung_page, admin_page, registration_page
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_search(browser, base_url):
    browser.get(f"{base_url}")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(main_page.CURRENCY_BUTTON))
    wait.until(EC.visibility_of_element_located(main_page.SEARCH_INPUT))
    wait.until(EC.visibility_of_element_located(main_page.SEARCH_BUTTON))
    wait.until(EC.visibility_of_element_located(main_page.MENU_TABS))


def test_desktops_page(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(desktops_page.HOME_BUTTON))
    wait.until(EC.visibility_of_element_located(desktops_page.SORT_CONTROL))
    wait.until(EC.visibility_of_element_located(desktops_page.LIST_VIEW_BUTTON))
    wait.until(EC.visibility_of_element_located(desktops_page.FIRST_ITEM))
    wait.until(EC.visibility_of_element_located(desktops_page.LEFT_MENU))


def test_tablet_samsung_page(browser, base_url):
    browser.get(f"{base_url}/en-gb/product/tablet/samsung-galaxy-tab-10-1")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(tablet_samsung_page.REVIEWS_TAB))
    wait.until(EC.visibility_of_element_located(tablet_samsung_page.IMAGE_TITLE))
    wait.until(EC.visibility_of_element_located(tablet_samsung_page.WISH_LIST_BUTTON))
    wait.until(EC.visibility_of_element_located(tablet_samsung_page.ADD_CART_BUTTON))
    wait.until(EC.visibility_of_element_located(tablet_samsung_page.QUANITY_INPUT))


def test_admin_page(browser, base_url):
    browser.get(f"{base_url}/administration")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(admin_page.USERNAME_INPUT))
    wait.until(EC.visibility_of_element_located(admin_page.USER_ICON))
    wait.until(EC.visibility_of_element_located(admin_page.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(admin_page.PASSWORD_ICON))
    wait.until(EC.visibility_of_element_located(admin_page.LOGIN_BUTTON))


def test_registration_page(browser, base_url):
    browser.get(f"{base_url}/index.php?route=account/register")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(registration_page.LOGIN_PAGE_LINK))
    wait.until(EC.visibility_of_element_located(registration_page.ACCOUNT_DATA))
    wait.until(EC.visibility_of_element_located(registration_page.RIGHT_MENU))
    wait.until(EC.visibility_of_element_located(registration_page.PRIVACY_POLICY_CHECKBOX))
    wait.until(EC.visibility_of_element_located(registration_page.CONTINUE_BUTTON))
