class Solution:
    def reverse(self, x: int) -> int:
        
        
        low = -(2**31)
        high = 2**31 - 1
        res = 0
        neg_flag = 1 if x > 0 else -1
        
        while x:
            
            digit = abs(x) % 10
            x = int(x / 10)
            
            if res > high // 10 or (res == high // 10 and digit > high % 10):
                return 0
            
            if res < low // 10 or (res == low // 10 and digit < low % 10):
                return 0
            
        
            res = (res * 10) + digit
            
        return res * neg_flag
        