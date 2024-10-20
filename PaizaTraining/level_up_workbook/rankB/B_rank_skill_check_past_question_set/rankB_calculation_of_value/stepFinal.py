N = int(input())
dic = {}
for _ in range(N):
    s, w = input().split()
    dic[s] = int(w)

M = int(input())
root = input().split()
cir_resi = 0

for i in root:
    if len(i) == 1:
        cir_resi += dic[i]
    else:
        den = 0
        for j in i:
            den += 1 / dic[j]
        cir_resi += 1 / den
print(int(cir_resi))