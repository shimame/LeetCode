h, w, n = [int(x) for x in input().split()]
A = [input() for _ in range(h*n)]
r, c = [int(y) for y in input().split()]
ans = ["" for _ in range(h * r)]

for row in range(r):
    b = [int(g) - 1 for g in input().split()]
    for j in range(h):
        current_row = []
        for k in range(c):
            # 文字列の連結は時間がかかるためlist型にし、joinする。
            # ans[i*h+j] += A[b[k] * h + j]
            current_row.append(A[b[k] * h + j])
        ans[row * h + j] = "".join(current_row)

print("\n".join(ans))