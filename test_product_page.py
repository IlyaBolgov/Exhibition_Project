import pytest
from .pages.product_page import ProductPage

xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [mask+str(i) for i in range(10) if i != xfile]
x_link = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
links.insert(xfile, x_link)


@pytest.mark.parametrize('link', links)
def test_add_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


# атомарные тест-кейсы:
# def test_add_to_basket_right_name(browser):
#     page = ProductPage(browser, links)
#     page.open()
#     page.add_to_basket()
#     page.should_be_message_about_adding()
#
#
# def test_add_to_basket_right_cost(browser):
#     page = ProductPage(browser, links)
#     page.open()
#     page.add_to_basket()
#     page.should_be_message_basket_total()
