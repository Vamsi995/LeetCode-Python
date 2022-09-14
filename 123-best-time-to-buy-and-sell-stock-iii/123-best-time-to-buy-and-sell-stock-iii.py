class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

#     Memoization + Recursion
        
    
        
        
        
#     Divide and Conquer        

        left = [0 for _ in range(len(prices))]    
        right = [0 for _ in range(len(prices))]
        
        l_min = prices[0]
        r_max = prices[-1]
        
        for i in range(1, len(left)):
            left[i] = max(left[i-1], prices[i]-l_min)
            l_min = min(l_min, prices[i])
        
        
        for i in range(len(right) - 2, -1, -1):
            right[i] = max(right[i+1], r_max - prices[i])
            r_max = max(r_max, prices[i])
        
        profit = 0

        for i in range(len(left)):
            if i == 0:
                profit = max(profit, right[i])
            else:
                profit = max(profit, left[i-1]+right[i]) 
        
        
        return profit