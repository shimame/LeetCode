X = int(input())
F_1, F_2 = map(int, input().split())
L, N = map(int, input().split())
S = [0] + [int(x) for x in input().split()] + [L]
sum_fuel = 0
for i in range(1, N+2):
    distance = S[i] - S[i-1]
    if distance > X:
        distance -= X
        sum_fuel += F_1 * X + F_2 * distance
    else:
        sum_fuel += F_1 * distance
print(sum_fuel)