### Variables:
#### Do's:
- Use descriptive and meaningful variable names.
  Example:
  ```python
  total_price = 100
  ```
- Use snake_case for variable names (e.g., `user_name`, `total_price`).
- Use constants for values that don’t change, and name them in uppercase.
  Example:
  ```python
  PI = 3.14159
  ```
- Loosely typed language; no need for a keyword, just declare a variable.
  Example:
  ```python
  name = "Swanand"
  age = 25
  ```
- Multiple assignment is possible (e.g., `x, y, z = 1, 2, 3`).
  Example:
  ```python
  x, y, z = 1, 2, 3
  ```
- Use `type(variable)` to check the type of a variable.
  Example:
  ```python
  print(type(name))
  print(type(age))
  ```

#### Don'ts:
- Avoid single-letter variable names unless in loops (e.g., `i`, `j`).
- Don’t overwrite built-in names like `list`, `str`, `int`.
- Don’t use keywords as variable names.

---

### String Operations:
#### Do's:
- Use f-strings for string formatting (modern and efficient).
  Example:
  ```python
  name = "Swanand"
  print(f"Hello, {name}")
  ```
- String concatenation: `"Hello, " + name`.
  Example:
  ```python
  greeting = "Hello, " + name
  print(greeting)
  ```
- String methods: `.lower()`, `.upper()`.
  Example:
  ```python
  print(name.lower())
  print(name.upper())
  ```

#### Don'ts:
- Avoid concatenating strings in a loop; use `.join()` for better performance.
  Example:
  ```python
  # Inefficient
  result = ""
  for word in words:
      result += word

  # Efficient
  result = "".join(words)
  ```

---

### Loops:
#### Do's:
- Use `enumerate()` when you need both the index and the value in a loop.
  Example:
  ```python
  for idx, value in enumerate(my_list):
      print(idx, value)
  ```
- Use list comprehensions for simple transformations.
  Example:
  ```python
  squares = [x**2 for x in range(10)]
  ```
- Loop through a range: `for i in range(5):`.
  Example:
  ```python
  for i in range(5):
      print(f"Count: {i}")
  ```
- Loop through a list: `for fruit in fruits:`.
  Example:
  ```python
  fruits = ["apple", "banana", "cherry"]
  for fruit in fruits:
      print(f"Fruit: {fruit}")
  ```
- Loop with index: `for idx, fruit in enumerate(fruits):`.
  Example:
  ```python
  for idx, fruit in enumerate(fruits):
      print(f"{idx}: {fruit}")
  ```
- Use `while` loops when the number of iterations is not known beforehand.
  Example:
  ```python
  count = 0
  while count < 3:
      print(f"While loop: {count}")
      count += 1
  ```

#### Don'ts:
- Avoid infinite loops unless absolutely necessary.
- Don’t modify a list while iterating over it. Instead, create a new list.

---

### List Comprehension:
#### Do's:
- Use list comprehensions for concise and readable code.
  Example:
  ```python
  squares = [x**2 for x in range(10)]
  ```
- Conditional comprehension: `[x for x in numbers if x % 2 == 0]`.
  Example:
  ```python
  evens = [x for x in numbers if x % 2 == 0]
  print(evens)
  ```

#### Don'ts:
- Avoid using list comprehensions for complex logic; use regular loops for clarity.

---

### Dictionaries:
#### Do's:
- Use `.get()` to safely access dictionary values.
  Example:
  ```python
  value = my_dict.get("key", "default_value")
  ```
- Use descriptive keys for clarity.
- Loop through dictionary: `for key, value in student.items():`.
  Example:
  ```python
  student = {"name": "Swanand", "age": 25, "grade": "A"}
  for key, value in student.items():
      print(f"{key}: {value}")
  ```

#### Don'ts:
- Avoid using mutable types (e.g., lists) as dictionary keys.

---

### Loop Control:
#### Do's:
- Use `break` and `continue` sparingly to avoid confusing logic.
- Use `else` with loops when appropriate.
  Example:
  ```python
  for i in range(5):
      if i == 3:
          break
  else:
      print("Loop completed without break")
  ```

#### Don'ts:
- Avoid deeply nested loops; refactor into functions if necessary.

---

### Additional Topics for Python Syntax and Variables:

#### Comments:
- Use single-line (`#`) and multi-line comments (`"""` or `'''`).
  Example:
  ```python
  # This is a single-line comment
  """
  This is a multi-line comment
  used for documentation.
  """
  ```

#### Variable Scope:
- Local vs Global variables.
  Example:
  ```python
  x = 10  # Global variable

  def my_function():
      x = 5  # Local variable
      print(x)

  my_function()
  print(x)
  ```

#### Constants:
- Use uppercase variable names for constants.
  Example:
  ```python
  PI = 3.14159
  GRAVITY = 9.8
  ```

#### Dynamic Typing:
- Variables can change types.
  Example:
  ```python
  x = 10  # Integer
  x = "Hello"  # Now a string
  ```

#### Type Conversion:
- Convert between data types using `int()`, `float()`, `str()`, etc.
  Example:
  ```python
  x = "123"
  y = int(x)  # Convert string to integer
  z = float(y)  # Convert integer to float
  ```

#### Augmented Assignment Operators:
- Operators like `+=`, `-=`, `*=`, `/=`.
  Example:
  ```python
  x = 5
  x += 3  # x = x + 3
  print(x)  # Output: 8
  ```

#### Reserved Keywords:
- Python's reserved keywords cannot be used as variable names.
  Example:
  ```python
  # This will raise a SyntaxError
  if = 10
  ```

#### Unpacking Variables:
- Unpack lists or tuples into variables.
  Example:
  ```python
  a, b, c = 1, 2, 3
  print(a, b, c)
  ```

#### Swapping Variables:
- Swap variables without a temporary variable.
  Example:
  ```python
  x, y = 10, 20
  x, y = y, x
  print(x, y)  # Output: 20, 10
  ```

#### Global and Nonlocal Keywords:
- Modify variables in different scopes.
  Example:
  ```python
  x = 10

  def outer():
      x = 5

      def inner():
          nonlocal x
          x = 15

      inner()
      print(x)  # Output: 15

  outer()
  ```