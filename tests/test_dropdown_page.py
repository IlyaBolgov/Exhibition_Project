from pages.dropdown_page import DropdownPage


def test_dropdown_selection(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.open()
    dropdown_page.select_option_by_value("1")
    selected = dropdown_page.get_selected_option_text()
    assert "Option 1" in selected, "Dropdown should selected Option 1"

    dropdown_page.select_option_by_value("2")
    selected = dropdown_page.get_selected_option_text()
    assert "Option 2" in selected, "Dropdown should selected Option 2"
