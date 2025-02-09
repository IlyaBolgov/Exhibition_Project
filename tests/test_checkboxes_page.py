from pages.checkboxes_page import CheckboxesPage


def test_checkboxes_default_state(driver):
    checkboxes_page = CheckboxesPage(driver)
    checkboxes_page.open()
    checkboxes = checkboxes_page.get_checkboxes()
    assert not checkboxes[
        0
    ].is_selected(), "First checkbox should be unchecked by default"
    assert checkboxes[1].is_selected(), "Second checkbox should be checked by default"


def test_toggle_checkboxes(driver):
    checkboxes_page = CheckboxesPage(driver)
    checkboxes_page.open()
    checkboxes = checkboxes_page.get_checkboxes()
    checkboxes[0].click()
    assert checkboxes[
        0
    ].is_selected(), "The first checkbox should be selected after click"
