from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import MainMenu

class CreateUserPage:
    def __init__(self,driver):
        self.driver = driver
        self.new_user_button=((By.XPATH, "//a[@title='فرد جدید']"))
        self.user_firstname_field = ((By.ID,"FirstName"))
        self.user_lastname_field = ((By.ID,"LastName"))
        self.user_meli_field = ((By.ID,"Meli"))
        self.user_girl_field = ((By.ID,"FirstName"))
        self.user_barcode_field = ((By.ID,"stid"))
        self.user_cardnumber_field = ((By.ID,"CardNumber"))
        self.user_expiredate_field = ((By.ID,"ExpireDate"))
        self.user_username_field = ((By.ID,"txtusername1"))
        self.user_password_field = ((By.ID,"txtpassword1"))
        self.user_repassword_field = ((By.ID,"RePassword"))
        self.user_role_field = ((By.ID,"Roles"))
        self.user_passwordfaramooshi_field = ((By.ID,"PasswordFaramooshi"))
        self.user_personelli_field = ((By.ID,"Personneli"))
        self.active_fromdate_field = ((By.ID,"txtFromDate"))
        self.active_todate_field = ((By.ID,"txtToDate"))
        

        #select_element = driver.find_element(By.NAME, 'selectomatic')
        #select = Select(select_element)
        #select.select_by_visible_text('Four')

        self.submit_button = ((By.XPATH,"(//button[contains(text(),'ثبت')])[1]"))



    def new_group(self):
        Side_Menu = MainMenu(self.driver)
        Side_Menu.create_user_menu()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[@title='فرد جدید']"))
        )

        self.driver.find_element(*self.new_user_button).click()
        wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='Groupname']"))
        )


    def enter_group_name(self,group_name):
        self.driver.find_element(*self.group_name_field).send_keys(group_name)

    def enter_group_MinIncreaseCredit(self,MinIncreaseCredit):
        self.driver.find_element(*self.MinIncreaseCredit_field).send_keys(MinIncreaseCredit)

    def enter_group_MaxIncreaseCredit(self,MaxIncreaseCredit):
        self.driver.find_element(*self.MaxIncreaseCredit_field).send_keys(MaxIncreaseCredit)
    
    def click_create(self):
        self.driver.find_element(*self.submit_button).click()



    def create_new_group(self,group_name,MinIncreaseCredit,MaxIncreaseCredit):
        self.enter_group_name(group_name)
        self.enter_group_MinIncreaseCredit(MinIncreaseCredit)
        self.enter_group_MaxIncreaseCredit(MaxIncreaseCredit)
        self.click_create()
        