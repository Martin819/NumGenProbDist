import random
from math import sqrt, cos, pi, log
import numpy

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

def numpyBetavariate(alpha, beta):
  return numpy.random.beta(alpha, beta)

def getExpovariate(alpha, beta):
  return random.betavariate(alpha, beta)

def getGammavariate(alpha, beta):
  return random.gammavariate(alpha, beta)

def getGauss(mu, sigma):
  return random.gauss(mu, sigma)

def getLofnormvariate(mu, sigma):
  return random.lognormvariate(mu, sigma)

def calculateNormalvariate(mu, sigma):
  y1 = random.uniform(0.0, 1.0) + 1
  y2 = random.uniform(0.0, 1.0) + 1
  z = cos(2 * pi * y2) * sqrt(-2 * log(y1))
  return (z * sigma) + mu

def getNormalvariate(mu, sigma):
  return random.normalvariate(mu, sigma)