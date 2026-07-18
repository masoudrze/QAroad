from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class UserIndexNav:
    def __init__(self,driver):
        self.driver = driver
        self.user_menu_dropdown = ((By.CSS_SELECTOR,"li.user-menu a.dropdown-toggle"))
        self.logout_button = ((By.XPATH, "(//a[contains(text(),'خروج')])[1]"))

    def click_user_menu_dropdown(self):
        self.driver.find_element(*self.user_menu_dropdown).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()


    def Logout(self):
        wait = WebDriverWait(self.driver, 5)
        self.click_user_menu_dropdown()
        wait.until(
        EC.visibility_of_element_located((By.XPATH,"(//a[contains(text(),'خروج')])[1]"))
        )
        self.click_logout()



    

        