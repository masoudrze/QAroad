import pytest
from PageObjects.LoginPage_POM import LoginPage
from PageObjects.MealPlan_POM import AddMealPlanPage
from Helpers.data_loader import DataLoader


@pytest.mark.smoke
def test_add_new_temp_meal(driver):
    login_page = LoginPage(driver)
    add_meal_plan_page = AddMealPlanPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = add_meal_plan_page.add_temp_meal(**DataLoader.load_addmeal("default"))

    assert success, (
        f"Create food failed. Server message: {error}"
        if error
        else "Create food should be successful but it was not."
    )
    

@pytest.mark.negative
def test_add_duplicate_temp_meal(driver):
    login_page = LoginPage(driver)
    add_meal_plan_page = AddMealPlanPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))
    success, error = add_meal_plan_page.add_duplicate_temp_meal(**DataLoader.load_addmeal("duplicate"))

    assert not success
    assert error == 'غذای انتخاب شده قبلا در این وعده و در همین سلف ها ثبت شده است.'




