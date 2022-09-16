class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        dp = [[0 for _ in range(len(multipliers)+1)] for _ in range(len(multipliers) + 1)]
        
        m = len(multipliers)
        
        
        for i in range(m-1, -1, -1):

            for start in range(i, -1, -1):
                
                end = len(nums) - 1 - (i - start)
                dp[i][start] = max(nums[start] * multipliers[i] + dp[i+1][start+1], nums[end]*multipliers[i] + dp[i+1][start])
                
                
            
        

        return dp[0][0]
   
        
    
        
        
        
        