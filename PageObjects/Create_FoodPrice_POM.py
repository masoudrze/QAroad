import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Components.Base_page import BasePage
from Components.Group_selection import GroupSelection
from Components.Main_Menu import SideMenu


class FoodPriceManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.new_button_locator = (
            By.XPATH,
            "//div[@ng-controller='ListGroupFoodPriceCtrl']//a[@title='قیمت جدید']",
        )
        self.name_field_locator = (
            By.XPATH,
            "/html[1]/body[1]/div[3]/div[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/span[1]/span[1]/span[1]/span[1]",
        )
        self.free_price_field_locator = (By.ID, "FreePrice")
        self.yarane_price_field_locator = (By.ID, "YaranePrice")
        self.rozforoosh_price_field_locator = (By.ID, "RozForoshPrice")
        self.bireserve_price_field_locator = (By.ID, "BiReservePrice")
        self.submit_button_locator = (By.XPATH, "//button[contains(text(),'ثبت')]")
        self.error_message_locator = (
            By.CSS_SELECTOR,
            "#toast-container .toast-warning .toast-message div",
        )

    def is_foodprice_created(self, name):
        locator = (By.XPATH, f"(//td[contains(text(),'{name}')])[1]")
        return self.is_visible(locator)

    def open_new_foodprice_form(self, group_name):
        with allure.step("open new foodprice form"):
            side_menu = SideMenu(self.driver)
            group_selection = GroupSelection(self.driver)

            side_menu.navigate(
                side_menu.Definitions_locator,
                side_menu.Definitions_feeding_locator,
                side_menu.Definitions_feeding_foodprice_locator,
            )
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.visibility_of_element_located(self.new_button_locator))
            group_selection.select_group(group_name)
            wait.until(EC.element_to_be_clickable(self.new_button_locator)).click()
            wait.until(EC.visibility_of_element_located(self.submit_button_locator))

    def enter_name(self, name):
        with allure.step("Enter foodname"):
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.element_to_be_clickable(self.name_field_locator)).click()

            wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space()='{name}']"))
            ).click()

    def enter_free_price(self, free_price):
        with allure.step("Enter free price"):
            self.driver.find_element(*self.free_price_field_locator).send_keys(free_price)

    def enter_yarane_price(self, yarane_price):
        with allure.step("Enter yarane price"):
            self.driver.find_element(*self.yarane_price_field_locator).send_keys(
                yarane_price
            )

    def enter_rozforoosh_price(self, rozforoosh_price):
        with allure.step("Enter rozforoosh price"):
            self.driver.find_element(*self.rozforoosh_price_field_locator).send_keys(
                rozforoosh_price
            )

    def enter_bireserve_price(self, bireserve_price):
        with allure.step("Enter bireserve price"):
            self.driver.find_element(*self.bireserve_price_field_locator).send_keys(
                bireserve_price
            )

    def select_meal(self, meal_names):
        with allure.step("Enter meal name"):
            wait = WebDriverWait(self.driver, 5)

            meal_name = [name.strip() for name in meal_names.split(",") if name.strip()]
            for name in meal_name:
                select_meal_locator = (
                    By.XPATH,
                    f"//span[@data-role='display' and normalize-space()='{name}']/preceding-sibling::span[@data-role='checkbox']//label",
                )
                wait.until(EC.element_to_be_clickable(select_meal_locator)).click()

    def select_self(self, self_names):
        with allure.step("Enter selfname"):
            wait = WebDriverWait(self.driver, 5)

            self_name = [name.strip() for name in self_names.split(",") if name.strip()]
            for name in self_name:
                select_self_locator = (
                    By.XPATH,
                    f"//span[@data-role='display' and normalize-space()='{name}']/preceding-sibling::span[@data-role='checkbox']//label",
                )
                wait.until(EC.element_to_be_clickable(select_self_locator)).click()

    def submit_form(self):
        with allure.step("submit form"):
            self.driver.find_element(*self.submit_button_locator).click()

    def create_new_foodprice(
        self,
        group_name,
        name,
        free_price,
        yarane_price,
        rozforoosh_price,
        bireserve_price,
        meal_names,
        self_names,
    ):
        self.open_new_foodprice_form(group_name)
        self.enter_name(name)
        self.enter_free_price(free_price)
        self.enter_yarane_price(yarane_price)
        self.enter_rozforoosh_price(rozforoosh_price)
        self.enter_bireserve_price(bireserve_price)
        self.select_meal(meal_names)
        self.select_self(self_names)
        self.submit_form()

        error = self.get_error_message(self.error_message_locator, timeout=2)

        if error:
            return False, error

        return self.is_foodprice_created(name), None
