from PageObjects.LoginPage_POM import LoginPage
from PageObjects.Create_Food_POM import FoodManagementPage
from Helpers.data_loader import DataLoader


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



def test_create_duplicate_food(driver):
    login_page = LoginPage(driver)
    food_management_page = FoodManagementPage(driver)
    login_page.login(**DataLoader.load_login("admin_pass"))

    success, error = food_management_page.create_food(**DataLoader.load_food("duplicate"))

    assert not success
    assert error == 'غذا با این نام وجود دارد.'




