#Question-
# Write a Python program to check if a string is a palindrome (reads the same forwards and backwards) without using string slicing.


# Solution-

# Define a function called is_palindrome that takes in argument s, which is a string.
def is_palindrome(s):
#uses a for loop to iterate through the first half of the input string s. 
#For each character in the first half of the string, 
#the program checks whether the corresponding character in the second half of the string is the same.
  for i in range(len(s)//2):
# if any pair of characters does not match, the function immediately returns False to indicate that the input string is not a palindrome.
    if s[i] != s[-1-i]:
      return False
# Otherwise, if all pairs of characters match, the function returns True to indicate that the input string is a palindrome.
  return True
