class Robot:
    def __init__(self, x, y, lv):
        self.x = x
        self.y = y
        self.lv = lv

    def move(self, direction):
        if self.lv == 1:
            distance = 1
        elif self.lv == 2:
            distance = 2
        elif self.lv == 3:
            distance = 5
        elif self.lv == 4:
            distance = 10

        if direction == "N":
            self.y -= distance 
        elif direction == "S":
            self.y += distance 
        elif direction == "E":
            self.x += distance 
        elif direction == "W":
            self.x -= distance

    def level_up(self, toolbox_positions):
        for i in toolbox_positions:
            if self.x == i[0] and self.y == i[1]:
                self.lv += 1

H, W, N, K = [int(x) for x in input().split()]
toolbox_positions = []
robots = []
for _ in range(10):
    toolbox_positions.append([int(x) for x in input().split()])

for _ in range(N):
    x, y, lv = [int(x) for x in input().split()]
    robots.append(Robot(x, y, lv))

for _ in range(K):
    input_line = input().split()
    robot_num = int(input_line[0]) - 1
    robot_direction = input_line[1]
    robots[robot_num].move(robot_direction)
    robots[robot_num].level_up(toolbox_positions)

for i in robots:
    print(i.x, i.y, i.lv)