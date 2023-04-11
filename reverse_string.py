
# Question: Write a Python program to reverse a string without using built-in functions.




Finally, the function returns the reversed string reversed_string. This program effectively reverses the input string without using any built-in Python functions for string manipulation such as the reversed function or string slicing.

# This Python program defines a function named reverse_string
# takes a single argument string, which is the string to be reversed

def reverse_string(string): 

# The program then initializes a new string reversed_string as an empty string
# Use a for loop with a range function that starts from the index of the last
# character of the string, goes backwards by 1 until the first character,
# and includes each index in the loop. 

  reversed_string = ""
  
# For each index i in this range, the program appends the character at index i 
# of the original string string to the end of reversed_string.

  for i in range(len(string)-1, -1, -1):

    reversed_string += string[i]
# function returns the reversed string reversed_string. 

  return reversed_string
# This program effectively reverses the input string without
# using any built-in Python functions for string manipulation such as the reversed function or string slicing.