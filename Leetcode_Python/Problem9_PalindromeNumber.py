x = -121
y = str(x)[::-1]
print(x)
print(y)
if(x >= 0):
    if(x == int(y)):
        print("success")
    else:
        print("false")
else:
    print("false")