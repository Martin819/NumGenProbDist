import sys
import generate
import numpy
import validate

debug = False
printNum = False
printOnlyTotal = False
validateRes = False
genCsv = False
genTxt = False
genPath = ""
txtPath = ""
run = 0
count = 0
gentype = 0
batch = 1
args = []

def main():
  import datetime
  global run
  check()
  if (genCsv or genTxt):
    now = datetime.datetime.now()
    if(batch > 1):
      dirName = switcher_gentype(gentype, 1).replace(" ", "-") + "_" + now.strftime("%Y-%m-%d-%H-%M-%S")
      filePrefix = dirName
    else:
      dirName = ""
      filePrefix = switcher_gentype(gentype, 1).replace(" ", "-") + "_" + now.strftime("%Y-%m-%d-%H-%M-%S")
  for i in range(batch):
    if (batch > 1):
      print("Run " + str(run + 1) + ":")
      print("======")
    run = run + 1
    switcher_gentype(gentype)
    numbers = getNumbers(gentype)
    if printNum: printNumbers(numbers)
    if validateRes:
      validate.validate(numbers, printOnlyTotal)
      if ((batch > 1) and (run == batch)):
        validate.printTotal()
    if genCsv: generateCsv(numbers, filePrefix, dirName)
    if genTxt: generateTxt(numbers, filePrefix, dirName)

def check():
  global debug
  global printNum
  global validateRes
  global genCsv
  global genPath
  global genTxt
  global txtPath
  global count
  global batch
  global printOnlyTotal
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
  for i in range(0,len(sys.argv)):
    if(sys.argv[i] == "-c" or sys.argv[i] == "--csv"):
      genCsv = True
      try:
        if (len(sys.argv) > (i + 1)):
          genPath = sys.argv[i + 1]
        break
      except ValueError:
        print("Invalid value provided for parameter genPath")
  for i in range(0,len(sys.argv)):
    if(sys.argv[i] == "-t" or sys.argv[i] == "--txt"):
      genTxt = True
      try:
        if (len(sys.argv) > (i + 1)):
          txtPath = sys.argv[i + 1]
        break
      except ValueError:
        print("Invalid value provided for parameter txtPath")
  for i in range(0,len(sys.argv)):
    if(sys.argv[i] == "-v" or sys.argv[i] == "--validate"):
      validateRes = True
      break
  for i in range(0,len(sys.argv)):
    if(sys.argv[i] == "-b" or sys.argv[i] == "--batch"):
      try:
        if (len(sys.argv) > (i + 1)):
          batch = int(sys.argv[i + 1])
        break
      except ValueError:
        print("Invalid value provided for parameter batch")
  for i in range(0,len(sys.argv)):
    if(sys.argv[i] == "-r" or sys.argv[i] == "--results"):
      printOnlyTotal = True
      break
  if debug: print("[DEBG     ] Args: " + str(arglen))
  if (arglen < 3):
    raise AttributeError("Not enough attributes")
  else:
    gentype = int(sys.argv[1])
    args = list(sys.argv[2].split(','))
    count = int(sys.argv[3])

def switcher_gentype(gentype, doReturn = 0):
  switcher = {
    0: "Uniform Python",
    1: "Triangular own",
    2: "Triangular Python",
    22: "Triangular NumPy",
    3: "Beta own",
    4: "Beta Python",
    20: "Beta NumPy",
    5: "Exponential own",
    6: "Exponential Python",
    23: "Exponential NumPy",
    11: "Lognormal own",
    12: "Lognormal Python",
    21: "Lognormal NumPy",
    13: "Normal own",
    14: "Normal Python",
    24: "Normal NumPy"
  }
  if doReturn:
    return switcher.get(gentype, "Invalid type")
  else:
    print("Type: " + switcher.get(gentype, "Invalid type"))

def getNumbers(t):
  if (t == 0):
    return generate.uniformRange(count, args)
  elif (t == 1 or t == 2 or t == 22):
    return generate.triangularRange(count, t, args)
  elif (t == 3 or t == 4 or t == 20):
    return generate.betavariateRange(count, t, args)
  elif (t == 5 or t == 6 or t == 23):
    return generate.expovariateRange(count, t, args)
  elif (t == 11 or t == 12 or t == 21):
    return generate.lognormalvariateRange(count, t, args)
  elif (t == 13 or t == 14 or t== 24):
    return generate.normalvariateRange(count, t, args)

def printNumbers(numbers):
  from sty import fg
  import os
  negative = False
  rows, columns = os.popen('stty size', 'r').read().split()
  numbers.sort()
  maxN = max(numbers)
  minN = min(numbers)
  diffN = maxN - minN
## Print CDF
  print("CDF:")
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
## Print PDF
  print()
  print("PDF:")
  step = diffN / (float(rows) * 0.9)
  print("step: " + str(step))
  curCount = 0
  for i in range(0, len(numpy.arange(minN, maxN, step))):
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

def generateCsv(numbers, filePrefix, dirName):
  import csv, os
  global run
  filename = dirName + "/" + filePrefix + "_" + str(run) + ".csv"
  if (genPath != ""):
    filename = genPath + filename
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, 'w', newline='') as numbersCsv:
    wr = csv.writer(numbersCsv, quoting=csv.QUOTE_ALL)
    wr.writerow(numbers)

def generateTxt(numbers, filePrefix, dirName):
  import os
  global run
  filename = filename = dirName + "/" + filePrefix + "_" + str(run) + ".txt"
  if (txtPath != ""):
    filename = txtPath + filename
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, 'w') as f:
    for item in numbers:
        f.write("%s\n" % item)

main()