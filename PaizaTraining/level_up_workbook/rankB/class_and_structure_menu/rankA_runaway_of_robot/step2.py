class Hero:
    def __init__(self, l, h, a, d, s, c, f):
        self.l = l 
        self.h = h
        self.a = a
        self.d = d
        self.s = s
        self.c = c
        self.f = f
    def levelup(self, h, a, d, s, c, f):
        self.l += 1
        self.h += h
        self.a += a
        self.d += d
        self.s += s
        self.c += c
        self.f += f
    def muscle_training(self, h, a):
        self.h += h
        self.a += a
    def running(self, d, s):
        self.d += d
        self.s += s
    def study(self, c):
        self.c += c
    def pray(self, f):
        self.f += f

N, K = [int(x) for x in input().split()]
persons = []
for _ in range(N):
    l, h, a, d, s, c, f = [int(x) for x in input().split()]
    person = Hero(l, h, a, d, s, c, f)
    persons.append(person)
for _ in range(K):
    input_line = input().split()
    person = persons[int(input_line[0]) - 1]
    event = input_line[1]
    if event == "levelup":
        h, a, d, s, c, f = [int(x) for x in input_line[2:]]
        person.levelup(h, a, d, s, c, f)
    elif event == "muscle_training":
        h, a = [int(x) for x in input_line[2:]]
        person.muscle_training(h, a)
    elif event == "running":
        d, s = [int(x) for x in input_line[2:]]
        person.running(d, s)
    elif event == "study":
        c = int(input_line[2])
        person.study(c)
    elif event == "pray":
        f = int(input_line[2])
        person.pray(f)
for i in persons:
    print(i.l, i.h, i.a, i.d, i.s, i.c, i.f)