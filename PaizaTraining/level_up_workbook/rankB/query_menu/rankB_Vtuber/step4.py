N, K = map(int, input().split())
records = {input(): [] for _ in range(N)}
for i in range(K):
    name, num, money = input().split()
    records[name].append((num, money))

for name in records:
    print(name)
    for num, money in records[name]:
        print(num, money)
    print("-----")