class Product:
    """ 
    Class that contains all products sold by Acme Corporation. 
    
    Parent Class
    """
    import random

    def __init__(self, name, identifier=random.randint(1000000, 9999999),\
        price=10, weight=20, flammability=0.5):
        self.name = str(name)
        self.identifier = identifier
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability) 

    def stealability(self):
        steal = self.price / self.weight
        if steal < 0.5:
            return 'Not so stealable...'
        elif (steal >= 0.5) & (steal < 1.0):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'
    
    def explode(self):
        flame = self.flammability * self.weight
        if flame < 10:
            return '...fizzle'
        elif (flame >= 10) & (flame < 50):
            return '...boom!'
        else:
            return '...BABOOM!'

class BoxingGlove(Product):
    """
    Child class
    """
    import random

    def __init__(self, name, identifier=random.randint(1000000, 9999999),\
        price=10, weight=10, flammability=0.5):
        self.name = str(name)
        self.identifier = identifier
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)

    def explode(self):
        return '...it\'s a glove.glove'
    
    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif (self.weight >= 5) & (self.weight < 15):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'


