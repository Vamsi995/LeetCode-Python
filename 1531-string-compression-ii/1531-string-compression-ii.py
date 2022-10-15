class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        return self.find_length(0, k, {}, s)
    
    def find_length(self, start, k, mem, s):
        
        if start >= len(s) or len(s) - start <= k:
            return 0
        
        if (start,k) not in mem:
            count = {}
            ans = float("inf")
            max_freq = 0
            for i in range(start, len(s)):
                count[s[i]] = 1 + count.get(s[i], 0)
                max_freq = max(count[s[i]], max_freq)
                
                append_count = 1 + (len(str(max_freq)) if max_freq > 1 else 0)
                         
                if k >= i - start + 1 - max_freq:
                    ans = min(ans, append_count + self.find_length(i + 1, k - (i - start + 1 - max_freq), mem, s))
                
            mem[(start,k)] = ans
            
        return mem[(start,k)]
            
        
    
        
        
        