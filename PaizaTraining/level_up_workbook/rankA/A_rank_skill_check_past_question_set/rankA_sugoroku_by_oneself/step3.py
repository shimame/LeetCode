t, b, u, d, l, r = [int(x) for x in input().split()]
dice_dict = {t:"t", b:"b", u:"u", d:"d", l:"l", r:"r"}

for i in range(1, 7):
    if dice_dict[i] == "t":
        print(0)
    elif dice_dict[i] == "b":
        print(2)
    else:
        print(1)