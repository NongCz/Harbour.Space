s = input()

mid_index = len(s) // 2

reult = s[mid_index:] + s[:mid_index]

print(reult)