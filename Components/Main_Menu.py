from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException

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
        
    #///////////////////////////////

    def _click(self, locator):
        WebDriverWait(self.driver, 1).until(
            EC.element_to_be_clickable(locator)
        ).click()



    def _expand_if_needed(self, parent_locator, child_locator):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located(child_locator)
            )
        except TimeoutException:
            self._click(parent_locator)



    def navigate(self, section_locator, page_locator):

        self._expand_if_needed(
            self.Definitions_locator,
            section_locator
        )

        self._expand_if_needed(
            section_locator,
            page_locator
        )

        self._click(page_locator)
    #///////////////////////////////
    '''

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


'''
    

        