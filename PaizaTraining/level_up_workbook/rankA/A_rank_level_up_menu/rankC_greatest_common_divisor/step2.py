# 繰り返し二乗法 x^n
N = int(input())
m = 1000003
x = 2
ans = 1
while 0 < N:
    if N & 1 == 1: # ビット列の一番右（最小）に1がたっていた場合
        ans = ans * x % m
    x = x * x % m
    N >>= 1 # 右に1シフト（指数の位置を一つずらす）1011 -> 0101
print(ans)