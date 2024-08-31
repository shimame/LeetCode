Q = int(input())
k = [int(input()) - 1 for _ in range(Q)]
fib = [0] * (max(k)+1)
fib[0], fib[1] = 1, 1

for i in range(2, max(k)+1):
    fib[i] = fib[i - 1] + fib[i - 2]

for j in k:
    print(fib[j])