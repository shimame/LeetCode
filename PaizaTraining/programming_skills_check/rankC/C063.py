n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]
bloom_days = [0] * n
for i in range(n):
    bloom_days[i] = flowers[i][0] + flowers[i][1]

set_bloom_days = list(set(bloom_days))
set_bloom_days.sort(reverse=True)

max_count = 0
max_bloom_day = 0

for j in set_bloom_days:
    if max_count <= bloom_days.count(j):
        max_count = bloom_days.count(j)
        max_bloom_day = j
        
print(max_bloom_day)