n, r = [int(x) for x in input().split()]
ans = []
for i in range(1, n+1):
    h, w, d = [int(y) for y in input().split()]
    if h >= 2*r and w >= 2*r and d >= 2*r:
        ans.append(str(i))
print("\n".join(ans))