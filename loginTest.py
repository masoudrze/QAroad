from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def setup_method(self):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def test_login_fail(self):
        driver=self.driver
        driver.get("http://localhost/")

        input_element_username = driver.find_element(By.ID,"username")
        input_element_password = driver.find_element(By.ID,"password")
        input_element_username.send_keys("supervisor")
        input_element_password.send_keys("111")

        wait = WebDriverWait(driver, 5)

        login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="ورود"]'))
        )
        login_button.click()
        wait = WebDriverWait(driver, 5)

        actual_text = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".login-alert.ng-binding")
        )
        ).text
        expected_text = "نام کاربری و یا کلمه عبور اشتباه است."

        assert expected_text in actual_text,"login should be failed but it is not"



    def test_login_successful(self):
        driver=self.driver
        driver.get("http://localhost/")
        input_element_username = driver.find_element(By.ID,"username")
        input_element_password = driver.find_element(By.ID,"password")
        input_element_username.send_keys("supervisor")
        input_element_password.send_keys("1")

        wait = WebDriverWait(driver, 5)

        login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="ورود"]'))
        )

        login_button.click()

        main_menu = wait.until(
        EC.visibility_of_element_located((By.ID, "main-menu"))
    )
        assert main_menu.is_displayed(),"login should be successful but it is not"



    def teardown_method(self):
        self.driver.quit()



