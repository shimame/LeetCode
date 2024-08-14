N = int(input())
history = []
for _ in range(N):
    word = input()
    if word in history:
        history.remove(word)
    history.append(word)
history.reverse()
for i in history:
    print(i)