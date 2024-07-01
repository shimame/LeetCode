N = int(input())
A = [int(x) for x in input().split()]
set_A = list(set(A))
set_A.sort()
print(" ".join(map(str, set_A)))