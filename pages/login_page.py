from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage:
    URL = "http://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        logger.info("Opening Login Page: %s", self.URL)
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        logger.info("Logging in with username: %s", username)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    def get_flash_message(self) -> str:
        flash_elem = self.driver.find_element(By.ID, "flash")
        message = flash_elem.text
        logger.debug("Flash message: %s", message)
        return message
