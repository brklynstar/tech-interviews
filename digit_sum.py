#Question-
# Write a Python program to find the sum of the digits of a positive integer.

#Solution-

#Define a function called digit_sum that takes in a single argument n
#which is a positive integar
def digit_sum(n):
# initializes a variable named total to 0. 
  total = 0
# uses a while loop to repeatedly add the rightmost digit of the input integer n
# to the total variable, and then removes the rightmost digit of n. 
# this process continues until all the digits in n have been added to total.
  while n > 0:
    total += n % 10
    n //= 10
# returns the total sum of all digits in the input integer n.
  return total
