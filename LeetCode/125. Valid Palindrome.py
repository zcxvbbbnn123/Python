class Solution:
    def isPalindrome(self, s: str) -> bool:
        #try to use two pointer actually slower than the two-liner below but less space
        lp, rp = 0, len(s) - 1
        while lp < rp:
            if not s[lp].isalnum():
                lp += 1
            elif not s[rp].isalnum():
                rp -= 1
            elif s[lp].lower() == s[rp].lower():
                lp, rp = lp + 1, rp - 1
            else:
                return False
        return True
        
        # #need to remove non-alphaberic char and convert into lower case
        # #need to store the converted string separately if need to keep s unchanged
        # s = "".join(c for c in s if c.isalnum()).lower()
        # return s[::-1] == s