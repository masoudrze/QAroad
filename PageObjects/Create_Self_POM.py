from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Components.Base_page import BasePage
from Components.Main_Menu import SideMenu


class SelfManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_new_button_locator = (
            By.XPATH,
            "//div[@ng-controller='ListSelfsCtrl']//a[@title='سلف جدید']",
        )
        self.name_field_locator = (By.ID, "Selfname")
        self.capacity_field_locator = (By.ID, "Capacity")
        self.submit_button_locator = (By.XPATH, "//button[contains(text(),'ثبت')]")
        self.error_message_locator = (
            By.CSS_SELECTOR,
            "#toast-container .toast-warning .toast-message div",
        )

    def is_self_created(self, name):
        locator = (By.XPATH, f"(//td[contains(text(),'{name}')])[1]")
        return self.is_visible(locator)

    def open_new_self_form(self):
        side_menu = SideMenu(self.driver)
        side_menu.navigate(
            side_menu.Definitions_locator,
            side_menu.Definitions_feeding_locator,
            side_menu.Definitions_feeding_self_locator,
        )
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(self.add_new_button_locator)).click()

        wait.until(EC.visibility_of_element_located(self.submit_button_locator))

    def enter_name(self, name):
        self.driver.find_element(*self.name_field_locator).send_keys(name)

    def enter_capacity(self, capacity):
        self.driver.find_element(*self.capacity_field_locator).send_keys(capacity)

    def submit_form(self):
        self.driver.find_element(*self.submit_button_locator).click()

    def create_self(self, name, capacity):
        self.open_new_self_form()
        self.enter_name(name)
        self.enter_capacity(capacity)
        self.submit_form()

        error = self.get_error_message(self.error_message_locator, timeout=2)

        if error:
            return False, error

        return self.is_self_created(name), None
