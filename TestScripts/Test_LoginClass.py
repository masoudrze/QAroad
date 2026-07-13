import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPagePOM import LoginPage


@pytest.fixture(scope="function")
def setup():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("http://localhost/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_valid_admin_login(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("supervisor","1")

    wait = WebDriverWait(driver, 5)
    main_menu = wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    assert main_menu.is_displayed(),"login should be successful but it is not"

def test_invalid_admin_login(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("supervisor","1111")

    wait = WebDriverWait(driver, 5)
    actual_text = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".login-alert.ng-binding")
    )
    ).text
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."

    assert expected_text in actual_text,"login should be failed but it is not"


def test_valid_user_login(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("user2","1")

    wait = WebDriverWait(driver, 5)
    main_menu = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[@class='user-panel']"))
    )
    assert main_menu.is_displayed(),"login should be successful but it is not"

def test_invalid_user_login(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("user2","1111")

    wait = WebDriverWait(driver, 5)
    actual_text = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".login-alert.ng-binding")
    )
    ).text
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."

    assert expected_text in actual_text,"login should be failed but it is not"