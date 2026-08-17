import pytest
from PageObjects.LoginPage_POM import LoginPage
from PageObjects.UserIndex_Nav_POM import UserIndexNav
from Helpers.data_loader import DataLoader

@pytest.mark.negative
def test_invalid_admin_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_fail"))
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."
    assert expected_text in login_page.login_failed_message()

@pytest.mark.negative
def test_invalid_user_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_fail"))
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."
    assert expected_text in login_page.login_failed_message()

@pytest.mark.smoke
def test_valid_admin_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))
    assert login_page.is_admin_dashboard_displayed(),"login should be successful but it is not"

@pytest.mark.smoke
def test_valid_user_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_pass"))
    assert login_page.is_user_dashboard_displayed(),"login should be successful but it is not"

@pytest.mark.smoke
def test_valid_admin_login_logout(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))
    logout=UserIndexNav(driver)
    logout.user_logout()
    assert logout.is_logged_out(),"logout should be successful but it is not"

@pytest.mark.smoke
def test_valid_user_login_logout(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_pass"))
    logout=UserIndexNav(driver)
    logout.user_logout()
    assert logout.is_logged_out(),"logout should be successful but it is not"



