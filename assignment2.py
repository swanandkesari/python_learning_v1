"""
Assignment2:
Write a Python program to find the number of ‘E’ in the string SELENIUM?
    Input : SELENIUM 
    Output: No. of Es in the string supplied are 2
"""
"""
###### Version 1######
InputString= "SELENIUM"
count = 0
for a in InputString:
    if(a == "E"):
        count=count+1
print( f'No. of Es in the string supplied are {count}')
"""
######  Version 2 ######
def count_e_in_string(input_string):
    """
    Counts the occurrences of the letter 'E' (case-insensitive) in the given string.

    Args:
        input_string (str): The string to search.

    Returns:
        int: The count of 'E' in the string.
    """
    # Convert the string to uppercase to handle case-insensitivity
    return input_string.upper().count('E')

# Get user input
input_string = input("Enter a string: ")

# Count occurrences of 'E'
e_count = count_e_in_string(input_string)

# Display the result
print(f"No. of Es in the string supplied are {e_count}")

#Sample test inputs:
#Apple
#Element
#Car
#1234
#12e4
