from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage:
    URL = "http://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        logger.info("Opening Login Page: %s", self.URL)
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        logger.info("Logging in with username: %s", username)
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button.radius")

    def get_flash_message(self) -> str:
        # text_content() retrieves the text content of the element
        message = self.page.locator("#flash").text_content()
        logger.debug("Flash message: %s", message)
        return message.strip() if message else ""
