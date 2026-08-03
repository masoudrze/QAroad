import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.get("http://192.168.101.117/")
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # فقط اگر مرحله اجرای تست Fail شود
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("Screenshots", exist_ok=True)

            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            filename = f"{test_name}_{timestamp}.png"

            filepath = os.path.join("Screenshots", filename)

            driver.save_screenshot(filepath)

            print(f"\nScreenshot saved: {filepath}")