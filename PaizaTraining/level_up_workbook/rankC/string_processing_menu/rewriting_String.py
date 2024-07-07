S = input()
input_line = input().split()
i = int(input_line[0])
c = input_line[1]
S = S[:i-1] + c + S[i:]
print(S)