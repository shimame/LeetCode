class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name
    def getnum(self):
        return self.number
    def getname(self):
        return self.name
N = int(input())
roster = []
answer = []
for _ in range(N):
    input_line = input().split()
    if "make" == input_line[0]:
        number = input_line[1]
        name = input_line[2]
        roster.append(Employee(number, name))
    elif "getnum" == input_line[0]:
        index = int(input_line[1]) - 1
        number = roster[index].getnum()
        answer.append(number)
    elif "getname" == input_line[0]:
        index = int(input_line[1]) - 1
        name = roster[index].getname()
        answer.append(name)
for i in answer:
    print(i)