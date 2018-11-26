from statistics import mean, median

def validate(numbers):
  minN = min(numbers)
  maxN = max(numbers)
  meanN = mean(numbers)
  print("[INFO     ] Result: min: " + str(minN) + ", max: " + str(maxN) + ", meanN: " + str(meanN))