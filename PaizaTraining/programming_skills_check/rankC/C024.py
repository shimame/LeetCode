n = int(input())
variables = [0, 0]

for _ in range(n):
    input_line = input().split()
    if input_line[0] == "SET":
        variables[int(input_line[1]) - 1] = int(input_line[2])
    elif input_line[0] == "ADD":
        variables[1] = variables[0] + int(input_line[1])
    elif input_line[0] == "SUB":
        variables[1] = variables[0] - int(input_line[1])

print(" ".join(map(str, variables)))