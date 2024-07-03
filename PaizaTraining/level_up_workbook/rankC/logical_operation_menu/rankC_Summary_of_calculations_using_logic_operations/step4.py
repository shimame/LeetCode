A, B = map(int, input().split())
answer = (not(A) and B) or (A and (not(B)))
print(int(answer))

#print(a ^ b)