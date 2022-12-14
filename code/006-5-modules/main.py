# This is the main file we will run, it will import other files into it

# Tell Main I want to run the Hello function in Hello.py
import hello # Importing the entire hello.py module
import math # Be wary of existing inbuilt libraries

# import colours - Every function I run requires me to specify the module
from colours import turnToRed, shape
from colours import * # Imports EVERYTHING from the module 

print(hello.helloWorld())
# print(math.itsMaths())

print(turnToRed("purple"))
print(shape)