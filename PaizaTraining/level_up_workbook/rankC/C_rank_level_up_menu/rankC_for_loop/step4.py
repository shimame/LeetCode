m = int(input())
c = []
S = []
for _ in range(m):
    c.append(input())

n = int(input())

for _ in range(n):
    S.append(input())

for i in range(m):
    for j in range(n):
        if c[i] in S[j]:
            print("YES")
        else:
            print("NO")