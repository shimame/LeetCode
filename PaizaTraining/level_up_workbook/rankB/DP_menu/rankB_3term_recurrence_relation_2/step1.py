x, d, k = [int(x) for x in input().split()]
a = [0] * k
a[0] = x
for i in range(1, k):
    a[i] = a[i-1] + d
print(a[k-1])