from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)


class DropdownPage:
    URL = "http://the-internet.herokuapp.com/dropdown"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        logger.info("Opening Dropdown Page: %s", self.URL)
        self.page.goto(self.URL)

    def select_option_by_value(self, value: str) -> None:
        logger.info("Selecting dropdown option with value: %s", value)
        self.page.select_option("#dropdown", value)

    def get_selected_option_text(self) -> str:
        # Get the text of the selected option
        # Option 1: evaluate
        # Option 2: locator option:checked
        selected_text = self.page.locator("#dropdown option:checked").text_content()
        logger.debug("Selected option: %s", selected_text)
        return selected_text.strip() if selected_text else ""
