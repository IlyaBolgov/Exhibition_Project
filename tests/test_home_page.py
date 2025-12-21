from pages.home_page import HomePage
from playwright.sync_api import Page


def test_home_page_contains_form_authentication_link(page: Page):
    home = HomePage(page)
    home.open()
    link = home.get_link_by_text("Form Authentication")
    assert (
        link.is_visible()
    ), "Form Authentication link should be visible on the home page"
