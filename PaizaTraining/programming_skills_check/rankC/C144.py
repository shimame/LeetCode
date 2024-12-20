n = int(input())
win_count = 0
for _ in range(n):
    a, b = input().split()
    if (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        win_count += 1
print(win_count)