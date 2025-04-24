n, t, s = input().split()
n = int(n)
for i in range(n+1):
    if s == t:
        print(i)
        break
    s = s[1:] + s[0]