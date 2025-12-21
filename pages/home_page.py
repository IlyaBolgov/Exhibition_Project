from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)


class HomePage:
    URL = "http://the-internet.herokuapp.com/"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        logger.info("Navigating to Home Page: %s", self.URL)
        self.page.goto(self.URL)

    def get_link_by_text(self, text: str):
        logger.info("Looking for link with text: %s", text)
        return self.page.get_by_role("link", name=text)
