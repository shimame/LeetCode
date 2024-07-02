A, B, C, D = map(int, input().split())
answer = pow(((A + B) * C), 2) % D
print(answer)