from pages.checkboxes_page import CheckboxesPage
from playwright.sync_api import Page


def test_checkboxes_default_state(page: Page):
    checkboxes_page = CheckboxesPage(page)
    checkboxes_page.open()
    checkboxes = checkboxes_page.get_checkboxes()
    assert not checkboxes[
        0
    ].is_checked(), "First checkbox should be unchecked by default"
    assert checkboxes[1].is_checked(), "Second checkbox should be checked by default"


def test_toggle_checkboxes(page: Page):
    checkboxes_page = CheckboxesPage(page)
    checkboxes_page.open()
    checkboxes = checkboxes_page.get_checkboxes()
    # Click expects the element to be visible and stable
    checkboxes[0].click()
    assert checkboxes[
        0
    ].is_checked(), "The first checkbox should be selected after click"
