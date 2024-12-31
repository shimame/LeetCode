n, m = [int(x) for x in input().split()]
current = (0, 0)
total_cost = 0
# 1番駅からのコスト
costs = [[int(c) for c in input().split()] for _ in range(n)]

# 経由する駅の数
x = int(input())

for _ in range(x):
    # r番路線s番駅を通る
    r, s = [int(y) - 1 for y in input().split()]
    if current[0] == r:
        total_cost += abs(costs[r][s] - costs[r][current[1]])
    elif current[1] == s:
        pass
    else:
        total_cost += abs(costs[r][current[1]] - costs[r][s])
    current = (r, s)

print(total_cost)