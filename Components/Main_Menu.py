from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SideMenu:
    def __init__(self,driver):
        self.driver = driver
        self.show_tree_groups_button_locator = (((By.XPATH, '//a[span[normalize-space()="تعاریف"]]')))

        self.Definitions_locator = (((By.XPATH, '//a[span[normalize-space()="تعاریف"]]')))
        self.Definitions_base_info_locator = (((By.XPATH, '//a[span[normalize-space()="اطلاعات پایه"]]')))
        self.Definitions_base_info_group_locator = (((By.XPATH, '//a[normalize-space()="گروه"]')))
        self.Definitions_base_info_users_locator = (((By.XPATH, '//a[normalize-space()="افراد"]')))

        self.Definitions_feeding_locator = (((By.XPATH, '//a[span[normalize-space()="تغذیه"]]')))
        self.Definitions_feeding_meal_locator = (((By.XPATH, '//a[normalize-space()="وعده"]')))
        self.Definitions_feeding_self_locator = (((By.XPATH, '//a[normalize-space()="سلف"]')))
        self.Definitions_feeding_foodtype_locator = (((By.XPATH, '//a[normalize-space()="نوع غذا"]')))
        self.Definitions_feeding_food_locator = (((By.XPATH, '//a[normalize-space()="غذا"]')))
        self.Definitions_feeding_foodprice_locator = (((By.XPATH, '//a[normalize-space()="قیمت غذا"]')))
        

    

    def navigate_to_group_page(self):
        wait = WebDriverWait(self.driver, 5)

        wait.until(
            EC.element_to_be_clickable(self.Definitions_locator)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.Definitions_base_info_locator)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.Definitions_base_info_group_locator)
        ).click()





    def navigate_to_users_page(self):
        wait = WebDriverWait(self.driver, 5)

        wait.until(
            EC.element_to_be_clickable(self.Definitions_locator)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.Definitions_base_info_locator)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.Definitions_base_info_users_locator)
        ).click()


    def navigate_to_meal_page(self):
        wait = WebDriverWait(self.driver, 5)
    
        wait.until(
            EC.element_to_be_clickable(self.Definitions_locator)
        ).click()
    
        wait.until(
            EC.element_to_be_clickable(self.Definitions_feeding_locator)
        ).click()
    
        wait.until(
            EC.element_to_be_clickable(self.Definitions_feeding_meal_locator)
        ).click()


    def navigate_to_self_page(self):
            wait = WebDriverWait(self.driver, 5)

            wait.until(
                EC.element_to_be_clickable(self.Definitions_locator)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_locator)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_self_locator)
            ).click()

    def navigate_to_foodtype_page(self):
            wait = WebDriverWait(self.driver, 5)
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_locator)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_locator)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_foodtype_locator)
            ).click()

    def navigate_to_food_page(self):
            wait = WebDriverWait(self.driver, 5)
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_locator)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_locator)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_food_locator)
            ).click()

    def navigate_to_foodprice_page(self):
            wait = WebDriverWait(self.driver, 5)
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_locator)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_locator)
            ).click()
        
            wait.until(
                EC.element_to_be_clickable(self.Definitions_feeding_foodprice_locator)
            ).click()



    

        