from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import SideMenu
from PageObjects.Create_Group_POM import GroupManagementPage


def test_create_new_group(setup):
    driver=setup
    login_page = LoginPage(driver)
    side_menu = SideMenu(driver)
    group_management_page = GroupManagementPage(driver)

    login_page.login("supervisor","1")
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    side_menu.navigate_to_group_page()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, '//a[normalize-space()="جدید"]'))
    )
    group_management_page.open_new_group_form()
    group_management_page.create_group("اساتید","10000","100000")
    new_created_group=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'اساتید')])[1]"))
    )
    
    assert new_created_group.is_displayed(),"Create group should be successful but it is not"
