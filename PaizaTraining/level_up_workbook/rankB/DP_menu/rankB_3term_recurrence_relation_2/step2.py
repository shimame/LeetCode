x, d = [int(x) for x in input().split()]
Q = int(input())
sequences = [0] * Q
for i in range(Q):
    num = int(input())
    sequences[i] = x + (num-1) * d
for j in sequences:
    print(j)