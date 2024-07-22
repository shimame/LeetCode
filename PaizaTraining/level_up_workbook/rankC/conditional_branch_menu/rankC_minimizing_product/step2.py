N, A, B = map(int, input().split())
if (N + (A+B) == 0) | (N + (A-B) == 0) | (N - (A+B) == 0) | (N - (A-B) == 0):
    print("YES")
else:
    print("NO")