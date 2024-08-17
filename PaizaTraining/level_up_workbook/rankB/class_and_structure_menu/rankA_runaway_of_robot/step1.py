class Point:
    def __init__(self, alphabet, root1, root2):
        self.alphabet = alphabet
        self.root1 = root1
        self.root2 = root2

N, K, S = [int(x) for x in input().split()]
roots = []
for _ in range(N):
    input_line = input().split()
    alphabet = input_line[0]
    root1 = int(input_line[1]) - 1
    root2 = int(input_line[2]) - 1
    root = Point(alphabet, root1, root2)
    roots.append(root)

current = roots[S - 1]
sentence = current.alphabet
for _ in range(K):
    select = input()
    if select == "1":
        next = current.root1
    elif select == "2":
        next = current.root2
    current = roots[next]
    sentence += current.alphabet
print(sentence)