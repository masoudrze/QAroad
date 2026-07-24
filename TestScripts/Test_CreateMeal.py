from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import MainMenu
from PageObjects.Create_Meal_POM import CreateMealPage
import time


def test_create_new_meal(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Main_menu = MainMenu(driver)
    Create_meal = CreateMealPage(driver)

    Login_page.login("supervisor","1")
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    Main_menu.create_meal_menu()
    time.sleep(5)
    wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
    )
    Create_meal.new_meal()
    Create_meal.create_new_meal("عصرونه")
    New_created_meal=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'عصرونه')])[1]"))
    )
    
    assert New_created_meal.is_displayed(),"Create meal should be successful but it is not"
