# 家の軒数n、男の子の人数m 、Aliceが連続で驚かされると帰ってしまう軒数k
n, m, k = map(int, input().split())
hide_house_nums = [int(input()) for _ in range(m)]
candy_count = 0
continuous_mischeif_count = 0

for i in range(1, n+1):
    if i in hide_house_nums:
        continuous_mischeif_count += 1
    else:
        candy_count += 1
        continuous_mischeif_count = 0
    
    if continuous_mischeif_count == k:
        break

print(candy_count)