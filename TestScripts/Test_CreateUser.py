from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from Components.Main_Menu import MainMenu
from PageObjects.Create_User_POM import CreateUserPage


def test_create_new_user(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Main_menu = MainMenu(driver)
    Create_user = CreateUserPage(driver)

    Login_page.login("supervisor","1")
    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    Main_menu.create_user_menu()
    wait.until(
    EC.visibility_of_element_located((By.XPATH, '//a[normalize-space()="جدید"]'))
    )
    Create_user.new_user()
    Create_user.create_new_user("عماد","عمادی","1111111141","مرد","32","32","1408/04/01","user32","Aa@12345","Aa@12345","کاربر","1","32","1404/04/01","1408/04/01")
    New_created_group=wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//td[@class='ng-binding'][normalize-space()='Supervisor'])[1]"))
    )
    
    assert New_created_group.is_displayed(),"Create user should be successful but it is not"
