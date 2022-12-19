# PolyMorphism 
# Poly  - Multiple or Many
# Morph - Change or type of form
# Objects can take on multiple forms and work in multiple ways

class boat:
    def __init__(self, speed, colour, type):
        self.speed = speed
        self.colour = colour
        self.type = type

    def move(self):
        return "*Slides through water*"

class plane:
    def __init__(self, speed, colour, type):
        self.speed = speed
        self.colour = colour
        self.type = type

    def move(self):
        return "*Glides through the sky*"

class car:
    def __init__(self, speed, colour, type):
        self.speed = speed
        self.colour = colour
        self.type = type

    def move(self):
        return "*Drives along the ground*"  

boat1 = boat(12, "grey", "Sail Boat")
plane1 = plane(156, "yellow", "Bi Plane")
car1 = car(140, "red", "Diesel")

# Polymorphism means objects can take on multiple forms 
# and interpreters (python) can accept multiple forms

vehicleList = [boat1, plane1, car1] 

# vehicle can be a boat, plane or car
for vehicle in vehicleList:
    print(vehicle.colour) # Accessing the colour of each type of vehicle
    print(vehicle.move())
