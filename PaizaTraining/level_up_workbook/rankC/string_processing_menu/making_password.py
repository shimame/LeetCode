N = int(input())
Q = int(input())
n = []
c = []
for _ in range(Q):
    n_i, c_i = input().split()
    n.append(int(n_i) - 1)
    c.append(c_i)
C = input()
answer = [C] * N
for i in range(Q):
    answer[n[i]] = c[i]
print("".join(answer))