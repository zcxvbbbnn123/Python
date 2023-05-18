# THIS one way too slow as it is directly copy form permu 1 and remove duplicate will figure out another faster way
class Solution:
    def permuteUnique(self, nums: list[int], memo={}) -> list[list[int]]:
        #time complexity = O(n!)?
        #Use memo to remove duplicate path or use set?
        if nums == []: return [[]]
        
        res = []
        for i in range(len(nums)):
            num = nums.pop(0)
            permutation = self.permuteUnique(nums)
            for item in permutation:
                item += [num]
            res += permutation
            nums.append(num)
        res_no_dup = []
        [res_no_dup.append(x) for x in res if x not in res_no_dup]
        return res_no_dup

A = Solution()
print(A.permuteUnique(nums=[1,2,3,1]))