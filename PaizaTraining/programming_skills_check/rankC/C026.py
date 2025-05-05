N, S, p = map(int, input().split())
max_vol = 0
num = 0
for i in range(1, N+1):
    m, s = map(int, input().split())
    if S - p <= s <= S + p and max_vol < m:
        max_vol = m
        num = i
if num == 0:
    print("not found")
else:
    print(num)