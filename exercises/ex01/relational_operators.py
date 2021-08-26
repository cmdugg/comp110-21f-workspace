"""This program prompts the user to enter two integer values and applys them to relational
operators such as less than, is at least, is equal to, and is not equal to."""

__author__ = "730474583"

first_number: int = int(input("Left-hand side: "))
second_number: int = int(input("Right-hand side: "))

less_than: bool = first_number < second_number
is_at_least: bool = first_number >= second_number
is_equal_to: bool = first_number == second_number
not_equal_to: bool = first_number != second_number

print(str(first_number) + " < " + str(second_number) + " is " + str(less_than))
print(str(first_number) + " >= " + str(second_number) + " is " + str(is_at_least))
print(str(first_number) + " == " + str(second_number) + " is " + str(is_equal_to))
print(str(first_number) + " != " + str(second_number) + " is " + str(not_equal_to))


