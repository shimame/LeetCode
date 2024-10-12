# n(座席数)とm(グループ数)
n, m = [int(x) for x in input().split()]
chairs = [0] * n
for i in range(m):
    # 整数a_i(グループの人数)とb_i(着席開始座席番号)
    a, b = [int(x) for x in input().split()]
    if b + a > n:
        front = b + a - n - 1
        if (chairs[:front] == [0] * (front)) and (chairs[b-1:] == [0] * (n-b+1)):
            chairs[:front] = [1] * front
            chairs[b-1:] = [1] * (n-b+1)
    elif chairs[b-1:b-1+a] == [0] * a:
        chairs[b-1:b-1+a] = [1] * a
print(sum(chairs))