from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SideMenu:
    def __init__(self,driver):
        self.driver = driver
        #self.show_tree_groups_button_locator = (((By.XPATH, '//a[span[normalize-space()="تعاریف"]]')))

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

        self.GroupsSettings_locator  = (((By.XPATH, '//a[span[normalize-space()="تنظیمات گروه ها"]]')))
        self.GroupsSettings_mealplan_locator  = (((By.CSS_SELECTOR, "a[href='#!/Diet']")))
        


    def _click(self, locator):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _expand_if_needed(self, parent_locator, child_locator):
        elements = self.driver.find_elements(*child_locator)

        if not elements or not elements[0].is_displayed():
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

        self.driver.execute_script("window.scrollTo(0,0)")

        #/////////////////////////////////////////////////////



    def navigate2(self, section_locator, page_locator):

        self._expand_if_needed(
            self.GroupsSettings_locator,
            section_locator
        )

        self._expand_if_needed(
            section_locator,
            page_locator
        )

        self._click(page_locator)

        self.driver.execute_script("window.scrollTo(0,0)")


    

        