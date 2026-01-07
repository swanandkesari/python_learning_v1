"""
Assignment: Write a Python program to reverse any number:
    Input : 1234
    Output: 4321 
"""

def validate_number(input_value):
    """Validate if the input is a number (integer or float)."""
    try:
        float(input_value)  # Check if input can be converted to a float
        return True
    except ValueError:
        return False

# Get user input
input_number = input("Enter a number: ")

if not validate_number(input_number):
    print("Invalid input. Please enter a valid number.")
else:
    # Reverse the number as a string
    reversed_number = input_number[::-1]
    print(f"Reversed number: {reversed_number}")

# Example test cases:
# Input: 1234 -> Output: 4321
# Input: 45.67 -> Output: 76.54
# Input: aws234 -> Output: Invalid input