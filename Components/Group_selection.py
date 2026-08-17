from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class GroupSelection:
    def __init__(self, driver):
        self.driver = driver
        self.Show_group_tree_button = (
            By.XPATH,
            "//a[@ng-click='ShowTreeGroupsDialog()']",
        )
        self.group_tree_box = (By.XPATH, "//div[@id='treeviewgroupslist']")
        self.select = (
            By.XPATH,
            "//li[@class='list-group-item active']//span[@data-role='display'][contains(text(),'دانشجویان')]",
        )

    def select_group(self, group_name):
        wait = WebDriverWait(self.driver, 5)
        option = (
            By.XPATH,
            f"//li[@class='list-group-item']//span[@data-role='display'][contains(text(),'{group_name}')]",
        )
        wait.until(EC.element_to_be_clickable(self.Show_group_tree_button)).click()

        wait.until(EC.element_to_be_clickable(option)).click()
