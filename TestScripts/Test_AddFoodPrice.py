from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_FoodPrice_POM import FoodPriceManagementPage
from Helpers.data_loader import DataLoader
import time


def test_add_new_foodprice(setup):
    driver=setup
    login_page = LoginPage(driver)
    side_menu = SideMenu(driver)
    food_price_management_page = FoodPriceManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    side_menu.navigate_to_foodprice_page()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
    )
    food_price_management_page.open_new_foodprice_form("دانشجویان")

    time.sleep(4)
    
    food_price_management_page.create_new_foodprice("نوشابه","250000","50000","250000","250000","مکمل")
    new_created_food=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'نوشابه')])[1]"))
    )

    assert new_created_food.is_displayed(),"Create food should be successful but it is not"
    
