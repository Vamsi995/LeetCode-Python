class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        min_price = float("Inf")
        profit = 0
        
        for i in range(len(prices)):
            
            min_price = min(min_price, prices[i])
            
            if i == len(prices) - 1:
                profit += prices[i] - min_price
                break
            
            if prices[i+1] - prices[i] < 0:
                profit += prices[i] - min_price
                min_price = float("Inf")
            
            
        return profit
        