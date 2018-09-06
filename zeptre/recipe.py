from ingredient import Ingredient

class Recipe():
    def __init__(self, name, description, ingredients, directions, **kwargs):
        self.name = name
        self.description = description
        self.ingredients = self.__setup_ingredients(ingredients, kwargs)
        self.directions = directions

    def get_ingredients(self):
        return [ing.get() for ing in self.ingredients]

    def __setup_ingredients(self, ingredients, kwargs):
        return [Ingredient(ing['material'], ing['amount'], amount_type=ing['amount_type'], description=ing['description'], **kwargs) for ing in ingredients]

        

def main():
    r = Recipe('Cookie', '', [{'material': 'Flour', 'amount': 1, 'amount_type': 'kg', 'description': ''}], '', **{'beware': 'only best flour possible'})
    print(r.get_ingredients())

if __name__ == '__main__':
    main()
