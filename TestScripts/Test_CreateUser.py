import pytest
import allure
from Helpers.data_loader import DataLoader
from PageObjects.Create_User_POM import UserManagementPage
from PageObjects.LoginPage_POM import LoginPage


@pytest.mark.dependency(
    name="create_user",
    depends=["create_group"]
)
@pytest.mark.blocker
@allure.epic("Definitions")
@allure.feature("Create User")
@allure.story("Admin User Creating A New User")
@allure.title("Create New User")
@allure.severity(allure.severity_level.BLOCKER)

def test_create_new_user(driver):
    login_page = LoginPage(driver)
    user_management_page = UserManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    success, error = user_management_page.create_user(**DataLoader.load_user("default"))
    assert success, (
        f"Create food failed. Server message: {error}"
        if error
        else "Create food should be successful but it was not."
    )

@pytest.mark.dependency(
    depends=["create_group"]
)
@pytest.mark.blocker
@allure.epic("Definitions")
@allure.feature("Create User")
@allure.story("Admin User Creating A Duplicate User")
@allure.title("Create Duplicate User")
@allure.severity(allure.severity_level.BLOCKER)

def test_create_duplicate_user(driver):
    login_page = LoginPage(driver)
    user_management_page = UserManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    success, error = user_management_page.create_user(
        **DataLoader.load_user("duplicate")
    )

    assert not success
    assert error == 'بارکد کارت تکراری است.'
