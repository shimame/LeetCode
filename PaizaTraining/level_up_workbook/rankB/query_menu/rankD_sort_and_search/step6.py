N, K = [int(x) for x in input().split()]
students = {}
for _ in range(N):
    num, id = input().split()
    students[num] = id
for _ in range(K):
    num = input()
    print(students[num])