class Solution:
    
    def maxSubArray(self, nums: list[int]) -> int:
        #O(n) solution, same logic but shorter than my first solution
        n = len(nums)
        largestSum = currSum = nums[0]
        for i in range(1, n):
            currSum = max(nums[i], currSum + nums[i])
            largestSum = max(largestSum, currSum)

        return largestSum

    # def maxSubArray(self, nums: list[int]) -> int:
    #     #O(n) solution? two pointer? my first solution
    #     n = len(nums)
    #     if n == 1: return nums[0]
        
    #     lp, rp = 0, 1
    #     largestSum, currSum = [nums[0]] * 2
    #     while rp < n:
    #         currSum += nums[rp]
    #         if nums[rp] > currSum:
    #             largestSum = max(largestSum, nums[rp])
    #             currSum = nums[rp]
    #             lp, rp = rp, rp+1
    #         else:
    #             largestSum = max(largestSum, currSum)
    #             rp += 1
        
    #     return largestSum