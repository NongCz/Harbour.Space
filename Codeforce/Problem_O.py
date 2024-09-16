# Input the number of left socks and right socks
n = int(input())
m = int(input())

# The maximum number of pairs is the minimum of the two sock counts
max_pairs = min(n, m)

print(max_pairs)