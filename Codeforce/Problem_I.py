the_current_number_of_magical_flowers = int(input())
the_number_of_days = int(input())
if 1 <= the_current_number_of_magical_flowers <= 100:
    1 <= the_number_of_days <= 10
    the_number_of_magical_flowers = the_current_number_of_magical_flowers * (3 ** the_number_of_days)
    print(the_number_of_magical_flowers)
