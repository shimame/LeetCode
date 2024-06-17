input_line = input()
decimal_point = 0
for i in range(len(input_line)):
    if "." == input_line[i]:
        decimal_point = i

input_line = str(round(float(input_line), 3))

while len(input_line[decimal_point+1:]) < 3:
    input_line = input_line + '0'

print(input_line)


""" answer
N = float(input())
print("{:.3f}".format(N))
"""