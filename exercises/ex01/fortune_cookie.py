"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730392685"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
str = input("Your fortune cookie says...")

random_number: int = randint(1, 80)

if random_number < 20:
    print("A beautiful, smart, and loving person will be coming ")
    print("Now, go spread positive vibes! ")
else:
    if random_number == 21:
        print("Your life will be happy and peaceful. ")
        print("Now, go spread positive vibes! ")
    else:
        if random_number > 21:
            print("Soon life will become more interesting. ")
            print("Now, go spread positive vibes! ")
