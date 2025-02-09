from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)

class InputsPage:
    URL = "http://the-internet.herokuapp.com/inputs"

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        logger.info("Opening Inputs Page: %s", self.URL)
        self.driver.get(self.URL)

    def set_input_value(self, value: str) -> None:
        logger.info("Setting input field value to: %s", value)
        input_elem = self.driver.find_element(By.TAG_NAME, "input")
        input_elem.clear()
        input_elem.send_keys(value)

    def get_input_value(self) -> str:
        input_elem = self.driver.find_element(By.TAG_NAME, "input")
        value = input_elem.get_attribute("value")
        logger.debug("Current input field value: %s", value)
        return value
