import pytest
import allure
from Helpers.data_loader import DataLoader
from PageObjects.Create_FoodType_POM import FoodTypeManagementPage
from PageObjects.LoginPage_POM import LoginPage


@pytest.mark.dependency(
    name="create_foodtype",
    depends=["admin_login"]
)
@pytest.mark.blocker
@allure.epic("Definitions")
@allure.feature("Create FoodType")
@allure.story("Admin User Creating A New FoodType")
@allure.title("Create New FoodType")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_new_foodtype(driver):
    login_page = LoginPage(driver)
    foodtype_management_page = FoodTypeManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = foodtype_management_page.create_foodtype(
        **DataLoader.load_foodtype("default")
    )

    assert success, (
        f"Create food failed. Server message: {error}"
        if error
        else "Create food should be successful but it was not."
    )


@pytest.mark.dependency(
    depends=["admin_login"]
)
@pytest.mark.blocker
@allure.epic("Definitions")
@allure.feature("Create FoodType")
@allure.story("Admin User Creating A Duplicate FoodType")
@allure.title("Create Duplicate FoodType")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_duplicate_foodtype(driver):
    login_page = LoginPage(driver)
    foodtype_management_page = FoodTypeManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = foodtype_management_page.create_foodtype(
        **DataLoader.load_foodtype("duplicate")
    )

    assert not success
    assert error == 'نام وارد شده تکراری می باشد'
