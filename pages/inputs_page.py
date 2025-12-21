from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)


class InputsPage:
    URL = "http://the-internet.herokuapp.com/inputs"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        logger.info("Opening Inputs Page: %s", self.URL)
        self.page.goto(self.URL)

    def set_input_value(self, value: str) -> None:
        logger.info("Setting input field value to: %s", value)
        # fill() clears the input before typing
        self.page.fill("input", value)

    def get_input_value(self) -> str:
        value = self.page.locator("input").input_value()
        logger.debug("Current input field value: %s", value)
        return value
