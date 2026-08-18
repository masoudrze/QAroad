import pytest

from Helpers.data_loader import DataLoader
from PageObjects.Create_User_POM import UserManagementPage
from PageObjects.LoginPage_POM import LoginPage


@pytest.mark.smoke
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


@pytest.mark.negative
def test_create_duplicate_user(driver):
    login_page = LoginPage(driver)
    user_management_page = UserManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    success, error = user_management_page.create_user(
        **DataLoader.load_user("duplicate")
    )

    assert not success
    assert error == 'بارکد کارت تکراری است.'
