import configparser
from page_objects.admin_page import AdminPage

config = configparser.ConfigParser()
config.read('config.ini')

# Read credentials from the config file
username = config['Credentials']['admin_username']
password = config['Credentials']['admin_password']


def test_login_admin_page(browser, base_url):
    admin = AdminPage(browser, base_url)
    admin.open_admin()
    admin.input_admin_credentials(username, password)
    admin.click_login_button()
    admin.wait_logged_in()
    admin.logout()


def test_add_item_in_admin(browser, base_url):
    admin = AdminPage(browser, base_url)
    admin.open_admin()
    admin.input_admin_credentials(username, password)
    admin.click_login_button().wait_logged_in()
    admin.open_catalog_menu()
    admin.select_products_section()
    admin.click_add_new_item()
    admin.input_product_name("Samsung Galaxy S24")
    admin.input_meta_tag_title("S24")
    admin.switch_to_data_tab()
    admin.input_model("Product NEW")
    admin.switch_to_seo_tab()
    admin.input_keyword("Samsung")
    admin.click_save_button()
    admin.success_alert_appears()


def test_delete_item_in_admin(browser, base_url):
    admin = AdminPage(browser, base_url)
    admin.open_admin()
    admin.input_admin_credentials(username, password)
    admin.click_login_button().wait_logged_in()
    admin.open_catalog_menu()
    admin.select_products_section()
    admin.filtered_product_name("Samsung Galaxy S24")
    admin.select_deleting_product()
    admin.click_delete_button()
    admin.confirm_action()
    admin.success_alert_appears()


