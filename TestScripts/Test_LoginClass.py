from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage_POM import LoginPage
from PageObjects.UserIndex_Nav_POM import UserIndexNav



def test_invalid_admin_login(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("supervisor","1111")

    wait = WebDriverWait(driver, 5)
    actual_text = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".login-alert.ng-binding")
    )
    ).text
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."

    assert expected_text in actual_text,"login should be failed but it is not"


def test_invalid_user_login(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("user2","1111")

    wait = WebDriverWait(driver, 5)
    actual_text = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".login-alert.ng-binding")
    )
    ).text
    expected_text = "نام کاربری و یا کلمه عبور اشتباه است."

    assert expected_text in actual_text,"login should be failed but it is not"


def test_valid_admin_login(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("supervisor","1")

    wait = WebDriverWait(driver, 5)
    main_menu = wait.until(
    EC.visibility_of_element_located((By.ID, "main-menu"))
    )
    assert main_menu.is_displayed(),"login should be successful but it is not"





def test_valid_user_login(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("user2","1")

    wait = WebDriverWait(driver, 5)
    main_menu = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[@class='user-panel']"))
    )
    assert main_menu.is_displayed(),"login should be successful but it is not"



def test_valid_admin_login_logout(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("supervisor","1")
    Logout=UserIndexNav(driver)
    

    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="content-left"]/nav/div/ul/li[9]/a'))
    )
    Logout.Logout()

    LoggedOut_message = wait.until(
    EC.visibility_of_element_located((By.XPATH,"(//a[contains(text(),'اینجا')])[1]"))
    )

    assert LoggedOut_message.is_displayed(),"logout should be successful but it is not"



def test_valid_user_login_logout(setup):
    driver=setup
    Login_page = LoginPage(driver)
    Login_page.login("user2","1")
    Logout=UserIndexNav(driver)
    

    wait = WebDriverWait(driver, 5)
    wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,"li.user-menu a.dropdown-toggle"))
    )
    Logout.Logout()

    LoggedOut_message = wait.until(
    EC.visibility_of_element_located((By.XPATH,"(//a[contains(text(),'اینجا')])[1]"))
    )

    assert LoggedOut_message.is_displayed(),"logout should be successful but it is not"



