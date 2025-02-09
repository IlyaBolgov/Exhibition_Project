from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)

class CheckboxesPage:
    URL = "http://the-internet.herokuapp.com/checkboxes"

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        logger.info("Opening Checkboxes Page: %s", self.URL)
        self.driver.get(self.URL)

    def get_checkboxes(self):
        logger.info("Retrieving all checkboxes")
        return self.driver.find_elements(By.CSS_SELECTOR, "form#checkboxes input[type='checkbox']")
