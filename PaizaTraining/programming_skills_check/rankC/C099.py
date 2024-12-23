n, d = [int(x) for x in input().split()]
overlap_range = [int(input()) for _ in range(n-1)]
print(d * (d * n - sum(overlap_range)))