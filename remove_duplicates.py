#Question-
# Write a Python program to remove duplicates from a list without using built-in functions.

#Solution-

# defines a function named remove_duplicates that takes a single argument lst, which is a list. 
def remove_duplicates(lst):

# initializes an empty list unique_lst
    unique_lst = []
# iterates over each value in the input list lst using a for loop. For each value, 
# the program checks whether it is already in unique_lst using the not in operator.
    for val in lst:
# if the value is not in unique_lst, it is added to unique_lst using the append method
        if val not in unique_lst:
            unique_lst.append(val)
# function returns unique_lst containing only the unique values from the input list lst.
    return unique_lst