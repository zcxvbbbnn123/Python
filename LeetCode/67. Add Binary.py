class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #O(n)time O(1) space
        #00->1, 01=10->0, 11->0 +carry
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0 or carry:
            aBit = int(a[i]) if i >= 0 else 0
            bBit = int(b[j]) if j >= 0 else 0
            temp = aBit + bBit + carry
            if temp == 0:
                res += "0"
                carry = 0
            elif temp == 1:
                res += "1"
                carry = 0
            elif temp == 2:
                res += "0"
                carry = 1
            else:
                res += "1"
                carry = 1
            i, j = i - 1, j - 1
                
        return res[::-1]