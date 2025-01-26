n = int(input())
s1 = input()
s2 = input()
flag = False
for i in range(n):
    if s1 == s2:
        flag = True
        break
    else:
        s2 = s2[-1] + s2[:-1]
if flag:
    print("Yes")
else:
    print("No")