S = input()
T = input()
N = int(input())
answer = S[:N] + T + S[N:]
print(answer)