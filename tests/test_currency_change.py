import pytest
from page_objects.currency_change import CurrencyPage


@pytest.mark.parametrize("page", ["", "/en-gb/catalog/desktops"])
def test_currency_change(browser, base_url, page):
    currency = CurrencyPage(browser, base_url + page)
    currency.open_browser()
    first_currency_price = currency.currency_memorization()
    currency.change_currency_to_euro()
    euro_currency_price = currency.currency_memorization()
    assert first_currency_price != euro_currency_price
