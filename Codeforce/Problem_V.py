the_number_of_integers = int(input())
number_of_zeros = 0
for i in range(the_number_of_integers):
    ai = int(input())
    if ai == 0:
        number_of_zeros += 1
print(number_of_zeros)
