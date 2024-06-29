N = int(input())
#nums = list(map(int, input().split()))
nums = [int(x) for x in input().split()]
counts = [0 for _ in range(10)]
for i in nums:
    counts[i] += 1
print(" ".join(map(str, counts)))