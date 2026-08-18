import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from Components.Base_page import BasePage
from Components.Main_Menu import SideMenu


class FoodManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.new_button_locator = (
            By.XPATH,
            "//div[@ng-controller='ListFoodsCtrl']//a[@title='غذای جدید']",
        )
        self.name_field_locator = (By.ID, "Foodname")
        self.foodtype_field_locator = (By.XPATH, '//*[@id="ListFoodTypes"]/select')
        self.submit_button_locator = (By.XPATH, "//button[contains(text(),'ثبت')]")
        self.error_message_locator = (
            By.CSS_SELECTOR,
            "#toast-container .toast-warning .toast-message div",
        )

    def is_food_created(self, name):
        locator = (By.XPATH, f"(//td[contains(text(),'{name}')])[1]")
        return self.is_visible(locator)

    def open_new_food_form(self):
        with allure.step("Open new food form"):
            side_menu = SideMenu(self.driver)
            side_menu.navigate(
                side_menu.Definitions_locator,
                side_menu.Definitions_feeding_locator,
                side_menu.Definitions_feeding_food_locator,
            )

            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.element_to_be_clickable(self.new_button_locator)).click()

            wait.until(EC.visibility_of_element_located(self.submit_button_locator))

    def enter_name(self, name):
        with allure.step("Enter foodname"):
            self.driver.find_element(*self.name_field_locator).send_keys(name)

    def enter_foodtype(self, foodtype):
        with allure.step("Enter foodtype"):
            self.driver.find_element(*self.foodtype_field_locator)
            select = Select(self.driver.find_element(*self.foodtype_field_locator))
            select.select_by_visible_text(foodtype)

    def submit_form(self):
        with allure.step("submit form"):
            self.driver.find_element(*self.submit_button_locator).click()

    def create_food(self, name, foodtype):
        self.open_new_food_form()
        self.enter_name(name)
        self.enter_foodtype(foodtype)
        self.submit_form()

        error = self.get_error_message(self.error_message_locator, timeout=2)

        if error:
            return False, error

        return self.is_food_created(name), None
