from PageObjects.LoginPage_POM import LoginPage
from PageObjects.Create_Group_POM import GroupManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_group(driver):
    login_page = LoginPage(driver)
    group_management_page = GroupManagementPage(driver)
    group_data = DataLoader.load_group("default")
    login_page.login(**DataLoader.load_login("admin_pass"))
    group_management_page.create_group(**DataLoader.load_group("default"))

    assert group_management_page.is_group_created(group_data["name"]),"Create group should be successful but it is not"
