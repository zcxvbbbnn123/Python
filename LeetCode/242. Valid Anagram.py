import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use counter
        # counter_s = collections.Counter(s)
        # counter_t = collections.Counter(t)
        # return counter_s == counter_t
        
        # use counter but shorter code
        return collections.Counter(s) == collections.Counter(t)
        
        #sorted works as well
        # return sorted(s) == sorted(t)
        
        #use custom dict as counter
        # counter_s = {}
        # counter_t = {}
        # for c in s:
        #     if c in counter_s:
        #         counter_s[c] += 1 
        #     else:
        #         counter_s[c] = 1
        # for c in t:
        #     if c in counter_t:
        #         counter_t[c] += 1 
        #     else:
        #         counter_t[c] = 1
        # return counter_s == counter_t