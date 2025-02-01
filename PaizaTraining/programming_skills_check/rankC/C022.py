n = int(input())
max_high = 0
min_low = 1000000
for i in range(n):
    start, end, high, low = [int(x) for x in input().split()]
    if i == 0:
        s = start
    if i == n - 1:
        e = end
    if max_high < high:
        max_high = high
    if min_low > low:
        min_low = low
print(s, e, max_high, min_low)