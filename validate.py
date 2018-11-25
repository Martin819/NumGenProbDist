import sys
import math
import generate
from statistics import mean, median
import numpy
from sty import fg
import os

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
  if (t == 0):
    return generate.uniformRange(count, args)
  elif (t == 1 or t == 2):
    return generate.triangularRange(count, gentype, args)
  elif (t == 3 or t == 4 or t == 20):
    return generate.betavariateRange(count, gentype, args)
  elif (t == 13 or t == 14):
    return generate.normalvariateRange(count, gentype, args)

def printNumbers(numbers):
  negative = False
  rows, columns = os.popen('stty size', 'r').read().split()
  numbers.sort()
  maxN = max(numbers)
  minN = min(numbers)
  diffN = maxN - minN
  step = diffN / (float(columns) * 0.9)
  if(minN < 0): negative = True
  for n in range(0, len(numbers)):
    if(numbers[n] >= 0):
      if negative:
        negrange = numpy.arange(minN, 0, step)
        for i in negrange:
          sys.stdout.write(" ")
      nrange = numpy.arange(0, numbers[n], step)
      for i in nrange:
        sys.stdout.write(fg.white + "|")
      sys.stdout.write(" " + str(round(numbers[n], 4)))
    else:
      if negative:
        negrange = numpy.arange(0, numbers[n] - minN, step)
        for i in negrange:
            sys.stdout.write(" ")
      nrange = numpy.arange(numbers[n], 0, step)
      for i in nrange:
        sys.stdout.write(fg.red + "|")
      sys.stdout.write(" " + str(round(numbers[n], 4)))
    print()

def stdoutRight(msg):
  sys.stdout.write(msg.rjust(50))
  # sys.stdout.write('\b' * len(msg))

main()