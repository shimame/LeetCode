N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = set(A + B)
print(" ".join(map(str, sorted(C))))