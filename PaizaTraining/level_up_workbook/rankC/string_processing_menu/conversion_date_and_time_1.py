input_line = input().split("/")
for x in input_line:
    if ":" in x:
        hour, minute = x.split(":")
        print(hour)
        print(minute)
    else:
        print(x)