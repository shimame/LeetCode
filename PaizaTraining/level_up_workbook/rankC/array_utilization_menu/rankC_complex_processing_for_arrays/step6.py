pins = []
for _ in range(4):
    pins += input().split()
    
for i in range(len(pins)):
    if pins[i] == "1":
        minum_position = len(pins) - i

print(minum_position)
print(pins.count("1"))