N = int(input())
s = []
a = []
for _ in range(N):
    s_i, a_i = input().split()
    a_i = int(a_i) + 1
    s.append(s_i)
    a.append(a_i)
for i in range(N):
    print(s[i], a[i])