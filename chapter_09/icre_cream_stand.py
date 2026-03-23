from restaurant import Restaurant

class IceCreanStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'mango']

    def display_flavours(self):
        for flavour in self.flavours:
            print(flavour)

ics = IceCreanStand('Icy', 'american')

ics.display_flavours()
