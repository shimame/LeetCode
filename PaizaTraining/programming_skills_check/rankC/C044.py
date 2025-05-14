n = int(input())
hands = [input() for _ in range(n)]
kind = list(set(hands))
kind.sort()

if len(kind) == 2:
    if kind[0] == "paper" and kind[1] == "scissors":
        print(kind[1])
    else:
        print(kind[0])
else:
    print("draw")