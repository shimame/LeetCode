N = int(input())
count = 0
for i in range(2, N+1):
    prime_judge = 0
    for j in range(2, i):
        if i % j == 0:
            prime_judge = 1
    if prime_judge == 0:
        print(f"i = {i}")
        count += 1
print(count)