# Basic Python Function
# def <function name>():
# Functions ONLY run when they are triggered 
def greeting():
    print("Hello World")
    # This function returns nothing as we haven't specified what it returns
    return "This is my return"
    print("will this print..") # Won't ever print as its after return

# print(greeting()) # greeting() = "This is my return"

def helloWorld():
    return "Hello World!"

helloWorld() # Equivalent to just writing "Hello World" in the file
"Hello World!"
print(helloWorld())

# Parameter passing in
# everytime 'colour' appears in my code block it will be replaced with the value we pass in
def favColour(colour):
    return f"My fav colour is {colour}"

print(favColour("purple"))
print(favColour(123))

# We can pass ANY value (theoretically..) into a function.. including other functions
# Callback function 

def titleFunc(word):
    return word.title() # Making the word Title Case

def helloCallback(function):
    return f"Hello {function}, how are you?"

print(helloCallback(titleFunc("sinbad")))

# Scope - Variables defined INSIDE of a function are local to the function 
def sum(num1, num2):
    total = num1 + num2 # The variable total (which is the same thing) is local to this function
    return total  # the sum of num1 + num2 is being returned / outputted

total = sum(5,4)
print(sum(7, 10))
print(total)