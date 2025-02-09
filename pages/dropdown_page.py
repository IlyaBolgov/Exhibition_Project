from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.logger import get_logger

logger = get_logger(__name__)

class DropdownPage:
    URL = "http://the-internet.herokuapp.com/dropdown"

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        logger.info("Opening Dropdown Page: %s", self.URL)
        self.driver.get(self.URL)

    def select_option_by_value(self, value: str) -> None:
        logger.info("Selecting dropdown option with value: %s", value)
        dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_value(value)

    def get_selected_option_text(self) -> str:
        dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
        selected_text = dropdown.first_selected_option.text
        logger.debug("Selected option: %s", selected_text)
        return selected_text
