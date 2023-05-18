import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter_s = collections.Counter(s)
        even, odd = 0, 0
        for char in counter_s:
            if counter_s[char] % 2 == 0:
                even += counter_s[char]
            else:
                even += counter_s[char] - 1
                odd = 1
        longestLength = even + odd

        return longestLength