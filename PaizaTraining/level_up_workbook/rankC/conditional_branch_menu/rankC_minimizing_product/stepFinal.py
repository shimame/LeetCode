A, B = map(int, input().split())

if A > 0:
    print(A * A)
elif A < 0 and B < 0:
    print(B * B)
elif A <= 0 and B >= 0:
    print(A * B)