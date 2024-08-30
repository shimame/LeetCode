x, d_1, d_2 = [int(x) for x in input().split()]
Q = int(input())
k = []
for _ in range(Q):
    k.append(int(input()))
sequences = [0] * (max(k)+1)
sequences[1] = x
for i in range(2, max(k)+1):
    if i % 2 == 0:
        sequences[i] = sequences[i-1] + d_2
    else:
        sequences[i] = sequences[i-1] + d_1

for j in k:
    print(sequences[j])