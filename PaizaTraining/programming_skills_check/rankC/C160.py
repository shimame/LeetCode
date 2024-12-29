import numpy
import math

n = int(input())
d = [int(x) for x in input().split()]
print(math.ceil(numpy.average(d)))