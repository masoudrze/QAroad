from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class UserIndexNav:
    def __init__(self,driver):
        self.driver = driver
        self.user_menu_dropdown_locator = ((By.CSS_SELECTOR,"li.user-menu a.dropdown-toggle"))
        self.logout_button_locator = ((By.XPATH, "(//a[contains(text(),'خروج')])[1]"))

    def open_user_menu_dropdown(self):
        self.driver.find_element(*self.user_menu_dropdown_locator).click()


    def user_logout(self):
        wait = WebDriverWait(self.driver, 5)
        self.open_user_menu_dropdown()
        wait.until(
        EC.element_to_be_clickable(self.logout_button_locator)
        ).click()



    def is_logged_out(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,"(//a[contains(text(),'اینجا')])[1]"))
        ).is_displayed()



    

        