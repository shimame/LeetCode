n = int(input())
heights = list(map(int, input().split()))
energy = 0
for i in range(n):
    height = heights[i]
    energy += -1 * height
    if energy < 0:
        break
if energy < 0:
    print("NO")
else:
    print("YES")