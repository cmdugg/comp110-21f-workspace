"""Repeating a beat in a loop."""

__author__ = "730474583"


# Begin your solution here...
counter: int = 0

beat = input("What beat do you want to repeat?")
b_repetitions = int(input("How many times do you want to repeat it?"))
if b_repetitions <= 0:
    print("No beat...")

while counter < b_repetitions:
    counter = counter + 1
    print(str(beat))