import sys
import distribution

def uniformRange(gencount, args):
  generated = []
  low = float(args[0])
  high = float(args[1])
  for i in range(0, gencount):
      generated.append(distribution.getUniform(low, high))
  return generated

def triangularRange(gencount, gentype, args):
  generated = []
  low = float(args[0])
  high = float(args[1])
  mode = float(args[2])
  if (gentype == 1):
    for i in range(0, gencount):
      generated.append(distribution.calculateTriangular(low, high, mode))
  elif (gentype == 2):
    for i in range(0, gencount):
      generated.append(distribution.getTriangular(low, high, mode))
  elif (gentype == 22):
    for i in range(0, gencount):
      generated.append(distribution.numpyTriangular(low, high, mode))
  return generated

def betavariateRange(gencount, gentype, args):
  generated = []
  alpha = float(args[0])
  beta = float(args[1])
  if (gentype == 3):
    for i in range(0, gencount):
      generated.append(distribution.calculateBetavariate(alpha, beta))
  elif (gentype == 4):
    for i in range(0, gencount):
      generated.append(distribution.getBetavariate(alpha, beta))
  elif (gentype == 20):
    for i in range(0, gencount):
      generated.append(distribution.numpyBetavariate(alpha, beta))
  return generated

def expovariateRange(gencount, gentype, args):
  generated = []
  lambd = float(args[0])
  if (gentype == 5):
    for i in range(0, gencount):
      generated.append(distribution.calculateExpovariate(lambd))
  elif (gentype == 6):
    for i in range(0, gencount):
      generated.append(distribution.getExpovariate(lambd))
  elif (gentype == 23):
    for i in range(0, gencount):
      generated.append(distribution.numpyExpovariate(lambd))
  return generated

def lognormalvariateRange(gencount, gentype, args):
  generated = []
  mu = float(args[0])
  sigma = float(args[1])
  if (gentype == 11):
    for i in range(0, gencount):
      generated.append(distribution.calculateLognormalvariate(mu, sigma))
  elif (gentype == 12):
    for i in range(0, gencount):
      generated.append(distribution.getLognormvariate(mu, sigma))
  elif (gentype == 21):
    for i in range(0, gencount):
      generated.append(distribution.numpyLognormalvariate(mu, sigma))
  return generated

def normalvariateRange(gencount, gentype, args):
  generated = []
  mu = float(args[0])
  sigma = float(args[1])
  if (gentype == 13):
    for i in range(0, gencount):
      generated.append(distribution.calculateNormalvariate(mu, sigma))
  elif (gentype == 14):
    for i in range(0, gencount):
      generated.append(distribution.getNormalvariate(mu, sigma))
  elif (gentype == 24):
    for i in range(0, gencount):
      generated.append(distribution.numpyNormalvariate(mu, sigma))
  return generated
