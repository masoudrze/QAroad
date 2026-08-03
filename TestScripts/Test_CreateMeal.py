from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_Meal_POM import MealManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_meal(driver):
    login_page = LoginPage(driver)
    meal_management_page = MealManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = meal_management_page.create_meal(**DataLoader.load_meal("default"))

    assert success, (
        f"Create meal failed. Server message: {error}"
        if error
        else "Create meal should be successful but it was not."
    )