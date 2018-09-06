class Ingredient():
    def __init__(self, material, amount, amount_type=None,
                 description='', **kwargs):
        self.material = material
        self.amount = float(amount)
        self.amount_type = amount_type
        self.description = description
        self.additional_info = kwargs

    def get(self):
        ingredient_dict = {'material': self.material, 'amount': self.amount,
                           'amount_type': self.amount_type,
                           'description': self.description,
                           'additional_info': self.additional_info}
        return ingredient_dict
        
    def get_amount(self):
        return self.amount, self.amount_type

    def set_amount(self, amount, amount_type=None):
        try:
            type(amount) == float
        except:
            raise ValueError('Amount must be passed as float.')

        self.amount = amount
        if amount_type:
            self.amount_type = amount_type
        return self.amount, self.amount_type

    def get_material(self):
        return self.material

    def set_material(self, material):
        try:
            type(material) == str
        except:
            raise ValueError('Material must be passed as string')

        self.material = material
        return self.material

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
        return self.description

def main():
    i = Ingredient('Flour', 1, amount_type='kg', description='Best Flour only.',
                   flour_type='Weizen')

    print(i.get())

if __name__ == '__main__':
    main()
    

    
