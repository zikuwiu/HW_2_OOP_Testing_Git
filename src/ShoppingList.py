from src.Ingredient import Ingredient
from src.Recipe import Recipe




class ShoppingList:
    def __init__(self):
        self._items = list()
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled_recipe = recipe.scale(portions)
        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))
    def remove_recipe(self, title: str):
        for ingredient in self._items:
            if ingredient[1] == title:
                self._items.remove(ingredient)
    def get_list(self):
        dict = dict()
        list = list()
        for ingredient in self._items:
            key = (ingredient[0].name, ingredient[0].unit)
            if key in dict:
                dict[key] += ingredient[0].quantity
            else:
                dict[key] = ingredient[0].quantity
        for ingredient in dict.keys():
            list.append(Ingredient(ingredient[0], dict[ingredient], ingredient[1]))
        list.sort(key=lambda name: ingredient.name)
        return list

    def __add__(self, other):
        if not isinstance(other, ShoppingList):
            raise TypeError("Добавить можно только список покупок")
        return self.get_list() + other.get_list()