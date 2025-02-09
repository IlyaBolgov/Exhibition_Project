from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("ilyabolgov", "SuperPassword!")
    flash_message = login_page.get_flash_message()
    assert "You logged into a secure area!" in flash_message, "Valid login should display a success message"

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid", "invalid")
    flash_message = login_page.get_flash_message()
    assert "Invalid username!" in flash_message, "Invalid login should be in error message"
