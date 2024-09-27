# Input the number of elements n
n = int(input())

# Input the list of n integers
a = list(map(int, input().split()))

# Input the index k
k = int(input())

# Increase each element of the list by x
for i in range(n):
    a[i] += k

# Output the resulting list, space-separated
print(" ".join(map(str, a)))