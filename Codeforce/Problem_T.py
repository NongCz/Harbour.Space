# Input the number of integers
n = int(input())

# Initialize a variable to store the sum
total_sum = 0

for _ in range(n):
    ai = int(input())
    total_sum += ai

print(total_sum)