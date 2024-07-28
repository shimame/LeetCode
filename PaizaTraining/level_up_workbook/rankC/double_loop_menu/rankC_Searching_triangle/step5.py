x, y = 0, 0
while x != 24:
    if (x + y) % 15 == 0:
        print("FIZZBUZZ")
    elif (x + y) % 5 == 0:
        print("BUZZ")
    elif (x + y) % 3 == 0:
        print("FIZZ")
    else:
        print()
    y += 1
    if y == 60:
        x += 1
        y = 0