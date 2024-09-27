s = input()

result = ""

for i in range(len(s)):
    result += s[i]
    if i != len(s) - 1:
        result += "_"

print(result)