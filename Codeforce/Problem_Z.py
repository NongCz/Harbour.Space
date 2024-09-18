s = input()

a = input()

mid_index = len(s) // 2

result = s[:mid_index] + a + s[mid_index:]

print(result)