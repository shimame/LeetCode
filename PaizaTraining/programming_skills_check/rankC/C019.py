q = int(input())
for _ in range(q):
    num = int(input())
    divisors = [i for i in range(1, num) if num % i == 0]
    if num == sum(divisors):
        print("perfect")
    elif abs(num - sum(divisors)) == 1:
        print("nearly")
    else:
        print("neither")