from PageObjects.LoginPage_POM import LoginPage
from PageObjects.Create_Group_POM import GroupManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_group(driver):
    login_page = LoginPage(driver)
    group_management_page = GroupManagementPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = group_management_page.create_group(**DataLoader.load_group("default"))
    assert success, (
        f"Create food failed. Server message: {error}"
        if error
        else "Create food should be successful but it was not."
    )


def test_create_duplicate_group(driver):
    login_page = LoginPage(driver)
    group_management_page = GroupManagementPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = group_management_page.create_group(**DataLoader.load_group("duplicate"))


    assert not success
    assert error == 'گروه با این نام وجود دارد.'
