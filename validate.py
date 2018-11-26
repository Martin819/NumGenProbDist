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
  for i in range(0,len(sys.argv)):
    if(sys.argv[i] == "-p" or sys.argv[i] == "--print"):
      printNum = True
      break
  for i in range(0,len(sys.argv)):
    if(sys.argv[i] == "-d" or sys.argv[i] == "--debug"):
      debug = True
      break
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
    2: "Triangular Python",
    3: "Beta own",
    4: "Beta Python",
    20: "Beta NumPy",
    13: "Normal own",
    14: "Normal Python"
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
  ## Print CDF
  print("CDF:")
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
        minrange = numpy.arange(minN, 0, step)
        currange = numpy.arange(numbers[n], 0, step)
        diffrange = len(minrange) - len(currange)
        for i in range(0, diffrange):
            sys.stdout.write(" ")
      nrange = numpy.arange(numbers[n], 0, step)
      for i in nrange:
        sys.stdout.write(fg.red + "|")
      sys.stdout.write(" " + str(round(numbers[n], 4)))
    print()
  ## TODO: Print PDF
  print("PDF:")
  step = diffN / (float(rows) * 0.9)
  curCount = 0
  for i in numpy.arange(minN, maxN, step):
    curLow = step * i
    curHigh = step * (i + 1)
    if debug: print("curLow: " + str(curLow) + " curHigh: " + str(curHigh))
    for n in range(0, len(numbers)):
      if (numbers[n] >= curLow and numbers[n] < curHigh):
        curCount = curCount + 1
    lowTag = str(round(curLow,4))
    sys.stdout.write(fg.white + str(round(curLow,4)) + " ")
    for k in range (0, 7 - len(lowTag)):
      sys.stdout.write(fg.white + " ")
    for j in range (0, curCount):
      sys.stdout.write(fg.white + "|")
    print()
    curCount = 0



def stdoutRight(msg):
  sys.stdout.write(msg.rjust(50))
  # sys.stdout.write('\b' * len(msg))

main()