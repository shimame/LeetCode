n, r = map(int, input().split())
data = [int(input()) // r for _ in range(n)]
max_num = max(data)

for i in range(n):
    print(f"{i+1}:" + "*" * data[i] + "." * (max_num - data[i]))