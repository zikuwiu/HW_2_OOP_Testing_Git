from typing import override

from src.Recipe import Recipe


class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    @override
    def scale(self, ratio: float):
        recipe = super.scale(ratio)
        return DietaryRecipe(recipe.title, recipe.diet_type, recipe.ingredients)
    @override
    def __str__(self):
        return f"[{self.diet_type}]" + super().__str__()