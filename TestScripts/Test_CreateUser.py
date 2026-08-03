from PageObjects.LoginPage_POM import LoginPage
from PageObjects.Create_User_POM import UserManagementPage
from Helpers.data_loader import DataLoader


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

   
