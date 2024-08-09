p, q, r = map(int, input().split())
A = []
A_to_B = {}
B_to_C = {}
for _ in range(p):
    a, b = input().split()
    A_to_B[a] = b
    A.append(a)
for _ in range(q):
    b, c = input().split()
    B_to_C[b] = c
A.sort()
for i in A:
    print(i, B_to_C[A_to_B[i]])