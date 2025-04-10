t = int(input())
eat_melon = 0
time = 0
for _ in range(t):
    sushi = input()
    if time > 0:
        time -= 1
    else:
        if sushi == "melon":
            eat_melon += 1
            time = 10
print(eat_melon)