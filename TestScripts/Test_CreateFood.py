from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_Food_POM import FoodManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_food(setup):
    driver=setup
    login_page = LoginPage(driver)
    side_menu = SideMenu(driver)
    food_management_page = FoodManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    side_menu.navigate_to_food_page()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
    )
    food_management_page.open_new_food_form()
    food_management_page.create_food("نوشابه","نوشیدنی")
    new_created_food=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'نوشابه')])[1]"))
    )
    
    assert new_created_food.is_displayed(),"Create food should be successful but it is not"
