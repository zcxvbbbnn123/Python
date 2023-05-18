class Solution:
    def majorityElement(self, nums: list[int]) -> int:
# Can do one pass one pointer O(n) O(1) but generally slower as has to check all ele
        target = nums[0]
        count = 0
        for num in nums:
            if num == target:
                count += 1
            else:
                count -= 1
            if count < 0:
                target = num
                count = 0
        return target
        # #O(n) time O(1) space counter maybe?
        # #Damn this is O(n) O(n)
        # if len(nums) == 1: return nums[0]
        # n = len(nums) // 2 + 1
        # counter = {}
        # for i in nums:
        #     if i not in counter:
        #         counter[i] = 1
        #     else:
        #         counter[i] += 1  
        #         if counter[i] == n:
        #             return i
        