# understandingMethodsAndClasses.py | ian luna

class Cat(object):
    """docstring for Dog."""

    def __init__(self, arg):
        super(Dog, self).__init__()
        self.arg = arg

class Dog:
    def __init__(self, name, legs, colour):
        self.name = name
        self.legs = legs
        self.colour = colour

    def __str__(self):
        obstring = self.name + ' ' + self.colour + ' ' + str(self.legs)
        return obstring

    def name(self):
        nameStr = self.name
        return nameStr

fido = Dog('fido', 4, 'brown')
buddy = Dog('buddy', 4, 'beagle-colour')

print(buddy.name)
