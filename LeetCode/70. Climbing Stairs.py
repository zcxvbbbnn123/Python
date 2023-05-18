class Solution:
    def climbStairs(self, n: int, memo = {}):
        # Permutation matters try dp
        if n in memo: return memo[n]
        if n == 0: return 1
        if n < 0: return 0
        
        total = 0
        for i in [1,2]:
            total += self.climbStairs(n - i)
            
        memo[n] = total
        return total
    # def climbStairsPermu(self, n: int, memo = {}):
    #     # Permutation matters and this function can return all possible paths
    #     # try using dp This can return all permutation but works very slow when n is big
    #     if n in memo: return memo[n]
    #     if n == 0: return [[]] 
    #     if n < 0: return None
        
    #     allPermu = None
    #     for i in [1,2]:
    #         temp = self.climbStairsPermu(n - i)
    #         if temp != None:
    #             permu = [p[:] for p in temp]
    #             for p in permu:
    #                 p += [i]
    #             if allPermu == None:
    #                 allPermu = permu
    #             else:
    #                 allPermu += permu
                    
    #     memo[n] = allPermu
    #     return allPermu

    # def climbStairs(self, n: int) -> int:
    #     return (self.climbStairsPermu(n, {}))
        
A = Solution()
print(A.climbStairs(4))