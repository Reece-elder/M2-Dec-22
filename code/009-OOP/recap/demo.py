# 4 OOP principles to work with

# Abstraction - Defining an object with its limitations and restrictions as an abstract 
# (you cannot create an object from an abstract class)

# Inheritance - A child object inherits the values and functions of a parent object

# Encapsulation - Keeping variables secure and keeping all necessary functions within the object
# Private variable : _pin - does absolutely nothing but tells the devs this should be a secure variable

# Polymorphism

# Make an object of a car

# Because Python is dynamically typed it shouldn't matter what the data type is unless it does matter
# Your code should be covered against unexpected data types separate to variable types 

class car:
    def __init__(self, wheels, colour, topSpeed, electric):
        self.wheels = wheels
        self.colour = colour
        self.topSpeed = topSpeed
        self.electric = electric

    def horn(self):
        return "*beep beep*"

# Child class of our parent class (car)
class tesla(car):
    def __init__(self, colour, topSpeed, soundEffects, chargingType):
        super().__init__(4, colour, topSpeed, True)
        self.soundEffects = soundEffects
        self.chargingType = chargingType

    def horn(self):
        return f"Horn Sound Effect: {self.soundEffects}"

car1 = car(3, "yellow", 54, False)
tesla1 = tesla("Cherry Red", 130, "Laser sounds", "EC2-A")
coolVar = "Hello!"
print(car1)
print(coolVar)
print(tesla1.colour)
# 0 1 2 3 4 5 - Common Number system (base 10)
# 0 1         - binary (base 2)
# 0 1 2 3.. 9 A B C D E F - Hexadecimal (base 16)

# Exercise Create a new python file that contains the following classes / objects
# - Parent abstract class with an abstract method
# - 1 x Child class that inherits the abstract method
# - Getter and Setter to access the fields of the child class, with some validation restriction
# setTitle(title) check title length is appropriate (greater than 5 chars but less than 40)