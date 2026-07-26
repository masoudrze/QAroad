import json
from pathlib import Path


class DataLoader:

    @staticmethod
    def load_meal(key):
        file_path = Path(__file__).parent.parent / "Data" / "Meals.json"

        with open(file_path, encoding="utf-8") as file:
            meals = json.load(file)

        return meals[key]