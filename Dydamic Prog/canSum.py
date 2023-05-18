def canSum(target: int , numbers, memo = {}) -> bool:
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False

    for num in numbers:
        remainder = target - num
        result = canSum(remainder, numbers, memo)
        memo[target] = result
        if result == True: return True

    return False

print(canSum(7, [2,3,4,7], {}))
print(canSum(8, [2,3,5], {}))
print(canSum(7, [2,4,6], {}))
print(canSum(300, [7,14], {}))