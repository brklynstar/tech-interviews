
# Question:
# Write a Python program to check whether a given number is prime or not.

# Define a function is_prime that takes a single arugement n,
# which is the number to be tested
def is_prime(n):
# first checks if the input number n is less than 2. If n is less than 2,
# then it cannot be prime, so the function returns False.
  if n < 2:
    return False
# If n is greater than or equal to 2, the program enters a for loop that iterates 
# from 2 to the square root of n (inclusive) using the range function.
# The loop variable i represents each potential factor of n.
  for i in range(2, int(n ** 0.5) + 1):
# For each value of i, the program checks whether n is divisible by i using the modulo operator %.
# If n is divisible by i, then n cannot be prime, so the function returns False.
    if n % i == 0:
      return False
# If the loop completes without finding a factor of n, then n must be prime, so the function returns True.
  return True