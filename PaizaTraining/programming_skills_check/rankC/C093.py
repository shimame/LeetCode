x, y = input().split()

bob = 0
for i in x:
    bob += int(i)

alice = 0
for j in y:
    alice += int(j)

if bob >= 10:
    bob %= 10
if alice >= 10:
    alice %= 10

if bob == alice:
    print("Draw")
elif bob < alice:
    print("Alice")
else:
    print("Bob")