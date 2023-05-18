class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = ["N"]
        for char in s:
            if char in myDict:
                stack.append(myDict[char])
            else:
                if char != stack.pop():
                    return 0
        return len(stack) == 1