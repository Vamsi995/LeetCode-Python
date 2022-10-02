class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        return self.num_rolls(n, target, k, {}) % (10**9 + 7)

    
    def num_rolls(self, n, target, k, mem):
        
        
        if n == 0:
            if target == 0:
                return 1
            return 0
            
        
        if (target, n) not in mem:
        
            ans = 0
            for i in range(1, k+1):

                ans += self.num_rolls(n-1, target - i, k, mem)
            mem[(target, n)] = ans

            
        return mem[(target, n)]
        
        
        