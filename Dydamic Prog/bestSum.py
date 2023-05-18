def bestSum(target: int, numbers, memo = {}) -> list:
  if target in memo: return memo[target]
  if target == 0: return []
  if target < 0: return None

  result = None
  for num in numbers:
    remainder = target - num
    combination = bestSum(remainder, numbers, memo)
    if combination != None:
      temp = [i for i in combination] #need deep copy as python uses pass by reference
      temp.append(num)
      if (result == None) or (len(temp) < len(result)):
        result = temp
  
  memo[target] = result
  # print(memo)
  return result
  
list_test = {
  7: [2,3,4,7], 
  8: [2,3,5],
  101: [2,4,6,8,10],
  300: [7,14],
  500: [15, 17, 5, 101, 100]
}

for k in list_test:
  print(bestSum(k, list_test[k], {}))
