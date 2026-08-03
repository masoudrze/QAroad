from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_Self_POM import SelfManagementPage
from Helpers.data_loader import DataLoader


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
