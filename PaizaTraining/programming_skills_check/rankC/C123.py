n = int(input())
ages = [int(input()) for _ in range(n)]
people = [0 for _ in range(n)]
flags = [0 for _ in range(n)]
m = int(input())

for _ in range(m):
    start, end, vol = [int(x) for x in input().split()]
    for i in range(start-1, end):
        if flags[i] == 0:
            people[i] += vol
            if people[i] > ages[i]:
                people[i] = ages[i]
                flags[i] = 1

print("\n".join(map(str, people)))