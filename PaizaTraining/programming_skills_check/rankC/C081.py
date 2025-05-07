n = int(input())
socks = {}
sum_pairs = 0

for _ in range(n):
    kind, part = input().split()
    if kind not in socks:
        socks[kind] = {"L": 0, "R": 0}
    socks[kind][part] += 1

for kind, part in socks.items():
    sum_pairs += min(part.values())

print(sum_pairs)