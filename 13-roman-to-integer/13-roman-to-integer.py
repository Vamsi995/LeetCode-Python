class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        num = 0
        counter = 0
        
        for i in range(len(s)):
            
            if i < len(s)-1 and ((s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or (s[i] == "X" and (s[i+1] == "C" or s[i+1] == "L")) or (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"))):
                num -= symbols[s[i]]
            else:
                num += symbols[s[i]]
            
        return num