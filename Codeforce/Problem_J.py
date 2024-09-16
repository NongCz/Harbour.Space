the_number_of_minutes = int(input())
if 0 <= the_number_of_minutes < 1440:
    the_number_of_hours = the_number_of_minutes // 60
    the_number_of_minutes_remaining = the_number_of_minutes % 60
    print(the_number_of_hours,the_number_of_minutes_remaining)