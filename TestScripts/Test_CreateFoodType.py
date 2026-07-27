from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_FoodType_POM import FoodTypeManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_foodtype(setup):
    driver=setup
    login_page = LoginPage(driver)
    side_menu = SideMenu(driver)
    foodtype_management_page = FoodTypeManagementPage(driver)

    llogin_page.login(**DataLoader.load_login("admin_pass"))
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    side_menu.navigate_to_foodtype_page()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
    )
    foodtype_management_page.open_new_foodtype_form()
    foodtype_management_page.create_foodtype("نوشیدنی")
    new_created_foodtype=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'نوشیدنی')])[1]"))
    )
    
    assert new_created_foodtype.is_displayed(),"Create foodtype should be successful but it is not"
