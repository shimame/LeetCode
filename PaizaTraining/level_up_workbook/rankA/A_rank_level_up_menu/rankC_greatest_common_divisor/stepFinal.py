import math

A, B = [int(x) for x in input().split()]
print(math.gcd(A, B))

"""別解
# ユークリッドの互助法
a, b = map(int, input().split())
def gcd(a,b): 
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(b,a%b))
"""