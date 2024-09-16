# Input the positive integer n
n = int(input())

# Check if the number is divisible by 7 and not divisible by 11
if n % 7 == 0 and n % 11 != 0:
    print("YES")
else:
    print("NO")