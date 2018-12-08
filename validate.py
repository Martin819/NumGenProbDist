from statistics import mean, median

minN = 0
maxN = 0
meanN = 0
minNList = []
maxNList = []
meanNList = []
runNrList = []
maxRunList = []
avgRunList = []
rpList = []
ppList = []
rsList = []
psList = []

def validate(numbers, printOnlyTotal):
  bindGlobals(numbers)
  runTestsResults = getRunsTest(numbers)
  corellationResults = getCorellation(numbers)
  if not printOnlyTotal: printResults(runTestsResults, corellationResults)
  return 0

def bindGlobals(numbers):
  global minN, maxN, meanN, minNlist, maxNList, meanNList
  minN = min(numbers)
  minNList.append(minN)
  maxN = max(numbers)
  maxNList.append(maxN)
  meanN = mean(numbers)
  meanNList.append(meanN)

def printResults(runTestsResults, corellationResults):
  print("===============================")
  print("VALIDATION RESULTS:")
  print("-------------------------------")
  print("Globals: min: " + str(minN) + ", max: " + str(maxN) + ", meanN: " + str(meanN))
  print("-------------------------------")
  print("RunsTest:")
  print("     - Number of runs: " + str(runTestsResults.get('runNr', 'N/A')))
  print("     - Maximum run sequence: " + str(runTestsResults.get('maxRun', 'N/A')))
  print("     - Average run sequence: " + str(runTestsResults.get('avgRun', 'N/A')))
  print("-------------------------------")
  print("Position corellation test (abs values):")
  print("     - Pearson corellation coef: " + str(corellationResults.get('pearsonCoef', 'N/A')) + " - p-value: " + str(corellationResults.get('pearsonP', 'N/A')))
  print("     - Spearman corellation coef: " + str(corellationResults.get('spearmanCoef', 'N/A')) + " - p-value: " + str(corellationResults.get('spearmanP', 'N/A')))
  print()
  print()

def printTotal():
  print("===============================")
  print("TOTAL RESULTS:")
  print("-------------------------------")
  print("Globals: min: " + str(min(minNList)) + ", max: " + str(max(maxNList)) + ", meanN: " + str(mean(meanNList)))
  print("-------------------------------")
  print("RunsTest:")
  print("     - Number of runs:")
  print("               - Min: " + str(min(runNrList)))
  print("               - Max: " + str(max(runNrList)))
  print("               - Avg: " + str(mean(runNrList)))
  print("     - Maximum run sequence:")
  print("               - Max: " + str(max(maxRunList)))
  print("               - Avg: " + str(mean(maxRunList)))
  print("     - Average run sequence:")
  print("               - Min: " + str(min(avgRunList)))
  print("               - Max: " + str(max(avgRunList)))
  print("               - Avg: " + str(mean(avgRunList)))
  print("-------------------------------")
  print("Position corellation test (abs values):")
  print("     - Pearson corellation coef:")
  print("               - Min: " + str(min(rpList)))
  print("               - Max: " + str(max(rpList)))
  print("               - Avg: " + str(mean(rpList)))
  print("     - Spearman corellation coef:")
  print("               - Min: " + str(min(rsList)))
  print("               - Max: " + str(max(rsList)))
  print("               - Avg: " + str(mean(rsList)))
  print("===============================")
  print("END")
  print("===============================")

def getRunsTest(numbers):
  global runNrList, maxRunList, avgRunList
  seq = 0
  maxRuns = []
  curRun = 0
  positivity = []
  for i in range(len(numbers)):
    if (numbers[i] >= numbers[i - 1]):
      positivity.append(1)
    else:
      positivity.append(0)
  for j in range(len(positivity)):
    if (j == 0):
      curRun = 1
    else:
      if(positivity[j] == positivity[j - 1]):
        curRun = curRun + 1
      else:
        maxRuns.append(curRun)
        curRun = 1
  maxRun = max(maxRuns)
  maxRunList.append(maxRun)
  avgRun = mean(maxRuns)
  avgRunList.append(avgRun)
  runNr = len(maxRuns)
  runNrList.append(runNr)
  results = {'maxRun': maxRun, 'avgRun': avgRun, 'runNr': runNr}
  return results

def getCorellation(numbers):
  from scipy.stats import pearsonr, spearmanr
  import numpy
  global rsList, psList, rpList, ppList
  sortedNumbers = sorted(numbers)
  numDict = {}
  for i in range(len(numbers)):
    for j in range(len(sortedNumbers)):
      if numbers[i] == sortedNumbers[j]:
        pos = j + 1
        break
    numDict[i] = j
  origPosList = list(numDict.keys())
  sortPosList = list(numDict.values())
  rp, pp = pearsonr(origPosList, sortPosList)
  rp = abs(rp)
  pp = abs(pp)
  rpList.append(rp)
  ppList.append(pp)
  rs, ps = spearmanr(origPosList, sortPosList)
  rs = abs(rs)
  ps = abs(ps)
  rsList.append(rs)
  psList.append(ps)
  results = {'pearsonCoef': rp, 'pearsonP': pp, 'spearmanCoef': rs, 'spearmanP': ps}
  return results