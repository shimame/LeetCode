N, K = [int(x) for x in input().split()]
a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]
c = [int(input()) for _ in range(N)]
min_a_average = 19
min_b_average = 19
min_c_average = 19

for i in range(N-K+1):
    a_average = sum(a[i:i+K]) / K
    b_average = sum(b[i:i+K]) / K
    c_average = sum(c[i:i+K]) / K

    if a_average < min_a_average:
        min_a_average = a_average
    if b_average < min_b_average:
        min_b_average = b_average
    if c_average < min_c_average:
        min_c_average = c_average

min_num = min(min_a_average, min_b_average, min_c_average)

if min_num == min_a_average:
    print(1)
elif min_num == min_b_average:
    print(2)
elif min_num == min_c_average:
    print(3)