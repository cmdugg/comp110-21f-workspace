"""Counting letters in a string."""

__author__ = "730474583"

# Your goal in this program is to allow the user to input two strings,
# a single letter to search for an arbitrary word, and then to print 
# out the number of times that letter appears in the word.

# Begin your solution here...
letter_choice = input("What letter do you want to search for?:")
word_choice = input("Enter a word:")

counter: int = 0
i: int = 0
while (i < len(word_choice)):
    if(word_choice[i] == letter_choice):
        counter = counter + 1
    i = i + 1
print("Count:" + str(counter))