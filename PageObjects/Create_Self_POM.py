from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import SideMenu

class SelfManagementPage:
    def __init__(self,driver):
        self.driver = driver
        self.add_new_button_locator=((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
        self.name_field_locator = ((By.ID,"Selfname"))
        self.capacity_field_locator = ((By.ID,"Capacity"))
        self.submit_button_locator = ((By.XPATH,"//button[contains(text(),'ثبت')]"))



    def open_new_self_form(self):
        side_menu = SideMenu(self.driver)
        side_menu.navigate_to_self_page()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.visibility_of_element_located(self.add_new_button_locator)
        )

        self.driver.find_element(*self.add_new_button_locator).click()
        wait.until(
        EC.visibility_of_element_located(self.submit_button_locator)
        )


    def enter_name(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_capacity(self,capacity):
        self.driver.find_element(*self.capacity_field).send_keys(capacity)
    
    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()



    def create_self(self,name,capacity):
        self.enter_name(name)
        self.enter_capacity(capacity)
        self.submit_form()
        