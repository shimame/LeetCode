m = int(input())
for _ in range(m):
    ip = input()
    if ip.count(".") != 3:
        print("Flase")
        continue
  
    ip_nums = [int(x) for x in ip.split(".")]
    flag = True
    for num in ip_nums:
        if 0 > num or 255 < num:
            flag = False
            break
    print(flag)