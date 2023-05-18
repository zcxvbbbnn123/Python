class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #simple solution first
        # if n < 1:
        #     return False
        # elif n == 1:
        #     return True
        # else:
        #     return self.isPowerOfTwo(n / 2)

        #bit manip
        return n > 0 and not(n & n - 1)
        