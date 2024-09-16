# Input the score
score = int(input())

# Determine the category based on the score
if 0 <= score <= 40:
    print("Emerging")
elif 41 <= score <= 80:
    print("Developing")
elif 81 <= score <= 100:
    print("Achieved")