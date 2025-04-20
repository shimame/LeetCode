n, k = map(int, input().split())
bus_times = list(int(input()) for _ in range(n))
if k in bus_times:
    print(k)
else:
    min_time = k
    ans = []
    for i in range(n):
        if abs(bus_times[i] - k) < min_time:
            min_time = abs(bus_times[i] - k)
        
    if k - min_time in bus_times:
        ans.append(k - min_time)
    if k + min_time in bus_times:
        ans.append(k + min_time)
    print("\n".join(map(str, ans)))