import pytest

from Helpers.data_loader import DataLoader
from PageObjects.Create_Meal_POM import MealManagementPage
from PageObjects.LoginPage_POM import LoginPage


@pytest.mark.smoke
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


@pytest.mark.negative
def test_create_duplicate_meal(driver):
    login_page = LoginPage(driver)
    meal_management_page = MealManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = meal_management_page.create_meal(
        **DataLoader.load_meal("duplicate")
    )

    assert not success
    assert error == "وعده با این نام وجود دارد."
