# Input the number of elements n
n = int(input())

# Input the list of n space-separated integers
a = list(map(int, input().split()))

# Check for adjacent elements with the same sign
for i in range(1, n):
    if a[i] * a[i - 1] > 0:
        print("YES")
        break
else:
    print("NO")
