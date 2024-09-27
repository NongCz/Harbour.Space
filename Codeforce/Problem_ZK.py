# Input the number of elements n
n = int(input())

# Input the list of n integers
a = list(map(int, input().split()))

b = list()

for i in range(n):
    if a[i] % 2 == 0:
        b.append(a[i])

print(*b)
        
