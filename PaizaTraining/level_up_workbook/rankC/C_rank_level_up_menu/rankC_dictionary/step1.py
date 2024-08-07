n = int(input())
memo = []
for _ in range(n):
    memo.append(input().split())
S = input()
for i in memo:
    if S == i[0]:
        print(i[1])

"""answer
n = int(input())
zaisan = {}

for i in range(n):
    [s, a] = input().split()
    zaisan[s] = a

S = input()

print(zaisan[S])
"""