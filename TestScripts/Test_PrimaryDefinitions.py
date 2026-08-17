import pytest
from PageObjects.LoginPage_POM import LoginPage
from PageObjects.Create_Group_POM import GroupManagementPage
from PageObjects.Create_User_POM import UserManagementPage
from PageObjects.Create_Meal_POM import MealManagementPage
from PageObjects.Create_Self_POM import SelfManagementPage
from PageObjects.Create_FoodType_POM import FoodTypeManagementPage
from PageObjects.Create_Food_POM import FoodManagementPage
from PageObjects.Create_FoodPrice_POM import FoodPriceManagementPage
from Helpers.data_loader import DataLoader


@pytest.mark.smoke
def test_primary_definitions(driver):
    login_page = LoginPage(driver)
    group_management_page = GroupManagementPage(driver)
    user_management_page = UserManagementPage(driver)
    meal_management_page = MealManagementPage(driver)
    self_management_page = SelfManagementPage(driver)
    foodtype_management_page = FoodTypeManagementPage(driver)
    food_management_page = FoodManagementPage(driver)
    food_price_management_page = FoodPriceManagementPage(driver)

    login_page.login(**DataLoader.load_login("admin_pass"))
    
    assert group_management_page.create_group(**DataLoader.load_group("default"))
    
    assert user_management_page.create_user(**DataLoader.load_user("default"))
    
    assert meal_management_page.create_meal(**DataLoader.load_meal("default"))
    
    assert self_management_page.create_self(**DataLoader.load_self("default"))
    
    assert foodtype_management_page.create_foodtype(**DataLoader.load_foodtype("default"))
    
    assert food_management_page.create_food(**DataLoader.load_food("default"))
    driver.refresh()
    
    assert food_price_management_page.create_new_foodprice(**DataLoader.load_foodprice("default"))
