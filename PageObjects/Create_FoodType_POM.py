from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import SideMenu
from Components.Base_page import BasePage

class FoodTypeManagementPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.new_button_locator=((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
        self.name_field_locator = ((By.ID,"FoodTypeName"))
        self.submit_button_locator = ((By.XPATH,"//button[contains(text(),'ثبت')]"))
        self.error_message_locator = (By.CSS_SELECTOR,"#toast-container .toast-message div")


    def is_foodtype_created(self, name):
        locator = (
            By.XPATH,
            f"(//td[contains(text(),'{name}')])[1]"
        )
        return self.is_visible(locator)


    def open_new_foodtype_form(self):
        side_menu = SideMenu(self.driver)
        side_menu.navigate_to_foodtype_page()
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



    def create_foodtype(self,name):
        self.open_new_foodtype_form()
        self.enter_name(name)
        self.submit_form()

        if error := self.get_error_message(self.error_message_locator, timeout=2):
            return False, error
        return self.is_foodtype_created(name), None