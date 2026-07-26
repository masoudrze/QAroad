from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_Meal_POM import MealManagementPage

from Helpers.data_loader import DataLoader


def test_create_new_meal(setup):
    driver=setup
    login_page = LoginPage(driver)
    side_menu = SideMenu(driver)
    meal_management_page = MealManagementPage(driver)

    login_page.login("supervisor","1")
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    side_menu.navigate_to_meal_page()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
    )
    meal_management_page.open_new_meal_form()
    #meal_management_page.create_meal("وعده تست")

    meal = DataLoader.load_meal("default")

    meal_management_page.create_meal(meal["name"])

    new_created_meal=wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, f"(//td[contains(text(),'{meal['name']}')])[1]")
        #(By.XPATH, "(//td[contains(text(),'وعده تست')])[1]")
        )
    )
    
    assert new_created_meal.is_displayed(),"Create meal should be successful but it is not"
