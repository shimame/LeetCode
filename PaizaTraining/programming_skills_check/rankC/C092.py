n, a, b = map(int, input().split())
s_n = input()
s_a = input()
s_b = input()
posi_a, posi_b = 0, 0

for i in s_n:
    if posi_a < a and i == s_a[posi_a]:
        posi_a += 1
    if posi_b < b and i == s_b[posi_b]:
        posi_b += 1

print(a-posi_a, b-posi_b)