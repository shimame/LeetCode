n = int(input())
countrys = [list(map(int, input().split())) for _ in range(n)]
countrys.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
for i in range(n):
    print(" ".join(map(str, countrys[i])))