"""
our descriptive docstring
"""

from random import randint

def rolllotsofdice():
    """
    our descriptive docstring
    """
    return randint(1,6)
print(rolllotsofdice())
def rolllotsofdice2():
    """
    our descriptive docstring
    """
    return randint(1,10,)
def rollcustonnumbersss(numberone, numbertwo,):
    """
    our descriptive docstring
    """

    return randint(numberone, numbertwo)
def checkrolls():
    """
    our descriptive docstring
    """
    if rolllotsofdice2() >= 6:
        return "big number!!!"
    return "small number :( "
    
CHECK_ROLLS = checkrolls()
print(CHECK_ROLLS)
LONG_VAR = """
this is a really long variable that is integral to the flow of the 
code, if this variable is to become any shorter the code will simply
fail as this is a fundamental piece of code for the really important 
and really resilient code base.. how many chars now??
"""
