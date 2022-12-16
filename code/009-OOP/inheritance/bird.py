# Bird is our parent class
class bird:

    def __init__(self, feathers, wingspan):
        self.feathers = feathers
        self.wingspan = wingspan

    def eat(self):
        return "*eating sounds*"