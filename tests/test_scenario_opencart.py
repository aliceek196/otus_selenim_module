# import pytest
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from page_objects.admin_page import AdminPage
# from page_objects.currency_change import CurrencyPage
# from page_objects.main_page import MainPage
# import configparser
#
# config = configparser.ConfigParser()
# config.read('config.ini')
#
# # Read credentials from the config file
# username = config['Credentials']['admin_username']
# password = config['Credentials']['admin_password']
#
#
# def test_login_admin_page(browser, base_url):
#     browser.get(f"{base_url}/administration")
#     wait = WebDriverWait(browser, 2)
#     AdminPage(browser).input_admin_credentials(username, password)\
#         .login_button().click()\
#         .wait_logged_in()
#     AdminPage(browser).logout()
#
#
# def test_add_item_to_cart(browser, base_url):
#     browser.get(f"{base_url}")
#     wait = WebDriverWait(browser, 2)
#     MainPage(browser).add_first_item_to_cart().check_first_item_in_cart()
#
#
# @pytest.mark.parametrize("page", ["", "en-gb/catalog/desktops"])
# def test_currency_change(browser, base_url, page):
#     browser.get(f"{base_url}/{page}")
#     wait = WebDriverWait(browser, 2)
#     # проверка соответствия валюты в магазине
#     # wait.until(EC.visibility_of_element_located(main_page.DOLLAR_CURRENCY))
#     # запоминаем цену в начальной валюте
#     first_currency_price = CurrencyPage(browser).currency_memorization()
#     # смена валюты
#     browser.find_element(*main_page.CURRENCY_BUTTON).click()
#     wait.until(EC.visibility_of_element_located(main_page.SELECT_EURO_CURRENCY_BUTTON)).click()
#     # проверка соответствия валюты в магазине
#     # wait.until(EC.visibility_of_element_located(main_page.EURO_CURRENCY))
#     # запоминаем цену после смены валюты
#     second_currency_price = CurrencyPage(browser).currency_memorization()
#     # проверка что цена отличается после смены валюты
#     assert first_currency_price != second_currency_price
#
# # Добавление нового товара в разделе администратора.
# # Удаление товара из списка в разделе администартора.
# # Регистрация нового пользователя в магазине опенкарта.
# # Переключение валют из верхнего меню опенкарта.
