import requests


class CakeRecipe():
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def roast(self):
        result = requests.get('https://api.cake.com/roast')

        if result.ok:
            return 'Roasted'

        return 'Not Roasted'

    def __str__(self):
        return f"Ingredients: {self.ingredients}"
