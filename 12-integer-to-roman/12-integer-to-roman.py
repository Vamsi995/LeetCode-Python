class Solution:
    def intToRoman(self, num: int) -> str:
        
        romans = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)]
        
        
        ans = ""
        
        
        for i in range(len(romans)-1, -1, -1):
            
            if num // romans[i][1] != 0:
                rep = num // romans[i][1]
                ans += romans[i][0] * rep
                num = num % romans[i][1]
            elif num == romans[i][1]:
                ans += romans[i][0]
        
        return ans
        
        