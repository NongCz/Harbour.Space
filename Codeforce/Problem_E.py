number_apples = int(input())
number_students = int(input())
if 1 <= number_apples and number_students <= 1000:
    apple_per_student = number_apples // number_students
    print(apple_per_student)