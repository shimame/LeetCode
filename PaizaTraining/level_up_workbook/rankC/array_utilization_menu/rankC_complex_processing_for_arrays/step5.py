N, K, F = map(int, input().split())
A = [int(input()) for _ in range(K)]
waiting_line = []
del A[:F]
for i in A:
    if i not in waiting_line:
        waiting_line.append(i)
        print(i)