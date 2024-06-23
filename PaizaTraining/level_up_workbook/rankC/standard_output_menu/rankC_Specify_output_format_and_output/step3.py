list = ["="] * (2*9 + 3*8)
for i in range(1, 10):
    for j in range(1, 10):
        if j == 9:
            print ("{: >2}".format(i*j))
        else:
            print("{: >2}".format(i*j), end=" | ")
    if i < 9:
        print("".join(list))