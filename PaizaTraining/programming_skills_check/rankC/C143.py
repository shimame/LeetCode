s = list(input())
count = 0
flag = True
ans = ""
for i in range(len(s)):
    if s[i] == "-" and flag:
        ans += s[i]
        flag = False
    elif s[i] != "-":
        ans += s[i]
        flag = True
print(ans)