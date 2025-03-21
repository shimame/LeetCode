n = int(input())
result_map = [[""] * n for _ in range(n)]

for i in range(n):
    result_map[i][i] = "-"
for _ in range((n * (n-1)) // 2):
    win, lose = map(int, input().split())
    result_map[win-1][lose-1] = "W"
    result_map[lose-1][win-1] = "L"

for j in result_map:
    print(" ".join(j))