N = int(input())
if N % 15 == 0:
    print("FizzBuzz")
elif N % 5 == 0:
    print("Buzz")
elif N % 3 == 0:
    print("Fizz")
else:
    print(N)