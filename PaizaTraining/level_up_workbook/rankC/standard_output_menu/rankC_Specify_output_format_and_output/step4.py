input_line = input().split(" ")
H = int(input_line[0])
W = int(input_line[1])
A = int(input_line[2])
B = int(input_line[3])

for i in range(H):
    for j in range(W):
        if j == W - 1:
            print("({}, {})".format(A, B))
        else:
            print("({}, {})".format(A, B), end=" | ")
    if i < H - 1:
        print("=" * (6 * W + 3 * (W - 1)))