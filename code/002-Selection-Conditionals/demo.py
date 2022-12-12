# Selection / Conditionals
# If this is true, do this thing, else do this

buttonPressed = True

# Within most languages '=' assigning a value
# We are checking if buttonPressed is true, querying the variable '=='
if buttonPressed == True:    # if buttonPressed
    print("Button is pressed") # After the : any code that is indented is part of the True block
else:
    print("button is not pressed") # button is false if this runs

string = "red"
if string == "red":
    print("String is red")
else:
    print("String is not red")

chosen_num = 10

# if number is greater than x do this
if chosen_num > 10:
    print("Chosen num is greater than 10")
# Num is either equal to 10 OR less than 10
# else: 
#     print("Num is either equal to 10 OR less than 10")
elif chosen_num < 10:
    print("Chosen num is less than 10")
else:
    print("Num is equal to 10")

# Logical AND OR Nested Statements
shape = "square"
roundedCorner = True

# Will trigger if shape is square OR roundedcorner is True
if shape == "square" or roundedCorner == True:
    print("Shape is square or has rounded corners")
    # if shape == "square":
    #     # No new info
    #     print("Shape is square and could have rounded corners")
    if shape != "square":
        print("Shape is not square but must have rounded corners")
    elif not roundedCorner: # not says this is not true (false)
        print("Shape is square and not rounded corners")
    else:
        print("Shape is square AND roundedCorners is true")
else:
    print("Shape is not square and not got rounded corners")

# Triggers if both are true
if shape == "triangle" and roundedCorner:
    print("Both conditions are true")