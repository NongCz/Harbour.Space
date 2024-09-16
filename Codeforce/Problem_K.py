the_current_temperature = int(input())
if 1 <= the_current_temperature <= 50:
    if the_current_temperature > 35:
        print("CANCEL SCHOOL")
    elif the_current_temperature > 30:
        print("CANCEL TWO CLASSES")
    else:
        print("NORMAL CLASSES")