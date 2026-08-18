import allure

from Helpers.data_loader import DataLoader
from PageObjects.LoginPage_POM import LoginPage
from PageObjects.UserIndex_Nav_POM import UserIndexNav

@allure.epic("Login Management")
@allure.feature("User Login")
@allure.story("Admin User Entered Wrong Credential")
@allure.title("Invalid admin login")
@allure.severity(allure.severity_level.BLOCKER)
def test_invalid_admin_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_fail"))
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."
    assert expected_text in login_page.login_failed_message()


@allure.epic("Login Management")
@allure.feature("User Login")
@allure.story("simple User Entered Wrong Credential")
@allure.title("Invalid user login")
@allure.severity(allure.severity_level.BLOCKER)
def test_invalid_user_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_fail"))
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."
    assert expected_text in login_page.login_failed_message()


@allure.epic("Login Management")
@allure.feature("User Login")
@allure.story("Admin User Correct login")
@allure.title("valid admin login")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_admin_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))
    assert login_page.is_admin_dashboard_displayed(), (
        "login should be successful but it is not"
    )


@allure.epic("Login Management")
@allure.feature("User Login")
@allure.story("Simple User Correct login")
@allure.title("valid user login")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_user_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_pass"))
    assert login_page.is_user_dashboard_displayed(), (
        "login should be successful but it is not"
    )


@allure.epic("Login Management")
@allure.feature("User Login")
@allure.story("Admin User Logged in and Logged out")
@allure.title("valid admin login logout")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_admin_login_logout(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))
    logout = UserIndexNav(driver)
    logout.user_logout()
    assert logout.is_logged_out(), "logout should be successful but it is not"


@allure.epic("Login Management")
@allure.feature("User Login")
@allure.story("simple User Logged in and Logged out")
@allure.title("valid simple login logout")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_user_login_logout(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_pass"))
    logout = UserIndexNav(driver)
    logout.user_logout()
    assert logout.is_logged_out(), "logout should be successful but it is not"
