import json
from pathlib import Path


class DataLoader:
    '''
    @staticmethod
    def load_meal(key):
        file_path = Path(__file__).parent.parent / "Data" / "Meals.json"

        with open(file_path, encoding="utf-8") as file:
            meals = json.load(file)

        return meals[key]
    '''

    @staticmethod
    def _load(file_name, key):
        file_path = Path(__file__).parent.parent / "Data" / file_name

        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        return data[key]



    @staticmethod
    def load_meal(key):
        return DataLoader._load("Meals.json", key)

    @staticmethod
    def load_login(key):
        return DataLoader._load("Login.json", key)

 