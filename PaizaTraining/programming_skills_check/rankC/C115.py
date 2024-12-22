n, m = [int(x) for x in input().split()]
traffic_jam_distance = 0
for _ in range(n-1):
    distance = int(input())
    if distance <= m:
        traffic_jam_distance += distance
print(traffic_jam_distance)