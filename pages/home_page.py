from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)


class HomePage:
    URL = "http://the-internet.herokuapp.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        logger.info("Navigating to Home Page: %s", self.URL)
        self.driver.get(self.URL)

    def get_link_by_text(self, text: str):
        logger.info("Looking for link with text: %s", text)
        return self.driver.find_element(By.LINK_TEXT, text)
