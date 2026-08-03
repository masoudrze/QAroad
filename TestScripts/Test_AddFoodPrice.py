from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_FoodPrice_POM import FoodPriceManagementPage
from Helpers.data_loader import DataLoader
import time


def test_add_new_foodprice(driver):
    login_page = LoginPage(driver)
    food_price_management_page = FoodPriceManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = food_price_management_page.create_new_foodprice(**DataLoader.load_foodprice("default"))

    assert success, (
        f"Adding food price failed. Server message: {error}"
        if error
        else "Adding food price should be successful but it was not."
    )
    
