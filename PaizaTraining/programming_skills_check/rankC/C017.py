de_f, de_s = [int(x) for x in input().split()]
n = int(input())
for _ in range(n):
    pl_f, pl_s = [int(y) for y in input().split()]
    if pl_f == de_f:
        if pl_s > de_s:
            judge = "win"
        else:
            judge = "lose"
    elif pl_f > de_f:
        judge = "lose"
    else:
        judge = "win"
    
    if judge == "win":
        print("High")
    else:
        print("Low")