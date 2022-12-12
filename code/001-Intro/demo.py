# Adding a comment with #
# Some code / text that is there for documentation, the interpreter (Python) will not read this
# print("Hello!")

# ls - List stuff, lists the directory -a to show hidden files
# cd - change directory cd .. back a folder, cd <folder name> to go to that folder
# python <name of file> - runs the file

# Pythons basic Control Flow is Top to Bottom of the file (module) we run
print("Hello World")
print(5)
print(3)
print(4)
print(6)

# Python is dynamically typed - We don't need to specify data types
# Within python there are basic data types, simplest or most common data type 

decorated = True # Boolean could also be False
price = 8.50 # float non whole number
flavour = "Black Forest" # string a text is an array of chars
rating = "B" # Char, which is a single character
tiers = 2 # int a whole number

# array - Collection of data, same data types or different (depending on type of array)
decorations = ["cherries", "choc shavings", "cream"] # list - type of array, collection of strings

# Within ALL (typically) languages variables are used as *Placeholders*
print("Blue Forest") # The flavour of cake
print(flavour)

print(tiers)
print(price * tiers) # What they expect this would be?
# print(flavour + tiers) # Trying to add a string to an int.. Will Error
print(flavour + rating)

print(decorations) # ['cherries', 'choc shavings', 'cream']
# arrays are indexed starting from 0 - cherries is in the 0th position, cream is in the 2nd index position
print(decorations[1]) # prints off the 1st index of our array

# Python has inbuilt very simple ways of letting the user enter data
colour = input("Please enter your fav colour: ")
print(colour)

# We can cast data types by wrapping the input in a casting function
number = int(input("Enter your fav number: "))
print(number + 5) # this fails if its a string

whippedCream = bool(input("Do you want whipped cream: "))
print(whippedCream)