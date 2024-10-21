N, M = [int(x) for x in input().split()]
max_earn = 0
if N == 0:
    print(0)
    exit()
for i in range(M):
    e = [int(x) for x in input().split()]
    s = sum(e)
    if s > 0:
        max_earn += s
print(max_earn)