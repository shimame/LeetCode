N, K = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]
i_counts = [0] + A
ans = []

for i in range(1, N+1):
    i_counts[i] += i_counts[i - 1]

for _ in range(K):
    A_l, A_r, B_l, B_r = map(int, input().split())
    A_pages = A_r - A_l + 1
    B_pages = B_r - B_l + 1
    A_sum = i_counts[A_r] - i_counts[A_l - 1]
    B_sum = i_counts[B_r] - i_counts[B_l - 1]

    if A_pages >= N/3:
        A_sum = -1
    if B_pages >= N/3:
        B_sum = -1

    if A_sum == B_sum:
        result = "DRAW"
    elif A_sum > B_sum:
        result = "A"
    elif A_sum < B_sum:
        result = "B"
    ans.append(result)

for i in ans:
    print(i)