A, B, C, D = map(int, input().split())
answer = int(((A | B) & C) ^ D)
print(answer)