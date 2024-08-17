class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name
    def get_num(self):
        return self.number
    def get_name(self):
        return self.name
    def change_num(self, number):
        self.number = number
    def change_name(self, name):
        self.name = name
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
        number = roster[index].get_num()
        answer.append(number)
    elif "getname" == input_line[0]:
        index = int(input_line[1]) - 1
        name = roster[index].get_name()
        answer.append(name)
    elif "change_num" == input_line[0]:
        index = int(input_line[1]) - 1
        number = input_line[2]
        roster[index].change_num(number)
    elif "change_name" == input_line[0]:
        index = int(input_line[1]) - 1
        name = input_line[2]
        roster[index].change_name(name)
for i in answer:
    print(i)