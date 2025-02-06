x = input()
count = 0
for day in range(365):
    if x in str(day):
        count += 1
print(count)