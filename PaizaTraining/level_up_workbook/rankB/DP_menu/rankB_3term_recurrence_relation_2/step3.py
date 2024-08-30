x, d_1, d_2, k = [int(x) for x in input().split()]
sequences = [0] * k
sequences[0] = x
for i in range(1, k):
    if (i - 1) % 2 == 0:
        sequences[i] = sequences[i-1] + d_2
    else:
        sequences[i] = sequences[i-1] + d_1

print(sequences[k-1])