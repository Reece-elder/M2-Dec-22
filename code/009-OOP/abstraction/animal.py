
# Abstract class it must inherit Abstract functionality
# Importing ABC and abstractmethod from abc (abstract base class) inbuilt library
from abc import ABC, abstractmethod

class animal(ABC):
    # because this is an abstract class, we can't create objects from it.. no need for a constructor
    size = 0
    name = ""
    # Abstract method for rest
    @abstractmethod  # Descriptor telling Python this function is abstract
    def rest(self, hours):
        pass # Every child MUST INCLUDE THE FUNCTION rest(self, hours) pass = does nothing 

class cat(animal):

    def __init__(self, fur_colour, fav_food, size, name):
        self.fur_colour = fur_colour
        self.fav_food = fav_food
        self.size = size
        self.name = name

    # Overriding our abstract method
    def rest(self, hours):
        return f"Sleeps for {hours}"

zaph = cat("Browny, blacky, beigey", "chicken sticks", "chonky", "zaph")
print(zaph.name)
print(zaph.rest(12))

