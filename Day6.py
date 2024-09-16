# Loops

# While loop
# Syntax
# while CONDITION:
#   Action

"""
number = 2
while number <= 20:
    print(number)
    number += 2
"""

""""
number = 1
while number <= 20:
    if number % 2 == 0:
        print(number)
    number += 1
"""

# break,continue,pass

# For loop
# range(start,stop,step)
# for variable_name in range(SOMETHING):
#   DO_SOMETHING

for number in range(1,11):
    square_of_numbers = number ** 2
    print(square_of_numbers)
