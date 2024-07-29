max = 0
for x in range(100):
    for y in range(100 - x):
        if (x ** 3) + (y ** 3) < 100000 and max < (x * y):
            max = x * y
print(max)