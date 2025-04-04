n, x = map(int, input().split())
binary_num = list(bin(x))
del binary_num[0:2]

for _ in range(n):
    posi = len(binary_num) - int(input())
    print(binary_num[posi])