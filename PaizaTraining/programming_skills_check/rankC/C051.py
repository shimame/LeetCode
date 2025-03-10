cards = list(map(int, input().split()))
cards.sort()
num0 = cards[3] * 10 + cards[0]
num1 = cards[2] * 10 + cards[1]
print(num0+num1)