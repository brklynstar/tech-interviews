# Question:
# Write a Python program to count the number of vowels in a string

#Solution

# defines a function named count_vowels that takes a single argument string,
# which is the string in which we want to count the vowels
def count_vowels(string):
# initializes a string variable vowels with all the vowels in lowercase
  vowels = 'aeiou'
# initializes a variable count to 0 to keep track of the number of vowels in the string. 
  count = 0
# uses a for loop to iterate through each character char in the input string string.
# For each character char, the program checks whether it is a vowel by checking if 
# it is in the vowels string 
  for char in string:
# The lower() function is used to convert the character to lowercase, ensuring that 
# the program can correctly identify uppercase vowels as well
    if char.lower() in vowels:
# If the character is a vowel, the program increments the count variable by 1. 
      count += 1
# function returns the count variable, which contains the number of vowels in the input string.
  return count