from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_FoodType_POM import FoodTypeManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_foodtype(driver):
    login_page = LoginPage(driver)
    side_menu = SideMenu(driver)
    foodtype_management_page = FoodTypeManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))


    success, error = foodtype_management_page.create_foodtype(**DataLoader.load_foodtype("default"))

    assert success, (
        f"Create food failed. Server message: {error}"
        if error
        else "Create food should be successful but it was not."
    )
