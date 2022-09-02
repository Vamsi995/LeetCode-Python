class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = {}
        
        l = 0
        r = 0
        
        res = 0
        
        while r < len(s):
            
            if s[r] in dic:
                l = max(l, dic[s[r]])
            
            dic[s[r]] = r + 1
            res = max(r - l + 1, res)
            
            r += 1
                
                
        return res
            
        
        
        
        