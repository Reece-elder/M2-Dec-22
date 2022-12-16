# Penguin is our child class
from bird import bird

# When making a child class, specify the parent within ()
class penguin(bird):
    def __init__(self, feathers, wingspan, bellySlideSpeed):
        # Run our parent constructor, which in turn makes a Bird object
        # super() is our parent class (Bird)
        super().__init__(feathers, wingspan)
        self.bellySlideSpeed = bellySlideSpeed
    
    def swim():
        return "*Swimming sounds* *bubble bubble*"

pingu = penguin("black and white", 23, 50)
print(pingu.eat())
print(pingu.feathers)