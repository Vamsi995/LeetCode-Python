class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

#     Memoization + Recursion
        
        return self.find_profit(prices, 0, 0, 2, {})
    
    
    
    def find_profit(self, prices, ind, bought, tr, mem):
        
        if ind >= len(prices) or tr == 0:
            return 0
        
        if (ind, bought, tr) not in mem:
            res = self.find_profit(prices, ind+1, bought, tr, mem)

            if bought == 1:

                res = max(res, self.find_profit(prices, ind+1, 0, tr-1, mem)+prices[ind])

            else:

                res = max(res, self.find_profit(prices, ind+1, 1, tr, mem)-prices[ind])


            mem[(ind, bought, tr)] = res
        
        return mem[(ind, bought, tr)]
        
        
#     Divide and Conquer        

#         left = [0 for _ in range(len(prices))]    
#         right = [0 for _ in range(len(prices))]
        
#         l_min = prices[0]
#         r_max = prices[-1]
        
#         for i in range(1, len(left)):
#             left[i] = max(left[i-1], prices[i]-l_min)
#             l_min = min(l_min, prices[i])
        
        
#         for i in range(len(right) - 2, -1, -1):
#             right[i] = max(right[i+1], r_max - prices[i])
#             r_max = max(r_max, prices[i])
        
#         profit = 0

#         for i in range(len(left)):
#             if i == 0:
#                 profit = max(profit, right[i])
#             else:
#                 profit = max(profit, left[i-1]+right[i]) 
        
        
#         return profit