import pytest

from Helpers.data_loader import DataLoader
from PageObjects.Create_Self_POM import SelfManagementPage
from PageObjects.LoginPage_POM import LoginPage


@pytest.mark.smoke
def test_create_new_self(driver):
    login_page = LoginPage(driver)
    self_management_page = SelfManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = self_management_page.create_self(**DataLoader.load_self("default"))

    assert success, (
        f"Create self failed. Server message: {error}"
        if error
        else "Create self should be successful but it was not."
    )


@pytest.mark.negative
def test_create_duplicate_self(driver):
    login_page = LoginPage(driver)
    self_management_page = SelfManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = self_management_page.create_self(**DataLoader.load_self("default"))

    assert not success
    assert error == 'نام وارد شده تکراری می باشد'
