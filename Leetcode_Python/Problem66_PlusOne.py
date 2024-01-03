def plusOne(digits):
    keep = True
    count = len(digits) - 1
    while keep and count != -1:
        if digits[count] != 9:
            keep = False
        else:
            digits[count] = 0
            count -= 1

    if count == -1:
        digits = [1] + digits
    else:
        digits[count] += 1

    return digits


digits = [8,9,9,9]
print(plusOne(digits))