import sys
import math
import generate
from statistics import mean, median
import numpy

debug = False
printNum = False
count = 0
gentype = 0
args = []

def main():
  print("[INFO     ] START")
  check()
  switcher_gentype(gentype)
  numbers = getNumbers(gentype)
  validate(numbers)
  if printNum: printNumbers(numbers)

def validate(numbers):
  minN = min(numbers)
  maxN = max(numbers)
  meanN = mean(numbers)
  print("[INFO     ] Result: min: " + str(minN) + ", max: " + str(maxN) + ", meanN: " + str(meanN))

def check():
  global debug
  global printNum
  global count
  global gentype
  global args
  arglen = len(sys.argv)
  if(sys.argv[-1] == '-d' or sys.argv[-1] == '--debug' or sys.argv[-2] == '-d' or sys.argv[-2] == '--debug'):
    debug = True
  if(sys.argv[-1] == '-p' or sys.argv[-1] == '--print' or sys.argv[-2] == '-p' or sys.argv[-2] == '--print'):
    printNum = True
  if debug: print("[DEBG     ] Args: " + str(arglen))
  if (arglen < 3):
    print("[    ERROR] Not enough attributes.")
    raise AttributeError
  else:
    gentype = int(sys.argv[1])
    args = list(sys.argv[2].split(','))
    count = int(sys.argv[3])

def switcher_gentype(gentype):
  switcher = {
    0: "Uniform Python",
    1: "Triangular own",
    2: "Triangular Python"
  }
  print("[INFO     ] Type: " + switcher.get(gentype, "Invalid type"))

def getNumbers(t):
  if t == 0:
    return generate.uniformRange(count, args)
  elif t == 1:
    return generate.triangularRange(count, gentype, args)
  elif t == 2:
    return generate.triangularRange(count, gentype, args)

def printNumbers(numbers):
  for n in range(0, len(numbers)):
    nrange = numpy.arange(0, numbers[n], 0.01)
    for i in nrange:
      sys.stdout.write("|")
    sys.stdout.write(" " + str(round(numbers[n], 4)))
    print()

main()