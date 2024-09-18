s = input()

mid_index = len(s) // 2

before_mid_index = mid_index - 1

after_mid_index = mid_index + 1

result = s[before_mid_index] + s[mid_index] + s[after_mid_index]

print(result)