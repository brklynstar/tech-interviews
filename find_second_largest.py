#Question-
#Write a Python program to find the second largest number in a list without using the built-in sorted() function.

#Solution-

# define a function named find_second_largest that takes a single argument lst, which is a list of integers.
def find_second_largest(lst):
# initializes two variables named largest and second_largest to the first element of the input list lst and None
  largest = lst[0]
  second_largest = None
#uses a for loop to iterate through each element val in the input list lst starting from the second element.
#   For each element val, the program checks whether val is greater than largest
  for val in lst[1:]:

# If val is greater than largest, then the program updates the second_largest variable to be equal to the previous value of largest,
# and updates the largest variable to be equal to val.

    if val > largest:
      second_largest = largest
      largest = val
# If val is less than largest, the program then checks whether second_largest is None or if val is greater than second_largest
    elif val < largest:
      if second_largest is None or val > second_largest:
# If either of these conditions is true, then the program updates second_largest to be equal to val.
        second_largest = val
# After iterating through all the elements in the list lst, the program returns the final value of second_largest, which should be the second largest element in the list.
  return second_largest