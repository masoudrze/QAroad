from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_User_POM import UserManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_user(setup):
    driver=setup
    login_page = LoginPage(driver)
    side_menu = SideMenu(driver)
    user_management_page = UserManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    side_menu.navigate_to_users_page()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, '//a[normalize-space()="جدید"]'))
    )
    
    user_management_page.open_new_user_form()
    
    user_management_page.create_user("کیان","کیانی","1111111142","مرد","33","33","1408/04/01","user33","Aa@12345","Aa@12345","کاربر","123","33","دانشجویان","1404/04/01","1408/04/01")
    
    
    
    new_created_user=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[@class='ng-binding'][normalize-space()='Supervisor'])[1]"))
    )
    
    assert new_created_user.is_displayed(),"Create user should be successful but it is not"

   
