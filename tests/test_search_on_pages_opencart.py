from page_objects.main_page import MainPage
from page_objects.desktops_page import DesktopsPage
from page_objects.tablet_samsung_page import TabletSamsungPage
from page_objects.admin_page import AdminPage
from page_objects.registration_page import RegistrationPage


def test_main_page_search(browser, base_url):
    main = MainPage(browser, base_url)
    main.open_browser()
    main.search_store_name()
    main.search_input()
    main.search_button()
    main.search_menu_tabs()
    main.search_cart_button()


def test_desktops_page(browser, base_url):
    desktops = DesktopsPage(browser, base_url)
    desktops.open_desktops()\
        .search_home_button()\
        .search_sort_controll()\
        .search_left_menu()\
        .search_first_item()\
        .search_list_view()


def test_tablet_samsung_page(browser, base_url):
    tablet_samsung = TabletSamsungPage(browser, base_url)
    tablet_samsung.open_tablet_samsung()\
        .search_image_title()\
        .search_quanity_input()\
        .search_reviews_tab()\
        .search_add_cart_button()\
        .search_wish_list_button()


def test_admin_page(browser, base_url):
    admin = AdminPage(browser, base_url)
    admin.open_admin()\
        .search_username()\
        .search_password()\
        .search_login_button()


def test_registration_page(browser, base_url):
    registration = RegistrationPage(browser, base_url)
    registration.open_registration_page()\
        .search_login_link()\
        .search_account_data()\
        .search_right_menu()\
        .search_privacy_policy()\
        .search_continue_button()

