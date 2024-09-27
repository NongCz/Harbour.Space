# Input the number of elements n
n = int(input())

# Input the list of n integers
a = list(map(int, input().split()))

distinct_elements = []

for num in a:
    if num not in distinct_elements:
        distinct_elements.append(num)

print(len(distinct_elements))
