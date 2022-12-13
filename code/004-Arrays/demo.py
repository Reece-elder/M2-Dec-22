# Arrays are ways of storing a variety of data to be used in other functions

# Lists
shapes = ["square", "triangle", "circle", "pentagon"]
print(shapes)    # whole array
print(shapes[2]) # Circle
print(shapes[-1])# pentagon (loops backwards)
shapes[2] = "rhombus"
print(shapes[2])

counter = 0
# Loops through the array and assigns the element to name 'shape'
for shape in shapes:
    # does the following to 'shape'
    print(shape)
    # Change all of the shapes to 'circle'
    shape = "circle" # Won't change the shape in the array as its a copy
    # shapes[counter] = "circle" 
    # counter += 1
print(shapes)

shapes.append("star") # Add star to the end
print(shapes)
shapes.remove("rhombus") # Removes this value
print(shapes)
print(len(shapes)) # Returns the length of an array

# Lists are dynamic and can contain ANY data type
cafe_order = [12, "John Cena", ["latte", "carrot cake"], True]
print(cafe_order)
print(cafe_order[1])    # "John Cena"
print(cafe_order[2][1]) # Carrot Cake - Multi Dimension Array

# Tuples - Ordered and cannot be modified once declared
colours_tuple = ("red", "green", "blue", "purple", 123, True)
print(colours_tuple[5])
# colours_tuple[4] = "567" - Can't modify our tuple after declaring it
# colours_tuple.append("star") - Doesnt support appending or removing either 

# Dictionaries - Key value pairs that share similar traits as a list
noises = {"key" : "value", "cow" : "moo", "duck" : "quack"}
print(noises) # Prints off the whole Dictionary
print(noises["cow"]) # Moo
noises["duck"] = "quacks don't echo"
noises["pig"] = "oink"
noises["number"] = 123
print(noises)

# Sets - Unordered mutable unique values
fruit_set = {"apple", "banana", "apple", "orange", "grapes", "apple", "banana", True}
print(fruit_set) # {True, 'apple', 'grapes', 'orange', 'banana'}

print("kiwi" in fruit_set) # returns true or false