from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import MainMenu

class CreateMealPage:
    def __init__(self,driver):
        self.driver = driver
        self.new_meal_button=((By.XPATH, "(//a[contains(text(),'جدید')])[1]"))
        self.meal_name_field = ((By.ID,"txtMealName"))
        self.meal_submit_button = ((By.XPATH,"//button[contains(text(),'ثبت')]"))



    def new_meal(self):
        Side_Menu = MainMenu(self.driver)
        Side_Menu.create_meal_menu()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.visibility_of_element_located(self.new_meal_button)
        )

        self.driver.find_element(*self.new_meal_button).click()
        wait.until(
        EC.visibility_of_element_located(self.meal_submit_button)
        )


    def enter_meal_name(self,meal_name):
        self.driver.find_element(*self.meal_name_field).send_keys(meal_name)
    
    def click_create(self):
        self.driver.find_element(*self.meal_submit_button).click()



    def create_new_meal(self,meal_name):
        self.enter_meal_name(meal_name)
        self.click_create()
        