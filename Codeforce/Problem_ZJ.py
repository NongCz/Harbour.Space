# Input the number of elements n
n = int(input())

# Input the list of n integers
a = list(map(int, input().split()))

a_even_positions = a[::2]

print(*a_even_positions)