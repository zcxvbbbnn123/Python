class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #Bisection search for O(log n)
        low, high = 0, len(nums) - 1
        while low <= high:
            #can use (high + low)/2 but could cause integer overflow
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
            
        #below is linear search time:O(n)
        #for i in range(len(nums)):
        #    if nums[i] == target:
        #        return i
        #return -1