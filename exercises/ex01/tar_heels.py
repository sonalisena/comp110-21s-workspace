"""An exercise in remainders and boolean logic."""

__author__ = "730392685"


# Begin your solution here...
number: int = int(input("Pick a random integer: "))

if number % 2 == 0 and number % 7 == 0:
    print("TAR HEELS")
else:
    if number % 2 == 0:
        print("TAR ")  
    else:
        if number % 7 == 0:
            print("HEELS ")
        else: 
            print("CAROLINA")
