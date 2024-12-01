import math

N = int(input())
ans = "YES"
if N == 1:
    ans = "NO"
else:
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            ans = "NO"
            break
print(ans)