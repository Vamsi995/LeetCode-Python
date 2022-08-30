class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
#  Max min method

#         pivot = prices[0]
#         maxprof = 0
        
#         for i in range(1, len(prices)):
            
#             diff = prices[i] - pivot
            
#             if diff < 0:
#                 pivot = prices[i]
                
#             else:
#                 maxprof = max(diff, maxprof)
        
#         return maxprof




#         two pointer method

        l = 0
        r = 1
        res = 0
        
        while r < len(prices):
            
            if prices[r] - prices[l] < 0:
                
                l = r
                r += 1
                
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
                
        return res




