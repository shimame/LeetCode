win_numbers = [int(x) for x in input().split()]
N = int(input())
ans = []
for _ in range(N):
    nums = [int(y) for y in input().split()]
    """
    count = 0
    for n in nums:
        if n in win_numbers:
            count += 1
    """
    count = sum(1 for n in nums if n in win_numbers)
    ans.append(str(count))
print("\n".join(ans))