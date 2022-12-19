# coollongvariablename = "hello everyone"
# booleanvariable = True
# def printtext(x):
#    return f"text added is {x}"
# print(printtext('Hello'))

# Check the quality of code with 'pylint'
# pip install pylint
# pip3 install pylint
# py install pylint (least likely to work)

# module docString Sits at the top of a file and tells the dev what the module is doing
"""
This allows us to make multiple line strings, that aren't associated to a variable
This is what is called a module docstring, and each module should have one talking about the file
"""

COOL_VAR = "hello everyone"
BOO_VAR = True
def printtext(text):
    """
    Function DocString which explains what the function does
    """
    return f"text added is {text}"
print(printtext('Hello')) # file should have a blank / final line at end of file
