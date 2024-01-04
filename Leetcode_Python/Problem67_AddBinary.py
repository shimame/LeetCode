def addBinary(a, b):    
    num_a = int(a,2)
    num_b = int(b,2)
    nums_sum = bin(num_a + num_b)
    return nums_sum[2:]

a = "11"
b = "1"
print(addBinary(a, b))