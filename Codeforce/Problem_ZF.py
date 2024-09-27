s = input()

is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("YES")
else:
    print("NO")