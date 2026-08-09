from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Main_Menu import SideMenu
from selenium.webdriver.support.select import Select
from Components.Base_page import BasePage
import time


class AddMealPlanPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.select_meal_locator=((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/span[1]/button[1]"))
        self.maxcount_meal_locator=((By.XPATH, "//input[@id='MaxCount']"))
        self.select_meal_list_locator =((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]/span[1]"))
        self.add_temp_meal_locator = ((By.XPATH, "(//button[contains(text(),'افزودن')])[1]"))
        self.submit_button_locator = ((By.XPATH,"(//button[contains(text(),'ثبت برنامه')])[1]"))
        self.error_message_locator = (By.CSS_SELECTOR, "#toast-container .toast-warning .toast-message div")



    def is_meal_added(self, name):
        locator = (
            By.XPATH,
            f"(//td[contains(text(),'{name}')])[1]"
        )
        #return self.is_visible(locator)
        return True
    

    def open_new_meal_plan_form(self):
        side_menu = SideMenu(self.driver)
        side_menu.navigate(
        side_menu.GroupsSettings_locator,
        side_menu.GroupsSettings_locator,
        side_menu.GroupsSettings_mealplan_locator
        )
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.element_to_be_clickable(self.select_meal_locator)
        )
        wait.until(
        EC.visibility_of_element_located(self.submit_button_locator)
        )


    def select_meal(self,meal):
        self.driver.find_element(*self.select_meal_locator).click()
        select = ((By.XPATH, f"//ul[@role='select']//a[span[normalize-space()='{meal}']]"))

        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.element_to_be_clickable(select)
        ).click()


    def enter_foodname(self,foodname):
        print(foodname)
        
        wait = WebDriverWait(self.driver, 5)
        wait.until(
        EC.element_to_be_clickable(self.select_meal_list_locator)
            ).click()
        
        wait.until(
        EC.element_to_be_clickable(
        (By.XPATH, f"//li[normalize-space()='{foodname}']")
        )
            ).click()
        


    def add_max_count(self,max):
        self.driver.find_element(*self.maxcount_meal_locator).send_keys(max)

    def select_week_day(self,weekdays):
        wait = WebDriverWait(self.driver, 5)
        select_weekday_locator = (
        By.XPATH,
        "//label[normalize-space()='شنبه']"
        )
        wait.until(
            EC.element_to_be_clickable(select_weekday_locator)
        ).click()
        weekday = [day.strip() for day in weekdays.split(",") if day.strip()]
        for day in weekday:

            select_weekday_locator = (
            By.XPATH,
            f"//label[normalize-space()='{day}']"
            )
            wait.until(
                EC.element_to_be_clickable(select_weekday_locator)
            ).click()


    def select_selfs(self,selfs):
        wait = WebDriverWait(self.driver, 5)

        self = [name.strip() for name in selfs.split(",") if name.strip()]
        for name in self:

            select_self_locator = (
            By.XPATH,
            f"//div[@id='normalcheckboxlistself']//li[.//span[@data-role='display' and normalize-space()='{name}']]//label"
            )
            wait.until(
                EC.element_to_be_clickable(select_self_locator)
            ).click()

    def add_temp_meal(self,meal,foodname,max,weekdays,selfs):
        self.open_new_meal_plan_form()
        self.select_meal(meal)
        self.enter_foodname(foodname)
        time.sleep(5)
        self.add_max_count(max)
        self.select_week_day(weekdays)
        self.select_selfs(selfs)
        self.driver.find_element(*self.add_temp_meal_locator).click()


    def submit_form(self):
        self.driver.find_element(*self.submit_button_locator).click()


    def add_meal(self,meal,foodname,max,weekdays,selfs):

        self.add_temp_meal(meal,foodname,max,weekdays,selfs)
        self.submit_form()
        

        if error := self.get_error_message(self.error_message_locator, timeout=2):
            return False, error
        return self.is_meal_added('ybh'), None




    




