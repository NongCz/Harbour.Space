# Input the number of gold coins in the three chests
a = int(input())
b = int(input())
c = int(input())

max_gold = max(a + b, a + c, b + c)

print(max_gold)