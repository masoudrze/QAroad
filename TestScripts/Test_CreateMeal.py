import pytest
import allure
from Helpers.data_loader import DataLoader
from PageObjects.Create_Meal_POM import MealManagementPage
from PageObjects.LoginPage_POM import LoginPage

@pytest.mark.dependency(
    name="create_meal",
    depends=["admin_login"]
)
@pytest.mark.blocker
@allure.epic("Definitions")
@allure.feature("Create Meal")
@allure.story("Admin User Creating A New Meal")
@allure.title("Create New Meal")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_new_meal(driver):
    login_page = LoginPage(driver)
    meal_management_page = MealManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = meal_management_page.create_meal(**DataLoader.load_meal("default"))

    assert success, (
        f"Create meal failed. Server message: {error}"
        if error
        else "Create meal should be successful but it was not."
    )


@pytest.mark.dependency(
    depends=["admin_login"]
)
@pytest.mark.blocker
@allure.epic("Definitions")
@allure.feature("Create Meal")
@allure.story("Admin User Creating A Duplicate Meal")
@allure.title("Create Duplicate Meal")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_duplicate_meal(driver):
    login_page = LoginPage(driver)
    meal_management_page = MealManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = meal_management_page.create_meal(
        **DataLoader.load_meal("duplicate")
    )

    assert not success
    assert error == 'نام وارد شده تکراری می باشد'
