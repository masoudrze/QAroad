import json
from pathlib import Path

from Helpers.config import (
    ADMIN_PASSWORD,
    ADMIN_USERNAME,
    FAIL_PASSWORD,
    USER_PASSWORD,
    USER_USERNAME,
)


class DataLoader:
    @staticmethod
    def _load(file_name, key):
        file_path = Path(__file__).parent.parent / "Data" / file_name

        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        return data[key]

    @staticmethod
    def load_login(key):
        credentials = {
            "admin_pass": {
                "username": ADMIN_USERNAME,
                "password": ADMIN_PASSWORD,
            },
            "user_pass": {
                "username": USER_USERNAME,
                "password": USER_PASSWORD,
            },
            "admin_fail": {
                "username": ADMIN_USERNAME,
                "password": FAIL_PASSWORD,
            },
            "user_fail": {
                "username": USER_USERNAME,
                "password": FAIL_PASSWORD,
            },
        }
        return credentials[key]

    @staticmethod
    def load_group(key):
        return DataLoader._load("Groups.json", key)

    @staticmethod
    def load_user(key):
        return DataLoader._load("Users.json", key)

    @staticmethod
    def load_meal(key):
        return DataLoader._load("Meals.json", key)

    @staticmethod
    def load_self(key):
        return DataLoader._load("Selfs.json", key)

    @staticmethod
    def load_foodtype(key):
        return DataLoader._load("FoodTypes.json", key)

    @staticmethod
    def load_food(key):
        return DataLoader._load("Foods.json", key)

    @staticmethod
    def load_foodprice(key):
        return DataLoader._load("FoodPrices.json", key)

    @staticmethod
    def load_addmeal(key):
        return DataLoader._load("AddMeal.json", key)
