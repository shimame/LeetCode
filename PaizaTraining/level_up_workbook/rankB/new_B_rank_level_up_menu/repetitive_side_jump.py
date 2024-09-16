N, X, K = [int(x) for x in input().split()]
l = 0
count = K // 4 - N
if K % 4 == 3:
    count += 0.5
print(int(count*X*2))