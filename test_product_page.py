from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_add_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()


def test_add_to_basket_right_name(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_about_adding()


def test_add_to_basket_right_cost(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_basket_total()
