class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #Kasean Algo? SameO(n)time O(1)space?
        n = len(prices)
        currMax, res = 0, 0
        for i in range(1, n):
            currMax += prices[i] - prices[i-1]
            if currMax < 0:
                currMax = 0
            if currMax > res:
                res = currMax
        return res
        
        
        # #two-pointer O(n)time? O(1)space?
        # profit = 0
        # n = len(prices)
        # lp, rp = 0, 1
        # while rp < n:
        #     p = prices[rp] - prices[lp]
        #     if p <= 0:
        #         lp, rp = rp, rp + 1
        #     else:
        #         if p > profit: profit = p
        #         rp += 1
        # return profit

        # Brute Force O(n^2) time O(1)space
        # profit = 0
        # n = len(prices)
        # #O(n^2) brute force too long
        # for i, buy in enumerate(prices):
        #     for j in range(i+1, n):
        #         p = prices[j] - buy
        #         if p > profit: profit = p
        # return profit