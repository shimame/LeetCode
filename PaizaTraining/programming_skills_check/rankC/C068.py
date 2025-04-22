n = int(input())
s = input()
ans = []
for i in range(len(s)):
    if i % 2 == 0:
        cal = ord(s[i]) - n
        if cal < 65:
            cal += 26
    else:
        cal = ord(s[i]) + n
        if cal > 90:
            cal -= 26
    ans.append(chr(cal))
print("".join(ans))