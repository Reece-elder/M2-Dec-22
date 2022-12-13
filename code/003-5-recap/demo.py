# What do I need to do if I want the user to input their favourite colour
# colour = input("Please enter your fav colour: ")

# print(colour)

# Create a conditional to print heads if heads is true or tails if heads is false
# Coneverted our input into a boolean
# heads = bool(input("Please enter Heads or tails"))

# if heads == True:
#     print("Heads!")
# else: 
#     print("Tails!")

# Conditional to check if input is greater than 10
# num = int(input("Please enter number: "))
# string = "orange"

# if num > 10:
#     print("Greater than 10")
# # I want the next line to trigger if num is equal to 10 AND string equal to orange
# if num == 10 and string == "orange":
#     print("Other task..")

# How can i short hand this code
tuesday = True

if tuesday:
    print("Its Tuesday!")
elif not tuesday:
    print("its not tuesday..")

# While Loops
# While loop to print 1 - 10 
counter = 1
while counter < 10:
    print(counter)
    counter = counter + 1

# For Loops
# For Loop to count from 30 to 7
for number in range(30, 7, -1):
    print(number)
