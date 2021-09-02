"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730474583"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune = (randint(1, 4))
print("Your fortune cookie says...")
if fortune == 1:
    print("You will make somebody's day amazing today!")
else:

    if fortune == 2:
        print("You will receive wonderful news very soon!")
    else:

        if fortune == 3:
            print("The tides of luck are in your favor!")
        else:

            if fortune == 4:
                print("Money will be making its way towards you very soon!")

print("Now, go spread positive vibes!")