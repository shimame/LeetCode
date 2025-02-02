n = int(input())
cards = input().split()
zero_flag = False
ten_flag = False

if "0" in cards:
    cards.remove("0")
    zero_flag = True
    
if "x10" in cards:
    cards.remove("x10")
    ten_flag = True

cards = list(map(int, cards))
ans = sum(cards)

if zero_flag:
    ans -= max(cards)

if ten_flag:
    ans *= 10

print(ans)