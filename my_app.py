# We need first to call our module "functions.py"

# Just for learning, I will use all the 3 ways below:

# First Way:
import functions
# We need to call our function: functions.find_factorial(x)

# Second Way:
from functions import *
# We can use: find_factorial(X)

# Third Way:
from functions import find_factorial

# Now we need to import colorama
# Importing the package "colorama":
# the link: https://pypi.org/project/colorama/
# you can use: Fore (foreground color) or Back (background color) or both
from colorama import Fore, Back


# The factorial of 5 is: 120
print("The factorial of 5 is:", functions.find_factorial(5))
print("The factorial of 7 is:", functions.find_factorial(7))

print("The factorial of 8 is:", find_factorial(8))

# Third Way:
print("The factorial of 9 is:", find_factorial(9))

print(Fore.LIGHTBLUE_EX+"The factorial of 3 is:", find_factorial(3))
print(Fore.GREEN+"The factorial of 4 is:", find_factorial(4))
print(Back.RED+"The factorial of 4 is:", find_factorial(6))
print(Fore.RESET + Back.RESET)
print("The factorial of 9 is:", find_factorial(20))
