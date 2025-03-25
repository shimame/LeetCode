n = int(input())
stay_times = [int(input()) for _ in range(n)]
transfer_times = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
spots = [int(input()) - 1 for _ in range(k)]
total_time = stay_times[spots[0]]
for i in range(1, k):
    total_time += transfer_times[spots[i-1]][spots[i]]
    total_time += stay_times[spots[i]]
print(total_time)