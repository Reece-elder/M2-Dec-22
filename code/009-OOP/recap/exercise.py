from abc import ABC, abstractmethod

class transport(ABC):

    # All child classes of Transport MUST include move()
    @abstractmethod
    def move():
        pass

class boat(transport):

    def __init__(self, speed, colour, type):
        self.speed = speed
        self.colour = colour
        self.type = type

    def move(self):
        return "*Slides through water*"

    # Getters and Setters - Allow us to Retrieve and modify fields with additional functionality

    
    def setColour(self, colour):
        colourList = ["purple", "cyan", "violet", "aquamarine", "green", "red"]
        if colour in colourList:
            self.colour = colour
            return f"Colour changed to: {colour}"
        else:
            return "Not acceptable colour!"


boatyMcBoatFace = boat(12, "white", "Fuel Powered")
print(boatyMcBoatFace.move())
print(boatyMcBoatFace.setColour("gold"))
print(boatyMcBoatFace.colour)
print(boatyMcBoatFace.setColour("purple"))
print(boatyMcBoatFace.colour)