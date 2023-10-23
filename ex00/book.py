from datetime import datetime


class Book:
    def __init__(self, name: str, last_update: datetime, creation_date: datetime, recipes_list: dict):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        pass

    def get_recipes_by_types(self, recipe_type):
        pass

    def add_recipe(self, recipe):
        pass
