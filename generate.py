import sys
import distribution

# def main():
#   print("[INFO     ] START")
#   check()
#   generate()

# def check():
#   global debug
#   global count
#   arglen = len(sys.argv)
#   if(sys.argv[-1] == '-d' or sys.argv[-1] == '--debug'):
#     debug = True
#   if debug: print("[DEBG     ] Args: " + str(arglen))
#   if (arglen < 2):
#     print("[    ERROR] Function to be used is not defined.")
#     raise AttributeError
#   if (arglen == 2):
#     print("[INFO     ] Numbers count not defined, generating just one.")
#     count = 1
#   else:
#     count = int(sys.argv[2])

# def generate():
#   global generated
#   print(sys.argv[1])
#   print(debug)
#   if (sys.argv[1] == '1'):
#     for i in range(0, count):
#       if debug: print("[DEBG     ] Calculting.")
#       generated.append(triangular.calculate(0.0, 3.0, 1.5))
#   elif (sys.argv[1] == '2'):
#     for i in range(0, count):
#       print("[DEBG     ] Getting.")
#       generated.append(triangular.getTriangular(0.0, 3.0, 1.5))
#   print(generated)

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
  return generated