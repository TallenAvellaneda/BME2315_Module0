# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX 
Create variables for input and output
Create loop to sum all numbers in the sequence up to the input
Once the input value is reached, output the sum
XXX
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # set the index of the fibonacci number to sum to

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # created an iterative variable to count until the index is reached
total = 0 # created an output variable

while count < N: # loop until the index is reached
    total = total + b # adds the current fibonacci number to the total

    next_value = a + b # created a next value variable so that it can be stored in b
    a = b # sets a to the current fibonacci number so that in the next iteration it can be added to the next value
    b = next_value

    count = count + 1 # count is increased by 1 to keep track of the number of iterations

print(total) # outputs the sum following the completion of the loop

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
import numpy as np
np.std([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
# the standard deviation is 10.467091286503619
# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.
def SumFib(N): # created a function SubFib, essentially a copy the the code above with some new variable names
    a = 0
    b = 1
    i = 0
    sum = 0
    while(i < N):
        sum = sum + b
        nextval = a + b
        a = b
        b = nextval
        i = i + 1
    return sum # when SumFib is called, the sum is output in its place

print(SumFib(5)) # output of the sums of all numbers up to the index input
print(SumFib(10))
print(SumFib(15))
print(SumFib(20))
print(SumFib(25))
print(SumFib(30))

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 # removed quotes to make an int
    b = 1 # removed quotes to make an int
    index = 0 # created variable so that index is created as an int and can now be referenced later

    while a <= limit: # TypeError as a is a str and can't be compared with an int
        next_value = a + b
        a = b
        b = next_value
        index += 1 # UnboundLocalError due to index not being a created variable prior to being referenced

    return index


result = find_fib_above_limit(50) # TypeError due to the function being called
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0: # This line checks if the Fibonacci number is even
            total += b # if the number is even, it will be added to the total
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_even_fib(0))
print(sum_even_fib(-1))
print(sum_even_fib(10))
print(sum_even_fib(50))

# %%
