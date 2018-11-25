import random
from math import sqrt

def calculate(a, b, c):
  U = random.uniform(0.0, 1.0) #Return the next random floating point number in the range [0.0, 1.0).
  F = (c - a) / (b - a)
  if (U <= F):
    return a + sqrt(U * (b - a) * (c - a))
  else:
    return b - sqrt((1.0 - U) * (b - a) * (b - c))


def getTriangular(low, high, mode):
  return random.triangular(low, high, mode)
