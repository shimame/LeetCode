N, K = map(int, input().split())
rosters = {}
for _ in range(N):
    name, passcode, balance = input().split()
    rosters[name] = [passcode, int(balance)]

for _ in range(K):
    name, passcode, money = input().split()
    if rosters[name][0] == passcode:
        rosters[name][1] -= int(money)
for i in rosters:
    print(i, rosters[i][1])