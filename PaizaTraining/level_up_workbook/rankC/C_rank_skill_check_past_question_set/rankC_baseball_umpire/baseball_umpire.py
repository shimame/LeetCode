N = int(input())
ball_counter = 0
strike_counter = 0
for _ in range(N):
    judge = input()
    if judge == "ball":
        ball_counter += 1
    elif judge == "strike":
        strike_counter += 1
    if ball_counter == 4:
        result = "fourball"
    elif strike_counter == 3:
        result = "out"
    else:
        result = judge
    print(result + "!")