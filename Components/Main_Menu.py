from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SideMenu:
    def __init__(self,driver):
        self.driver = driver
        self.Definitions=(((By.XPATH, '//a[span[normalize-space()="تعاریف"]]')))
        self.Definitions_base_info=(((By.XPATH, '//a[span[normalize-space()="اطلاعات پایه"]]')))
        self.Definitions_base_info_group=(((By.XPATH, '//a[normalize-space()="گروه"]')))
        self.Definitions_base_info_users=(((By.XPATH, '//a[normalize-space()="افراد"]')))

        self.Definitions_feeding=(((By.XPATH, '//a[span[normalize-space()="تغذیه"]]')))
        self.Definitions_feeding_meal=(((By.XPATH, '//a[normalize-space()="وعده"]')))
        self.Definitions_feeding_self=(((By.XPATH, '//a[normalize-space()="سلف"]')))
        self.Definitions_feeding_foodtype=(((By.XPATH, '//a[normalize-space()="نوع غذا"]')))
        self.Definitions_feeding_food=(((By.XPATH, '//a[normalize-space()="غذا"]')))
        self.Definitions_feeding_foodprice=(((By.XPATH, '//a[normalize-space()="قیمت غذا"]')))
        

    

    def navigate_to_group_page(self):
        wait = WebDriverWait(self.driver, 5)

        wait.until(
            EC.element_to_be_clickable(self.Definitions)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.Definitions_base_info)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.Definitions_base_info_group)
        ).click()





    def navigate_to_users_page(self):
        wait = WebDriverWait(self.driver, 5)

        wait.until(
            EC.element_to_be_clickable(self.Definitions)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.Definitions_base_info)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.Definitions_base_info_users)
        ).click()


    def navigate_to_meal_page(self):
        wait = WebDriverWait(self.driver, 5)
    
        wait.until(
            EC.element_to_be_clickable(self.Definitions)
        ).click()
    
        wait.until(
            EC.element_to_be_clickable(self.Definitions_feeding)
        ).click()
    
        wait.until(
            EC.element_to_be_clickable(self.Definitions_feeding_meal)
        ).click()


    def navigate_to_self_page(self):
            wait = WebDriverWait(self.driver, 5)
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_self)
            ).click()

    def navigate_to_foodtype_page(self):
            wait = WebDriverWait(self.driver, 5)
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_foodtype)
            ).click()

    def navigate_to_food_page(self):
            wait = WebDriverWait(self.driver, 5)
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_food)
            ).click()

    def navigate_to_foodprice_page(self):
            wait = WebDriverWait(self.driver, 5)
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_foodprice)
            ).click()



    

        