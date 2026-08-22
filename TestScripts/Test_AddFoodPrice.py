import pytest
import allure
from Helpers.data_loader import DataLoader
from PageObjects.Create_FoodPrice_POM import FoodPriceManagementPage
from PageObjects.LoginPage_POM import LoginPage

@pytest.mark.dependency(
    name="add_food_price",
    depends=["create_meal","create_self","create_food"]
)
@pytest.mark.blocker
@allure.epic("Definitions")
@allure.feature("Add Food Price")
@allure.story("Admin User Add A New Food Price")
@allure.title("Add New Food Price")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_new_foodprice(driver):
    login_page = LoginPage(driver)
    food_price_management_page = FoodPriceManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = food_price_management_page.create_new_foodprice(
        **DataLoader.load_foodprice("default")
    )

    assert success, (
        f"Adding food price failed. Server message: {error}"
        if error
        else "Adding food price should be successful but it was not."
    )


@pytest.mark.dependency(
    depends=["create_meal","create_self","create_food"]
)
@pytest.mark.blocker
@allure.epic("Definitions")
@allure.feature("Add Food Price")
@allure.story("Admin User Add A Duplicate Food Price")
@allure.title("Add Duplicate Food Price")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_duplicate_foodprice(driver):
    login_page = LoginPage(driver)
    food_price_management_page = FoodPriceManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = food_price_management_page.create_new_foodprice(
        **DataLoader.load_foodprice("duplicate")
    )

    assert not success
    assert (
        error
        == "قیمت این غذا برای یک یا چند وعده و سلف های انتخابی شما قبلا تعریف شده است."
    )
