start = int(input())
stop = int(input())
if start % 2 != 0:
    start += 1
for i in range(start, stop + 1, 2):
    print(i)
