from pages.login_page import LoginPage
from playwright.sync_api import Page


def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    flash_message = login_page.get_flash_message()
    assert (
        "You logged into a secure area!" in flash_message
    ), "Valid login should display a success message"


def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("invalid", "invalid")
    flash_message = login_page.get_flash_message()
    assert (
        "Your username is invalid!" in flash_message
    ), "Invalid login should be in error message"
