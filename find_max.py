# Question
# Write a Python program to find the maximum value in a list without using the built-in max() function.

# defines a function named find_max that takes a single argument lst, which is a list of integers
def find_max(lst):

#  initializes a variable named max_val to the first element of the list lst.

    max_val = lst[0]

# then iterates through each element val in the input list lst using a for loop.
# for each element val, the program checks whether val is greater than max_val. 

    for val in lst:
# If val is greater than max_val, then the program updates the max_val variable to be equal to val.
        if val > max_val:
            max_val = val
# After iterating through all the elements in the list lst, the program returns the final value of max_val,
# which should be the maximum element in the list.
    return max_val