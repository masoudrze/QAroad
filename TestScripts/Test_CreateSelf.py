from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_Self_POM import SelfManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_self(setup):
    driver=setup
    login_page = LoginPage(driver)
    side_menu = SideMenu(driver)
    self_management_page = SelfManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    side_menu.navigate_to_self_page()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
    )
    self_management_page.open_new_self_form()
    self_management_page.create_self("سالن","0")
    new_created_self=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'سالن')])[1]"))
    )
    
    assert new_created_self.is_displayed(),"Create self should be successful but it is not"
