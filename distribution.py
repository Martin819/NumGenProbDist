import random
from math import sqrt, cos, pi, log, exp
import numpy

## Uniform
def getUniform(low, high):
  return random.uniform(low, high)

## Triangular
def calculateTriangular(a, b, c):
  U = random.uniform(0.0, 1.0)
  F = (c - a) / (b - a)
  if (U <= F):
    return a + sqrt(U * (b - a) * (c - a))
  else:
    return b - sqrt((1.0 - U) * (b - a) * (b - c))

def getTriangular(low, high, mode):
  return random.triangular(low, high, mode)

def numpyTriangular(low, high, mode):
  return numpy.random.triangular(low, mode, high)

## Beta
def calculateBetavariate(alpha, beta):
  x = random.gammavariate(alpha, 1.0)
  y = random.gammavariate(beta, 1.0)
  z = x / (x + y)
  return z

def getBetavariate(alpha, beta):
  return random.betavariate(alpha, beta)

def numpyBetavariate(alpha, beta):
  return numpy.random.beta(alpha, beta)

## Exponential
def calculateExpovariate(lambd):
  return log(random.uniform(0.0,1.0))/lambd

def getExpovariate(alpha, beta):
  return random.expovariate(alpha, beta)

def numpyExpovariate(lambd):
  return numpy.random.exponential(lambd)

## Lognormal
def calculateLognormalvariate(mu, sigma):
  return exp(random.normalvariate(mu, sigma))

def getLognormvariate(mu, sigma):
  return random.lognormvariate(mu, sigma)

def numpyLognormalvariate(mu, sigma):
  return numpy.random.lognormal(mu, sigma)

## Normal
def calculateNormalvariate(mu, sigma):
  y1 = random.uniform(0.0, 1.0) + 1
  y2 = random.uniform(0.0, 1.0) + 1
  z = cos(2 * pi * y2) * sqrt(-2 * log(y1))
  return (z * sigma) + mu

def getNormalvariate(mu, sigma):
  return random.normalvariate(mu, sigma)

def numpyNormalvariate(mu, sigma):
  return numpy.random.normal(mu, sigma)