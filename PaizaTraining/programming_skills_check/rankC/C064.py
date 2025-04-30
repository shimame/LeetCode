m, n = map(int, input().split())
calories = [int(input()) for _ in range(m)]

for _ in range(n):
    volumes = list(map(int, input().split()))
    total_calories = 0
    for i in range(m):
        total_calories += calories[i] * volumes[i] // 100
    print(total_calories)