N = int(input())
A = map(int, input().split())
E = 0
O = 0
for i in A:
    if i % 2 == 0:
        E += 1
    else:
        O += 1
print(E, O)