input_line = input().split(" ")
N = float(input_line[0])
M = str(input_line[1])

Format = "{:." + M + "f}"

print(Format.format(N))


"""answer
values = input().split()
N = float(values[0])
M = int(values[1])

print("{:.{}f}".format(N, M))
"""