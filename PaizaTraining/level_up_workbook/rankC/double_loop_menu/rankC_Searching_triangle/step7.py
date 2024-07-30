X, Y, Z = map(int, input().split())
answer = Z
for i in range(Z // X + 1):
    for j in range(Z // Y + 1):
        if (i * X + j * Y) <= Z:
            one_coin = Z - i * X - j * Y
            if (i + j + one_coin) < answer:
                answer = i + j + one_coin
print(answer)