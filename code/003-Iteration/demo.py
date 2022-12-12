# Iteration - Repeating a block of code until a condition is no longer true

# While Loop
counter = 1

while counter < 10:
    # fStrings allow you to easily add vars to strings by surrounding in {}
    print(f"Value of counter: {str(counter)}")
    counter += 1 # Incrementing counter by 1 

print("Happens after the while loop")

while counter > 0:
    print(f"Value of counter: {str(counter)}")
    counter -= 1 # counter = counter - 1

    # Stop the loop when it gets to 4
    if counter == 4:
        break # Break as a command sits in a loop and stops the loop from running

# For Loops - Work well when using range()
print("***********************************")
print(range(5))          # What the range is, what the list is
print(*range(5))         # raw value of the list and easy to see
print(*range(2, 12))     # Starting and Ending values
print(*range(10, 0, -1)) # Starting, ending and increment value
print(*range(37, 90, 4)) # Range command to start from 37, end at 89 increasing by 4

# Create a loop to run 15 times
# For every element in range(15) (0 - 15 list)
for x in range(15):
    print(x)

for x in range(20, 3, -3):
    print(f"Value of x: {x}")

print("===========================")
# Nested loop
for x in range(10):
    for y in range(10):
        print(f"x: {x}")
        print(f"y: {y}")
    print("x loop ends")