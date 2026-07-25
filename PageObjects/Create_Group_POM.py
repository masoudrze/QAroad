from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import SideMenu

class GroupManagementPage:
    def __init__(self,driver):
        self.driver = driver
        self.new_button_locator=((By.XPATH, "//a[@title='گروه جدید']"))
        self.name_field_locator = ((By.ID,"Groupname"))
        self.MinIncreaseCredit_field_locator = ((By.ID,"MinIncreaseCredit"))
        self.MaxIncreaseCredit_field_locator = ((By.ID,"MaxIncreaseCredit"))
        self.submit_button_locator = ((By.XPATH,"(//button[contains(text(),'ثبت')])[1]"))



    def open_new_group_form(self):
        side_menu = SideMenu(self.driver)
        side_menu.navigate_to_group_page()
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

    def enter_MinIncreaseCredit(self,MinIncreaseCredit):
        self.driver.find_element(*self.MinIncreaseCredit_field_locator).send_keys(MinIncreaseCredit)

    def enter_MaxIncreaseCredit(self,MaxIncreaseCredit):
        self.driver.find_element(*self.MaxIncreaseCredit_field_locator).send_keys(MaxIncreaseCredit)
    
    def submit_form(self):
        self.driver.find_element(*self.submit_button_locator).click()



    def create_group(self,name,MinIncreaseCredit,MaxIncreaseCredit):
        self.enter_name(name)
        self.enter_MinIncreaseCredit(MinIncreaseCredit)
        self.enter_MaxIncreaseCredit(MaxIncreaseCredit)
        self.submit_form()
        