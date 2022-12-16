class cakeConstructor:
    # Allowing the dev to input values for the cake
    # __init__ (2x _ on each side) initial function and replaces the default
    # Constructor, it allows us to construct an object 
    def __init__(self, flavour, tiers, toppings, gluten_free):
        self.flavourObj = flavour
        self.tiersObj = tiers
        self.toppingsObj = toppings
        self.gluten_freeObj = gluten_free

    def eatCake(self):
        return f"Cake tastes like {self.flavourObj}"

newCake = cakeConstructor("marzipany almondy", 4, ["marzipan", "colourings"], False)
print(newCake.tiersObj)
print(newCake.eatCake())

# Inbuilt functions that work with attributes
# getattr - used to retrieve the attribute value
print(getattr(newCake, 'tiersObj')) # More flexible, easier to loop and pass in variables into these

# hasattr - returns true or false if the object has that attr
print(hasattr(newCake, 'calories'))

# setattr - Sets the value of an attribute (and creates if not there)
setattr(newCake, 'calories', 11000)
print(getattr(newCake, 'calories'))

# delattr - Deletes the attribute
delattr(newCake, 'calories')

