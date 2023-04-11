#Question-
# Write a Python program to find the intersection of two lists without using the built-in set() function.


#Solution-

#defines a function named intersection that takes two arguments lst1 and lst2, 
# which are both lists of integers.
def intersection(lst1, lst2):
#initializes an empty list named intersect
  intersect = []
#uses a for loop to iterate through each element val in the first input list lst1.
  for val in lst1:
# For each element val, the program checks whether val is also in the second input list lst2,
# and whether val has not already been added to the intersect list.
# If both of these conditions are true, then the program adds val to the intersect list.
    if val in lst2 and val not in intersect:
      intersect.append(val)
# After iterating through all the elements in lst1, the program returns the final intersect list, 
# which contains all elements that are common to both input lists lst1 and lst2, with no duplicates.
  return intersect