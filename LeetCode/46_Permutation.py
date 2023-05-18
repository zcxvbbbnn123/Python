from statistics import mean
import time
#DP solution need to improve the passing slice of list part
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        #no memorization is needed as all numbers in nums are unique
        #time complexity = O(n!)?
        if nums == []: return [[]]
        
        res = []
        for i in range(len(nums)):
            num = nums.pop(0)
            #recursion with list slicing (nums[:i] + nums[i+1:]) / pop() and append()
            permutation = self.permute(nums)
            for item in permutation:
                item += [num]
            res += permutation
            nums.append(num)

        return res

A = Solution()
print(A.permute(nums=[1,2,3,4]))
# avg_time = []
# for i in range(100):
#     start = time.process_time()
#     A.permute(nums=[1,2,3,4,5,6,7])
#     end = time.process_time()
#     avg_time.append(end - start)
# print(mean(avg_time))