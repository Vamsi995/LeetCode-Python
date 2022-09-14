class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        return self.find_profit(prices, 0, 0, k, {})
        
        
    def find_profit(self, prices, ind, bought, tr, mem):
        
        
        if ind > len(prices) - 1 or tr == 0:
            return 0
        
        
        if (ind, bought, tr) not in mem:
            
            res = self.find_profit(prices, ind+1, bought, tr, mem)
            
            if bought == 1:
                res = max(res, self.find_profit(prices, ind+1, 0, tr-1, mem) + prices[ind])
                
            else:
                res = max(res, self.find_profit(prices, ind+1, 1, tr, mem) - prices[ind])
                
            mem[(ind, bought, tr)] = res
            
        return mem[(ind, bought, tr)]
        
        
        
        