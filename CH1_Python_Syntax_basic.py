# Python Syntax Basics - Variables and Loops

# ========== VARIABLES ==========
# Variable assignment
name = "Swanand"
age = 25
height = 5.9
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3

# Type checking
print(type(name))
print(type(age))

# ========== STRING OPERATIONS ==========
# String concatenation
greeting = "Hello, " + name
print(greeting)

# F-strings (modern way)
message = f"My name is {name} and I'm {age} years old"
print(message)

# String methods
print(name.lower())
print(name.upper())

# ========== FOR LOOPS ==========
# Loop through range
for i in range(5):
    print(f"Count: {i}")

# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Loop with index
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

# ========== WHILE LOOPS ==========
count = 0
while count < 3:
    print(f"While loop: {count}")
    count += 1

# ========== LIST & COMPREHENSION ==========
numbers = [1, 2, 3, 4, 5]

# List comprehension
squares = [x**2 for x in numbers]
print(squares)

# Conditional comprehension
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# ========== DICTIONARIES ==========
student = {"name": "Swanand", "age": 25, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

# ========== LOOP CONTROL ==========
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 7:
        break     # Exit loop
    print(i)

# ========== ADDITIONAL TOPICS ==========

# Comments
# This is a single-line comment
"""
This is a multi-line comment
used for documentation.
"""

# Variable Scope
glob_x = 10  # Global variable

def scope_demo():
    loc_x = 5  # Local variable
    print(f"Local x: {loc_x}")

scope_demo()
print(f"Global x: {glob_x}")

# Constants
PI = 3.14159
GRAVITY = 9.8
print(f"PI: {PI}, GRAVITY: {GRAVITY}")

# Dynamic Typing
dyn_var = 10  # Integer
print(f"Type: {type(dyn_var)}")
dyn_var = "Hello"  # Now a string
print(f"Type: {type(dyn_var)}")

# Type Conversion
str_num = "123"
int_num = int(str_num)  # Convert string to integer
float_num = float(int_num)  # Convert integer to float
print(f"String: {str_num}, Int: {int_num}, Float: {float_num}")

# Augmented Assignment Operators
aug_x = 5
aug_x += 3  # aug_x = aug_x + 3
print(f"After += 3: {aug_x}")

# Unpacking Variables
a, b, c = 1, 2, 3
print(f"Unpacked: a={a}, b={b}, c={c}")

# Swapping Variables
swap_x, swap_y = 10, 20
swap_x, swap_y = swap_y, swap_x
print(f"After swap: x={swap_x}, y={swap_y}")

# Global and Nonlocal Keywords
nonlocal_x = 10

def outer():
    nonlocal_x = 5

    def inner():
        nonlocal nonlocal_x
        nonlocal_x = 15

    inner()
    print(f"After inner(): {nonlocal_x}")

outer()