import json

from ingredient import Ingredient

class Recipe():
    def __init__(self, name, description, ingredients, directions, **kwargs):
        self.name = name
        self.description = description
        self.ingredients = self.__setup_ingredients(ingredients, **kwargs)
        self.directions = directions

    def save(self, path='./recipe_data.json', saving_format='json'):
        recipe_dict = {'name': self.name, 'description': self.description,
                       'ingredients': [ing.get() for ing in self.ingredients],
                       'directions': self.directions}
        fobj = open(path, 'w')
        json.dump(recipe_dict, fobj, indent=4, sort_keys=True)
        fobj.close()

    def load(self, path='./recipe_data.json', saving_format='json'):
        fobj = open(path, 'r')
        recipe_dict = json.load(fobj)
        fobj.close()

        self.name = recipe_dict['name']
        self.description = recipe_dict['description']
        self.ingredients = self.__setup_ingredients(recipe_dict['ingredients'])
        self.directions = recipe_dict['directions']
        
        
    def get_ingredients(self):
        return [ing.get() for ing in self.ingredients]

    def add_ingredient(self, ingredient, **kwargs):
        self.ingredients.append(Ingredient(ingredient['material'],
                                           ingredient['amount'],
                                           amount_type=ingredient['amount_type'],
                                           description=ingredient['description'],
                                           **kwargs))
        return self.ingredients

    def remove_ingredient(self, ingredient_id, by='all'):
        delete_entity = self.__search_ingredient(ingredient_id, by=by)
        try:
            self.ingredients.remove(delete_entity)
        except:
            print('Did not find {} by searching in terms of {}'.format(ingredient_id, by))
        del delete_entity
        return self.ingredients
        

    def __search_ingredient(self, ingredient_id, by='all'):
        for ing in self.ingredients:
            if by != 'all':
                if getattr(ing, by) == ingredient_id:
                    return ing
            else:
                if ingredient_id in ing.get().values():
                    return ing

    def __setup_ingredients(self, ingredients, **kwargs):
        print(ingredients)
        return [Ingredient(ing['material'], ing['amount'],
                           amount_type=ing['amount_type'],
                           description=ing['description'], **kwargs)
                for ing in ingredients]


        

def main():
    r = Recipe('Cookie', '', [{'material': 'Flour', 'amount': 1, 'amount_type': 'kg', 'description': ''}], '', **{'beware': 'only best flour possible'})
    print(r.get_ingredients())
    r.add_ingredient({'material': 'Tomato', 'amount': 1, 'amount_type': None, 'description': 'Youll need them5'})
    print(r.get_ingredients())
    r.save()
    print('Saving ...')
    r.remove_ingredient('Flour', by='amount')
    print(r.get_ingredients())
    r.remove_ingredient('Tomato', by='material')
    print(r.get_ingredients())
    print('Loading ...')
    r.load()
          

if __name__ == '__main__':
    main()
