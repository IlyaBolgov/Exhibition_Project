import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser type: chrome or firefox",
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def driver(browser):
    if browser.lower() == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run headless for CI environments
        service = ChromeService(ChromeDriverManager().install())
        driver_instance = webdriver.Chrome(service=service, options=options)
    elif browser.lower() == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver_instance = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver_instance.implicitly_wait(10)
    yield driver_instance
    driver_instance.quit()
