import pytest
import allure
from Helpers.data_loader import DataLoader
from PageObjects.LoginPage_POM import LoginPage
from PageObjects.MealPlan_POM import AddMealPlanPage


@pytest.mark.normal
@allure.epic("Group Settings")
@allure.feature("Add Temp Meal Plan")
@allure.story("Admin User Add A New Temp Meal Plan")
@allure.title("Add New Temp Meal Plan")
@allure.severity(allure.severity_level.Normal)
def test_add_new_temp_meal(driver):
    login_page = LoginPage(driver)
    add_meal_plan_page = AddMealPlanPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = add_meal_plan_page.add_temp_meal(
        **DataLoader.load_addmeal("default")
    )

    assert success, (
        f"Create food failed. Server message: {error}"
        if error
        else "Create food should be successful but it was not."
    )


@pytest.mark.normal
@allure.epic("Group Settings")
@allure.feature("Add Temp Meal Plan")
@allure.story("Admin User Add A Duplicate Temp Meal Plan")
@allure.title("Add Duplicate Temp Meal Plan")
@allure.severity(allure.severity_level.Normal)
def test_add_duplicate_temp_meal(driver):
    login_page = LoginPage(driver)
    add_meal_plan_page = AddMealPlanPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))
    success, error = add_meal_plan_page.add_duplicate_temp_meal(
        **DataLoader.load_addmeal("duplicate")
    )

    assert not success
    assert error == "غذای انتخاب شده قبلا در این وعده و در همین سلف ها ثبت شده است."
