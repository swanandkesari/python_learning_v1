# Python Basics - Data Structures, and Functions



# ========== DATA TYPE: TUPLE ==========
# Tuples are ordered, immutable collections of items.
# "Immutable" means they cannot be changed after creation.

# Creating a tuple
coordinates = (10.0, 20.0)
print(f"Tuple: {coordinates}")

# Accessing elements (similar to lists)
print(f"X-coordinate: {coordinates[0]}")

# Tuples are useful for data that should not change, like days of the week or coordinates.
# Trying to change an element will cause an error:
# coordinates[0] = 15.0  # This would raise a TypeError

# ========== DATA TYPE: SET ==========
# Sets are unordered collections of unique items.
# They are useful for membership testing and eliminating duplicate entries.

# Creating a set from a list with duplicates
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)
print(f"Set of unique numbers: {unique_numbers}")

# Adding items to a set
unique_numbers.add(6)
print(f"Set after adding 6: {unique_numbers}")

# Checking for membership (this is very fast in sets)
if 3 in unique_numbers:
    print("3 is in the set.")

# ========== FUNCTIONS (WITH PARAMETERS AND RETURN) ==========
# Functions are blocks of reusable code.

# A function that takes parameters (arguments)
def greet(name, greeting="Hello"):
    """
    This function greets a person.
    It demonstrates parameters and a default value.
    """
    message = f"{greeting}, {name}!"
    print(message)

# Calling the function with different arguments
greet("Swanand")
greet("World", "Hi")

# A function that returns a value
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

# Calling the function and storing the returned value
sum_result = add(5, 3)
print(f"The sum is: {sum_result}")

# ========== MODULES ==========
# Modules are Python files with functions, classes, and variables that you can use in other files.
# The 'import' statement is used to bring a module's code into your script.

# 'math' is a standard library module for mathematical operations.
import math

# Using functions and constants from the math module
radius = 5
area = math.pi * (radius ** 2)
print(f"The area of a circle with radius {radius} is: {area:.2f}")

# You can also import specific items from a module
from math import sqrt

square_root_of_16 = sqrt(16)
print(f"The square root of 16 is: {square_root_of_16}")
