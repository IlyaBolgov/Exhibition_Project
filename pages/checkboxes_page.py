from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)


class CheckboxesPage:
    URL = "http://the-internet.herokuapp.com/checkboxes"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        logger.info("Opening Checkboxes Page: %s", self.URL)
        self.page.goto(self.URL)

    def get_checkboxes(self):
        logger.info("Retrieving all checkboxes")
        # Return a list of Locators
        return self.page.locator("form#checkboxes input[type='checkbox']").all()
