# Inputs ALWAYS GENERATE STRINGS
# Cast your input as an int
grade = int(input("Please enter grade value: "))

if grade < 10 or grade > 100:
    print("Incorrect.. try again")

if grade < 50:
    print("FAILED!")
elif grade <= 60:
    print("Pass!")
elif grade <= 70:
    print("merit!")
else:
    print("Distinction!")