the_number_of_intergers = int(input())
sum_of_numbers = the_number_of_intergers * (the_number_of_intergers + 1) // 2
sum_of_ai = 0
for i in range(the_number_of_intergers - 1):
    ai = int(input())
    sum_of_ai += ai
    the_number_of_missing_hero = sum_of_numbers - sum_of_ai
print(the_number_of_missing_hero)