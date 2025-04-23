s = input()
num = ""
ans = []
for i in range(len(s)):
    if ord(s[i]) >= 65:
        cal = ord(s[i]) + 1
        if num != "":
            ans.append(str(int(num) + 1))
            num = ""
        if cal > 90:
            cal -= 26
        ans.append(chr(cal))
    else:
        num += s[i]
if num != "":
    ans.append(str(int(num) + 1))
print("".join(ans))