import random
from math import sqrt

def getUniform(low, high):
  return random.uniform(low, high)

def calculateTriangular(a, b, c):
  U = random.uniform(0.0, 1.0)
  F = (c - a) / (b - a)
  if (U <= F):
    return a + sqrt(U * (b - a) * (c - a))
  else:
    return b - sqrt((1.0 - U) * (b - a) * (b - c))

def getTriangular(low, high, mode):
  return random.triangular(low, high, mode)

def calculateBetavariate(alpha, beta):
  return 0

def getBetavariate(alpha, beta):
  return random.betavariate(alpha, beta)

def getExpovariate(alpha, beta):
  return random.betavariate(alpha, beta)

def getGammavariate(alpha, beta):
  return random.gammavariate(alpha, beta)

def getGauss(mu, sigma):
  return random.gauss(mu, sigma)

def getLofnormvariate(mu, sigma):
  return random.lognormvariate(mu, sigma)

def getNormalvariate(mu, sigma):
  return random.normalvariate(mu, sigma)