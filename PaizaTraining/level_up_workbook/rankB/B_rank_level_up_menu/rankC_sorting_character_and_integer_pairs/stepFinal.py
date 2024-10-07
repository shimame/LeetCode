n = int(input())
l = []
for _ in range(n):
    s, d = input().split()
    l.append((s, d))
l = sorted(l, key=lambda x: int(x[1]))
for s, d in l:
    print(s)