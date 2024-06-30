N = int(input())
S = list(input())
alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
counts = [0] * len(alphabets)
for i in S:
    counts[ord(i) - ord('a')] += 1
print(" ".join(map(str, counts)))


"""answer
N = int(input())
S = input()

count = {chr(x): 0 for x in range(ord("a"), ord("z")+1)}
for char in S:
    count[char] += 1

print(" ".join(map(str, count.values())))
"""