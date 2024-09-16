# Input the number of apple cakes, orange cakes, and the sizes of the two bags
a = int(input())  # Number of apple cakes
b = int(input())  # Number of orange cakes
c = int(input())  # Size of the first bag
d = int(input())  # Size of the second bag

if (a <= c and b <= d) or (a <= d and b <= c):
    print("YES")
else:
    print("NO")