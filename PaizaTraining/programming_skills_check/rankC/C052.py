h, w = map(int, input().split())
dy, dx = map(int, input().split())
print(w * dy + h * dx - dy * dx)