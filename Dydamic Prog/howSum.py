def howSum(target: int , numbers, memo = {}) -> list:
  if target in memo: return memo[target]
  if target == 0: return []
  if target < 0: return None
  
  for num in numbers:
    remainder = target - num
    result = howSum(remainder, numbers, memo)
    memo[target] = result
    if result != None:
      result.append(num)
      return result

  return None


# print(howSum(7, [2,3,4,7], {}))
# print(howSum(8, [2,3,5], {}))
# print(howSum(5, [2,4], {}))
# print(howSum(300, [7,14], {}))
print(howSum(101, [3,15,25], {}))