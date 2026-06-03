class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self._quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(quantity)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if isinstance(other, Ingredient):
            raise TypeError("Сравнивать можно только экземпляры одного класса")
        if self.name == other.name and self.unit == other.unit:
            return True
        return False
