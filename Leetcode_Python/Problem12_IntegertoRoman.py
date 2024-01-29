def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    answer = ""
    i = 0
    while num != 0:
        while num >= values[i]:
            num -= values[i]
            answer += romans[i]
            print(num)
        i += 1

    return answer

num = 3
print(intToRoman(num))