def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        print(f"a = {a}, b = {b}")
    return a

n = 4
print(climbStairs(n))