"""This program prompts the user to enter two integer values, then plugs in those
integers into numerical operators such as exponentiation, division, integer division, and remainder 'modulo'."""

__author__ = "730474583"

first_number: int = int(input("Left-hand side: "))
second_number: int = int(input("Right-hand side: "))

exponentiation: int = first_number ** second_number
div_w_decimal: float = first_number / second_number 
div_wo_decimal: int = first_number // second_number
remainder: int = first_number % second_number

print(str(first_number) + " ** " + str(second_number) + " is " + str(exponentiation))
print(str(first_number) + " / " + str(second_number) + " is " + str(div_w_decimal))
print(str(first_number) + " // " + str(second_number) + " is " + str(div_wo_decimal))
print(str(first_number) + " % " + str(second_number) + " is " + str(remainder))

