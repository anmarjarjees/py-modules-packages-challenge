# A function about math formula named "Factorial":
# The factorial function (symbol: !) says to multiply all whole numbers
# from our chosen number down to 1.
# Examples of "factorial":
# 5! = 5 * 4 * 3 * 2 * 1
# 3! = 3 * 2 * 1
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
# OR:
# 5! = 1 * 2 * 3 * 4 * 5
# n! = n * (n-1)

# 1! = 1
# 0! = ?
# Note: the factorial of 0 is 1
# The factorial of 0 is 1, or in symbols, 0! = 1.

# Create a function for this factorial formula
# This function:
# 1) needs to have a numeric positive value to be passed
# 2) should "return" the factorial of that positive value

# num is the parameter to accept an argument (the number)
# We can set a default value of 0
def find_factorial(num=0):
    """
    - accepts a numeric integer value 
    - returns the factorial of this value
    """
    # starting my code against a numeric value
    # For Loop: for x in range(1,num+1)
    # Any loop: the initial value for the loop counter and the condition to keep my loop

    # Let's take the number 5 as an example:
    # 5! = 5 * 4 * 3 * 2 * 1 * => we need to stop the loop with the value of 0
    # Or:
    # 5! = 1 * 2 * 3 * 4 * 5 => we need to stop the loop with the value of 6

    # Let's use this formula: 5! = 5 * 4 * 3 * 2 * 1
    # count is our while loop counter with initial value of any number that we pass to this function
    count = num
    # We need to keep looping while count still more than 0:
    # either count > 0 OR count >= 1
    factorial = 1
    # or like JS:  while (count > 0):
    while count > 0:  # this is the condition to keep looping while x is greater than or equal to 1
        # Just for testing:
        # print(count) # the count values printed in vertical layout: 5 4 3 2 1

        # the Python code for the factorial formula:
        factorial = factorial * count

        # decrement the loop counter by 1:
        count -= 1  # in JS we can write count--
        # or using the long syntax:
        # count = count - 1

    # The last thing:
    # This function should ONLY return the result of the factorial (no printing)
    return factorial


# print(find_factorial(5))  # 120
# result = find_factorial(5) # 5 + 4 + 3 + 2 + 1
# print(result)

# And yes you can add more functions of you want

# The normal step after:
# Create the virtual environment
# Activate it
# Install the required package
# pip list => show us all the installed packages
