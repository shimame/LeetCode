N = int(input())
A = [int(x) for x in input().split()]
sum = 0
i = 0
while A[i] % 2 == 0:
    sum += A[i]
    i += 1

print(sum)

"""
11
28 30 60 65 44 52 36 36 16 6 42
"""