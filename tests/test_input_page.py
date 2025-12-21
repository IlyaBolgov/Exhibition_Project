from pages.inputs_page import InputsPage
from playwright.sync_api import Page


def test_input_field(page: Page):
    inputs_page = InputsPage(page)
    inputs_page.open()
    test_value = "12345"
    inputs_page.set_input_value(test_value)
    value = inputs_page.get_input_value()
    assert value == test_value, f"Expected value {test_value} but {value}"
