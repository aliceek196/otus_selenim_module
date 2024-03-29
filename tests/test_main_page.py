from page_objects.main_page import MainPage
from allure import title


@title("Checking adding an item to cart")
def test_add_item_to_cart(browser, base_url):
    main = MainPage(browser, base_url)
    main.open_browser()
    main.add_first_item_to_cart()
    main.check_first_item_in_cart()


