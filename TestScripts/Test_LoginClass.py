import allure
import pytest
from Helpers.data_loader import DataLoader
from PageObjects.LoginPage_POM import LoginPage
from PageObjects.UserIndex_Nav_POM import UserIndexNav


@pytest.mark.blocker
@allure.epic("Authentication")
@allure.feature("User Login")
@allure.story("Admin User Entered Wrong Credential")
@allure.title("Invalid Admin Login")
@allure.severity(allure.severity_level.BLOCKER)
def test_invalid_admin_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_fail"))
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."
    assert expected_text in login_page.login_failed_message()


@pytest.mark.dependency(
    depends=["create_user"]
)
@pytest.mark.blocker
@allure.epic("Authentication")
@allure.feature("User Login")
@allure.story("Simple User Entered Wrong Credential")
@allure.title("Invalid User Login")
@allure.severity(allure.severity_level.BLOCKER)
def test_invalid_user_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_fail"))
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."
    assert expected_text in login_page.login_failed_message()


@pytest.mark.dependency(name="admin_login")
@pytest.mark.blocker
@allure.epic("Authentication")
@allure.feature("User Login")
@allure.story("Admin User Correct Credential")
@allure.title("Valid Admin Login")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_admin_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))
    assert login_page.is_admin_dashboard_displayed(), (
        "login should be successful but it is not"
    )

@pytest.mark.dependency(
    name="user_login",
    depends=["create_user"]
)
@pytest.mark.blocker
@allure.epic("Authentication")
@allure.feature("User Login")
@allure.story("Simple User Correct Credential")
@allure.title("Valid User Login")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_user_login(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_pass"))
    assert login_page.is_user_dashboard_displayed(), (
        "login should be successful but it is not"
    )

@pytest.mark.dependency(
    depends=["admin_login"]
)
@pytest.mark.blocker
@allure.epic("Authentication")
@allure.feature("User Login")
@allure.story("Admin User Login And Logout")
@allure.title("Valid Admin Login And Logout")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_admin_login_logout(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))
    logout = UserIndexNav(driver)
    logout.user_logout()
    assert logout.is_logged_out(), "logout should be successful but it is not"


@pytest.mark.dependency(
    depends=["user_login"]
)
@pytest.mark.blocker
@allure.epic("Authentication")
@allure.feature("User Login")
@allure.story("Simple User Login And Logout")
@allure.title("Valid Simple Login And Logout")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_user_login_logout(driver):
    login_page = LoginPage(driver)
    login_page.login(**DataLoader.load_login("user_pass"))
    logout = UserIndexNav(driver)
    logout.user_logout()
    assert logout.is_logged_out(), "logout should be successful but it is not"
