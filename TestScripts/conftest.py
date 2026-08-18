import os
from datetime import datetime

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from Helpers.config import (
    BASE_URL,
    BROWSER,
    CHROMEDRIVER_PATH,
    HEADLESS,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)


@pytest.fixture(scope="function")
def driver():
    if BROWSER == "chrome":
        options = ChromeOptions()

        if HEADLESS:
            options.add_argument("--headless=new")

        options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")

        if CHROMEDRIVER_PATH:
            browser_driver = webdriver.Chrome(
                service=Service(CHROMEDRIVER_PATH),
                options=options,
            )
        else:
            browser_driver = webdriver.Chrome(options=options)

    elif BROWSER == "firefox":
        options = FirefoxOptions()

        if HEADLESS:
            options.add_argument("-headless")

        browser_driver = webdriver.Firefox(options=options)
        browser_driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

    else:
        raise ValueError(
            f"Unsupported browser: {BROWSER}. Supported browsers: chrome, firefox."
        )

    if not HEADLESS:
        browser_driver.maximize_window()

    try:
        browser_driver.get(BASE_URL)
        yield browser_driver
    finally:
        browser_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser_driver = item.funcargs.get("driver")

        if browser_driver:
            os.makedirs("Screenshots", exist_ok=True)

            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join("Screenshots", filename)

            browser_driver.save_screenshot(filepath)
            print(f"\nScreenshot saved: {filepath}")


