from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import SideMenu

class FoodManagementPage:
    def __init__(self,driver):
        self.driver = driver
        self.new_button_locator=((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
        self.name_field_locator = ((By.ID,"Foodname"))
        self.submit_button_locator = ((By.XPATH,"//button[contains(text(),'ثبت')]"))



    def open_new_food_form(self):
        side_menu = SideMenu(self.driver)
        side_menu.navigate_to_food_page()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.visibility_of_element_located(self.new_button_locator)
        )

        self.driver.find_element(*self.new_button_locator).click()
        wait.until(
        EC.visibility_of_element_located(self.submit_button_locator)
        )


    def enter_name(self,name):
        self.driver.find_element(*self.name_field_locator).send_keys(name)
    
    def submit_form(self):
        self.driver.find_element(*self.submit_button_locator).click()



    def create_new_food(self,name):
        self.enter_name(name)
        self.submit_form()
        