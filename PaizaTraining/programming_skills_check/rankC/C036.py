versus = [list(map(int, input().split())) for _ in range(2)]
times = list(map(int, input().split()))
f_versus = []

for i in range(2):
    p1, p2 = versus[i][0] - 1, versus[i][1] - 1
    if times[p1] < times[p2]:
        f_versus.append(p1 + 1)
    else:
        f_versus.append(p2 + 1)
        
f_versus.sort()
t0, t1 = map(int, input().split())
if t0 < t1:
    print("\n".join(map(str, f_versus)))
else:
    print("\n".join(map(str, f_versus[::-1])))