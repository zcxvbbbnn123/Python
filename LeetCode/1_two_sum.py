class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for n, v in enumerate(nums):
            diff = target - v
            if v in visited:
                return [visited[v], n]
            visited[diff] = n