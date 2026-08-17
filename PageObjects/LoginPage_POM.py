from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field_locator = (By.ID, "username")
        self.password_field_locator = (By.ID, "password")
        self.submit_button_locator = (By.XPATH, '//button[text()="ورود"]')

    def enter_username(self, username):
        self.driver.find_element(*self.username_field_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field_locator).send_keys(password)

    def submit_form(self):
        self.driver.find_element(*self.submit_button_locator).click()

    def is_admin_dashboard_displayed(self):
        return (
            WebDriverWait(self.driver, 5)
            .until(EC.visibility_of_element_located((By.ID, "main-menu")))
            .is_displayed()
        )

    def is_user_dashboard_displayed(self):
        return (
            WebDriverWait(self.driver, 5)
            .until(EC.visibility_of_element_located((By.ID, "user-section")))
            .is_displayed()
        )

    def login_failed_message(self):
        return (
            WebDriverWait(self.driver, 5)
            .until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".login-alert.ng-binding")
                )
            )
            .text
        )

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.submit_form()
