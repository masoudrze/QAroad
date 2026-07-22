from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import MainMenu
from selenium.webdriver.support.select import Select
import time

class CreateUserPage:
    def __init__(self,driver):
        self.driver = driver
        self.new_user_button=((By.XPATH, "//a[contains(text(),'جدید')]"))

        self.user_firstname_field = ((By.ID,"FirstName"))
        self.user_lastname_field = ((By.ID,"LastName"))
        self.user_meli_field = ((By.ID,"Meli"))
        self.user_sex_field = ((By.ID, 'Girl'))
        self.user_barcode_field = ((By.ID,"stid"))
        self.user_cardnumber_field = ((By.ID,"CardNumber"))
        self.user_expiredate_field = ((By.ID,"ExpireDate"))
        self.user_username_field = ((By.ID,"txtusername1"))
        self.user_password_field = ((By.ID,"txtpassword1"))
        self.user_repassword_field = ((By.ID,"RePassword"))
        self.user_role_field = ((By.ID,"Roles"))
        self.user_passwordfaramooshi_field = ((By.ID,"PasswordFaramooshi"))
        self.user_personelli_field = ((By.ID,"Personneli"))
        self.user_group_field = ((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[3]/div[5]/div[1]/div[2]/div[3]/div[1]/span[1]/span[1]/span[1]"))
        self.active_fromdate_field = ((By.ID,"txtFromDate"))
        self.active_todate_field = ((By.ID,"txtToDate"))

        self.submit_button = ((By.XPATH,"//button[@title='توجه']"))


        #//////////////////////////////////////////////
    # Open the dropdown

        #/////////////////////////////////////////////



    def new_user(self):
        Side_Menu = MainMenu(self.driver)
        Side_Menu.create_user_menu()
        wait = WebDriverWait(self.driver, 5)
        time.sleep(2)
        wait.until(
        EC.element_to_be_clickable(self.new_user_button)
        ).click()

        wait.until(
        EC.visibility_of_element_located((By.ID,"FirstName"))
        )


    def enter_user_firstname(self,firstname):
        self.driver.find_element(*self.user_firstname_field).send_keys(firstname)

    def enter_user_lastname(self,lastname):
        self.driver.find_element(*self.user_lastname_field).send_keys(lastname)

    def enter_user_meli(self,meli):
        self.driver.find_element(*self.user_meli_field).send_keys(meli)
    
    def enter_user_sex(self,sex):
        self.driver.find_element(*self.user_sex_field)
        select = Select(self.driver.find_element(*self.user_sex_field))
        select.select_by_visible_text(sex)

    def enter_user_barcode(self,barcode):
        self.driver.find_element(*self.user_barcode_field).send_keys(barcode)
    
    def enter_user_cardnumber(self,cardnumber):
        self.driver.find_element(*self.user_cardnumber_field).send_keys(cardnumber)

    def enter_user_expiredate(self,expiredate):
        self.driver.find_element(*self.user_expiredate_field).send_keys(expiredate)
    
    def enter_user_username(self,username):
        self.driver.find_element(*self.user_username_field).send_keys(username)
    
    def enter_user_password(self,password):
        self.driver.find_element(*self.user_password_field).send_keys(password)

    def enter_user_repassword(self,repassword):
        self.driver.find_element(*self.user_repassword_field).send_keys(repassword)

    def enter_user_role(self,role):
        select_element = self.driver.find_element(*self.user_role_field)
        select = Select(select_element)
        select.select_by_visible_text(role)

    def enter_user_passwordfaramooshi(self,passwordfaramooshi):
        self.driver.find_element(*self.user_passwordfaramooshi_field).send_keys(passwordfaramooshi)

    def enter_user_personelli(self,personelli):
        self.driver.find_element(*self.user_personelli_field).send_keys(personelli)

    def enter_user_group(self,group):
        print(self.driver.find_elements(*self.user_group_field))
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.element_to_be_clickable(self.user_group_field)
            ).click()
        
        wait.until(
        EC.element_to_be_clickable(
        (By.XPATH, f"//li[normalize-space()='{group}']")
        )
            ).click()

    def enter_user_active_fromdate(self,active_fromdate):
        self.driver.find_element(*self.active_fromdate_field).send_keys(active_fromdate)

    def enter_user_active_todate(self,active_todate):
        self.driver.find_element(*self.active_todate_field).send_keys(active_todate)

    
    
    def click_create(self):
        self.driver.find_element(*self.submit_button).click()



    def create_new_user(self,firstname,lastname,meli,sex,barcode,cardnumber,expiredate,username,password,repassword,role,passwordfaramooshi,personelli,group,active_fromdate,active_todate):
        self.enter_user_firstname(firstname)
        self.enter_user_lastname(lastname)
        self.enter_user_meli(meli)
        self.enter_user_sex(sex)
        self.enter_user_barcode(barcode)
        self.enter_user_cardnumber(cardnumber)
        self.enter_user_expiredate(expiredate)
        self.enter_user_username(username)
        self.enter_user_password(password)
        self.enter_user_repassword(repassword)
        self.enter_user_role(role)
        self.enter_user_passwordfaramooshi(passwordfaramooshi)
        self.enter_user_personelli(personelli)
        self.enter_user_group(group)
        self.enter_user_active_fromdate(active_fromdate)
        self.enter_user_active_todate(active_todate)
        self.click_create()
        