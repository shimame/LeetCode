def half_adder(a, b):
    c = a & b
    s = a ^ b
    return (c, s)

A, B, C1 = map(int, input().split())
Cx, Sy = half_adder(A, B)
Cy, S = half_adder(Sy, C1)
C2 = Cx | Cy
#C2 = Cx ^ Cy
print(C2, S)