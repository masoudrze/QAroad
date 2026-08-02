from PageObjects.LoginPage_POM import LoginPage
from PageObjects.Create_Food_POM import FoodManagementPage
from Helpers.data_loader import DataLoader


def test_create_new_food(driver):
    login_page = LoginPage(driver)
    food_management_page = FoodManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    food_data = DataLoader.load_food("default")

    food_management_page.create_food(**DataLoader.load_food("default"))

    assert food_management_page.is_food_created(food_data["name"]),"Create food should be successful but it is not"
