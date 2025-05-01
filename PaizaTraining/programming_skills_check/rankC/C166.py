x = int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0
while x > 0:
    if x >= coins[0]:
        x -= coins[0]
        count += 1
    elif x >= coins[1]:
        x -= coins[1]
        count += 1
    elif x >= coins[2]:
        x -= coins[2]
        count += 1
    elif x >= coins[3]:
        x -= coins[3]
        count += 1
    elif x >= coins[4]:
        x -= coins[4]
        count += 1
    elif x >= coins[5]:
        x -= coins[5]
        count += 1
print(count)