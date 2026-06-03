from src.Ingredient import Ingredient


class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for exist_ingredient in self.ingredients:
            if exist_ingredient == ingredient:
                exist_ingredient.quantity = ingredient.quantity + exist_ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float)) and ratio > 0:
            return True
        return False

    def scale(self, ratio: float):
        if self.is_valid_ratio(ratio):
            scaled_ingredients = list()
            for ingredient in self.ingredients:
                scaled_ingredients.append(Ingredient(
                    ingredient.name, ingredient.quantity * ratio, ingredient.unit
                ))
            return Recipe(self.title, scaled_ingredients)
        else:
            raise ValueError(
                "Ratio must be positive")  # Мне нравится когда ошибки на английском выводятся. Могу и делаю.

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        str_ingredients = list()
        for ingredient in self.ingredients:
            str_ingredients.append(str(ingredient))
        ans = "Блюдо:" + self.title + "\nИнгридиенты:\n" + "\n".join(str_ingredients)
        return ans