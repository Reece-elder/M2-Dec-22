# Scientific calculator or not
# What colour the calculator is

class calculator:
    # Ctrl + ] indents everything to the right by 4 spaces

    def __init__(self, scientific, colour):
        self.scientific = scientific
        self.colour = colour

    # If self.scientific is true present the sums in 1.23x10^7
    def addSum(self, x, y):
        if self.scientific:
            return "1.24x10^7"
        else:
            return x + y

    def subSum(self, x, y):
        return x - y

    def multiplySum(self, x, y):
        return x * y

    def divideSum(self, x, y):
        return x / y

    def menu(self):
        print("""
            Press the chosen number to do that sum
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
        """)
        choice = input("Please enter choice: ")
        num1 = int(input("Please enter first number: "))
        num2 = int(input("Please enter second number: "))

        if choice == "1":
            return self.addSum(num1, num2)
        else:
            return self.subSum(num1, num2)

# Create my calculator
calc_science = calculator(True, "Dark Green")
calc_normal = calculator(False, "red")
print(calc_science.addSum(6,8))
print(calc_normal.addSum(6,8))