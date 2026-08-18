import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Components.Base_page import BasePage
from Components.Main_Menu import SideMenu


class GroupManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.new_button_locator = (
            By.XPATH,
            "//div[@ng-controller='ListGroupsCtrl']//a[@title='گروه جدید']",
        )
        self.name_field_locator = (By.ID, "Groupname")
        self.MinIncreaseCredit_field_locator = (By.ID, "MinIncreaseCredit")
        self.MaxIncreaseCredit_field_locator = (By.ID, "MaxIncreaseCredit")
        self.submit_button_locator = (By.XPATH, "(//button[contains(text(),'ثبت')])[1]")
        self.error_message_locator = (
            By.CSS_SELECTOR,
            "#toast-container .toast-warning .toast-message div",
        )

    def is_group_created(self, name):
        locator = (By.XPATH, f"(//td[contains(text(),'{name}')])[1]")
        return self.is_visible(locator)

    def open_new_group_form(self):
        with allure.step("open new group form"):
            side_menu = SideMenu(self.driver)
            side_menu.navigate(
                side_menu.Definitions_locator,
                side_menu.Definitions_base_info_locator,
                side_menu.Definitions_base_info_group_locator,
            )
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.element_to_be_clickable(self.new_button_locator)).click()
            wait.until(EC.element_to_be_clickable(self.submit_button_locator))

    def enter_name(self, name):
        with allure.step("Enter group name"):
            self.driver.find_element(*self.name_field_locator).send_keys(name)

    def enter_MinIncreaseCredit(self, MinIncreaseCredit):
        with allure.step("Enter group min increase credit"):
            self.driver.find_element(*self.MinIncreaseCredit_field_locator).send_keys(
                MinIncreaseCredit
            )

    def enter_MaxIncreaseCredit(self, MaxIncreaseCredit):
        with allure.step("Enter group max increase credit"):
            self.driver.find_element(*self.MaxIncreaseCredit_field_locator).send_keys(
                MaxIncreaseCredit
            )

    def submit_form(self):
        with allure.step("submit form"):
            self.driver.find_element(*self.submit_button_locator).click()

    def create_group(self, name, MinIncreaseCredit, MaxIncreaseCredit):
        self.open_new_group_form()
        self.enter_name(name)
        self.enter_MinIncreaseCredit(MinIncreaseCredit)
        self.enter_MaxIncreaseCredit(MaxIncreaseCredit)
        self.submit_form()

        error = self.get_error_message(self.error_message_locator, timeout=2)

        if error:
            return False, error

        return self.is_group_created(name), None
