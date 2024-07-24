H, W = map(int, input().split())
if (H == 0) | (W == 0):
    print("NO")
elif (H % 2 == 0) & (W % 2 == 0):
    print("YES")
else:
    print("NO")