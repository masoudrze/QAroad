from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainMenu:
    def __init__(self,driver):
        self.driver = driver
        self.Definitions_menu=(((By.XPATH, '//a[span[normalize-space()="تعاریف"]]')))
        self.Definitions_menu_base_info=(((By.XPATH, '//a[span[normalize-space()="اطلاعات پایه"]]')))
        self.Definitions_menu_base_info_group=(((By.XPATH, '//a[normalize-space()="گروه"]')))

    
    def create_group_menu(self):
        self.driver.find_element(*self.Definitions_menu).click()
        self.driver.find_element(*self.Definitions_menu_base_info).click()
        self.driver.find_element(*self.Definitions_menu_base_info_group).click()



    

        