from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import MainMenu
from PageObjects.Create_Group_POM import CreateGroupPage


def test_create_new_group(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Main_menu = MainMenu(driver)
    Create_group = CreateGroupPage(driver)

    Login_page.login("supervisor","1")
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    Main_menu.create_group_menu()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, '//a[normalize-space()="جدید"]'))
    )
    Create_group.new_group()
    Create_group.create_new_group("sel test","10000","100000")
    New_created_group=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[contains(text(),'دانشجویان')])[1]"))
    )
    
    assert New_created_group.is_displayed(),"Create group should be successful but it is not"
