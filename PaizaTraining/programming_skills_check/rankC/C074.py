h, w, x = map(int, input().split())
sentence = [input() for _ in range(h)]
sentence = "".join(sentence)

new_h = len(sentence) // x
if len(sentence) % x != 0:
    new_h += 1

for i in range(new_h):
    print(sentence[i*x:i*x+x])