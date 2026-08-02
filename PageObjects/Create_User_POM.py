from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import SideMenu
from Components.Base_page import BasePage
from selenium.webdriver.support.select import Select


class UserManagementPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.new_button_locator=((By.XPATH, "//a[contains(text(),'جدید')]"))
        self.firstname_field_locator = ((By.ID,"FirstName"))
        self.lastname_field_locator = ((By.ID,"LastName"))
        self.meli_field_locator = ((By.ID,"Meli"))
        self.sex_field_locator = ((By.ID, 'Girl'))
        self.barcode_field_locator = ((By.ID,"stid"))
        self.cardnumber_field_locator = ((By.ID,"CardNumber"))
        self.expiredate_field_locator = ((By.ID,"ExpireDate"))
        self.username_field_locator = ((By.ID,"txtusername1"))
        self.password_field_locator = ((By.ID,"txtpassword1"))
        self.repassword_field_locator = ((By.ID,"RePassword"))
        self.role_field_locator = ((By.ID,"Roles"))
        self.passwordfaramooshi_field_locator = ((By.ID,"PasswordFaramooshi"))
        self.personelli_field_locator = ((By.ID,"Personneli"))
        self.group_field_locator = ((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[3]/div[5]/div[1]/div[2]/div[3]/div[1]/span[1]/span[1]/span[1]"))
        self.active_fromdate_field_locator = ((By.ID,"txtFromDate"))
        self.active_todate_field_locator = ((By.ID,"txtToDate"))
        self.submit_button_locator = ((By.XPATH,"//button[@title='توجه']"))
        
        self.error_message_locator = (By.CSS_SELECTOR,"#toast-container .toast-message div")


    def is_user_created(self, name):
        locator = (
            By.XPATH,
            f"(//td[@class='ng-binding'][normalize-space()='{name}'])[1]"
        )
        return self.is_visible(locator)


    def open_new_user_form(self):
        side_menu = SideMenu(self.driver)
        side_menu.navigate_to_users_page()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.element_to_be_clickable(self.new_button_locator)
        ).click()

        wait.until(
        EC.visibility_of_element_located(self.submit_button_locator)
        )


    def enter_firstname(self,firstname):
        self.driver.find_element(*self.firstname_field_locator).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(*self.lastname_field_locator).send_keys(lastname)

    def enter_meli(self,meli):
        self.driver.find_element(*self.meli_field_locator).send_keys(meli)
    
    def enter_sex(self,sex):
        self.driver.find_element(*self.sex_field_locator)
        select = Select(self.driver.find_element(*self.sex_field_locator))
        select.select_by_visible_text(sex)

    def enter_barcode(self,barcode):
        self.driver.find_element(*self.barcode_field_locator).send_keys(barcode)
    
    def enter_cardnumber(self,cardnumber):
        self.driver.find_element(*self.cardnumber_field_locator).send_keys(cardnumber)

    def enter_expiredate(self,expiredate):
        self.driver.find_element(*self.expiredate_field_locator).send_keys(expiredate)
    
    def enter_username(self,username):
        self.driver.find_element(*self.username_field_locator).send_keys(username)
    
    def enter_password(self,password):
        self.driver.find_element(*self.password_field_locator).send_keys(password)

    def enter_repassword(self,repassword):
        self.driver.find_element(*self.repassword_field_locator).send_keys(repassword)

    def enter_role(self,role):
        select_element = self.driver.find_element(*self.role_field_locator)
        select = Select(select_element)
        select.select_by_visible_text(role)

    def enter_passwordfaramooshi(self,passwordfaramooshi):
        self.driver.find_element(*self.passwordfaramooshi_field_locator).send_keys(passwordfaramooshi)

    def enter_personelli(self,personelli):
        self.driver.find_element(*self.personelli_field_locator).send_keys(personelli)

    def enter_group(self,group):
        print(self.driver.find_elements(*self.group_field_locator))
        wait = WebDriverWait(self.driver, 100)
        wait.until(
        EC.element_to_be_clickable(self.group_field_locator)
            ).click()
        
        wait.until(
        EC.element_to_be_clickable(
        (By.XPATH, f"//li[normalize-space()='{group}']")
        )
            ).click()

    def enter_active_fromdate(self,active_fromdate):
        self.driver.find_element(*self.active_fromdate_field_locator).send_keys(active_fromdate)

    def enter_active_todate(self,active_todate):
        self.driver.find_element(*self.active_todate_field_locator).send_keys(active_todate)

    
    
    def submit_form(self):
        self.driver.find_element(*self.submit_button_locator).click()



    def create_user(self,firstname,lastname,meli,sex,barcode,cardnumber,expiredate,username,password,repassword,role,passwordfaramooshi,personelli,group,active_fromdate,active_todate):
        self.open_new_user_form()
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_meli(meli)
        self.enter_sex(sex)
        self.enter_barcode(barcode)
        self.enter_cardnumber(cardnumber)
        self.enter_expiredate(expiredate)
        self.enter_username(username)
        self.enter_password(password)
        self.enter_repassword(repassword)
        self.enter_role(role)
        self.enter_passwordfaramooshi(passwordfaramooshi)
        self.enter_personelli(personelli)
        self.enter_group(group)
        self.enter_active_fromdate(active_fromdate)
        self.enter_active_todate(active_todate)
        self.submit_form()

        if error := self.get_error_message(self.error_message_locator, timeout=2):
            return False, error
        return self.is_user_created(personelli), None

        