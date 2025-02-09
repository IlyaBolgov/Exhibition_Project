from pages.home_page import HomePage

def test_home_page_contains_form_authentication_link(driver):
    home = HomePage(driver)
    home.open()
    link = home.get_link_by_text("Form Authentication")
    assert link.is_displayed(), "Form Authentication link should be visible on the home page"
