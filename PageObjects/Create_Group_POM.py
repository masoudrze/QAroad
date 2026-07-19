from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import MainMenu

class CreateGroupPage:
    def __init__(self,driver):
        self.driver = driver
        self.new_group_button=((By.XPATH, "//a[@title='گروه جدید']"))
        self.group_name_field = ((By.ID,"Groupname"))
        self.group_MinIncreaseCredit_field = ((By.ID,"MinIncreaseCredit"))
        self.group_MaxIncreaseCredit_field = ((By.ID,"MaxIncreaseCredit"))
        self.group_submit_button = ((By.XPATH,"(//button[contains(text(),'ثبت')])[1]"))



    def new_group(self):
        Side_Menu = MainMenu(self.driver)
        Side_Menu.create_group_menu()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[@title='گروه جدید']"))
        )

        self.driver.find_element(*self.new_group_button).click()
        wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='Groupname']"))
        )


    def enter_group_name(self,group_name):
        self.driver.find_element(*self.group_name_field).send_keys(group_name)

    def enter_group_MinIncreaseCredit(self,MinIncreaseCredit):
        self.driver.find_element(*self.group_MinIncreaseCredit_field).send_keys(MinIncreaseCredit)

    def enter_group_MaxIncreaseCredit(self,MaxIncreaseCredit):
        self.driver.find_element(*self.group_MaxIncreaseCredit_field).send_keys(MaxIncreaseCredit)
    
    def click_create(self):
        self.driver.find_element(*self.submit_button).click()



    def create_new_group(self,group_name,MinIncreaseCredit,MaxIncreaseCredit):
        self.enter_group_name(group_name)
        self.enter_group_MinIncreaseCredit(MinIncreaseCredit)
        self.enter_group_MaxIncreaseCredit(MaxIncreaseCredit)
        self.click_create()
        