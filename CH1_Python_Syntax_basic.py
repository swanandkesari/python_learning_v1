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