import pytest
import allure
from Helpers.data_loader import DataLoader
from PageObjects.Create_Food_POM import FoodManagementPage
from PageObjects.LoginPage_POM import LoginPage


@pytest.mark.critical
@allure.epic("Definitions")
@allure.feature("Create Food")
@allure.story("Admin User Creating A New Food")
@allure.title("Create New Food")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_new_food(driver):
    login_page = LoginPage(driver)
    food_management_page = FoodManagementPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = food_management_page.create_food(**DataLoader.load_food("default"))

    assert success, (
        f"Create food failed. Server message: {error}"
        if error
        else "Create food should be successful but it was not."
    )


@pytest.mark.critical
@allure.epic("Definitions")
@allure.feature("Create Food")
@allure.story("Admin User Creating A Duplicate Food")
@allure.title("Create Duplicate Food")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_duplicate_food(driver):
    login_page = LoginPage(driver)
    food_management_page = FoodManagementPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = food_management_page.create_food(
        **DataLoader.load_food("duplicate")
    )

    assert not success
    assert error == 'نام وارد شده تکراری می باشد'
