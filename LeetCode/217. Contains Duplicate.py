class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #has to be O(n)time right? O(n)space or O(1)space possible?
        checked = set()
        for num in nums:
            if num in checked: return True
            else: checked.add(num)
        return False