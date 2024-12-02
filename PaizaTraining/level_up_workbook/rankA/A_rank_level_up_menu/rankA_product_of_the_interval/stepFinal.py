def multiplication(data):
    result = 1
    for i in data:
        result *= i
    return result

N, K = [int(x) for x in input().split()]
A = [int(n) for n in input().split()]

length = 10 ** 5
start, end = 0, 0

# しゃくとり法
while end < N and start <= end:
    if multiplication(A[start:end+1]) >= K:
        if end - start + 1 < length:
            length = end - start + 1
        start += 1
    elif A[end] == 0: # 0が含まれていた場合、0の次をスタートの位置とする。
        start = end + 1
        end += 1
    else:
        end += 1

print(length)