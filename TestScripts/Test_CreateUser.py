from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_User_POM import UserManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_user(driver):
    login_page = LoginPage(driver)
    user_management_page = UserManagementPage(driver)
    user_data = DataLoader.load_user("default")

    login_page.login(**DataLoader.load_login("admin_pass"))
    
    user_management_page.create_user(**DataLoader.load_user("default"))
    
    assert user_management_page.is_user_created(user_data["name"]),"Create group should be successful but it is not"

   
