class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        if d > len(jobDifficulty):
            return -1
        
        elif d == len(jobDifficulty):
            return sum(jobDifficulty)
        
        else:
            return self.jS(jobDifficulty, d, {})
    
    def jS(self, jobDifficulty, d, mem):
        
        
        if d == 1:
            return max(jobDifficulty)
        
        if (d, len(jobDifficulty)) not in mem:
        
            min_el = float('Inf')
            for i in range(0, len(jobDifficulty) - d + 1):

                if i == 0:
                    max_el = jobDifficulty[0]
                else:
                    max_el = max(jobDifficulty[0:i+1])

                min_el = min(min_el, max_el + self.jS(jobDifficulty[i+1:], d - 1, mem))
            
            mem[(d, len(jobDifficulty))] = min_el
        
        return mem[(d, len(jobDifficulty))] 
        
                    
            
        