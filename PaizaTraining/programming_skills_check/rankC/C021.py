xc, yc, r_1, r_2 = [int(a) for a in input().split()]
n = int(input())
ans = []
for _ in range(n):
    x, y = [int(b) for b in input().split()]
    cal = (x - xc) ** 2 + (y - yc) ** 2
    if r_1**2 <= cal <= r_2**2:
        ans.append("yes")
    else:
        ans.append("no")
print("\n".join(ans))