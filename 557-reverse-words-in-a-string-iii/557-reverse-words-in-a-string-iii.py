class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        test = ""
        
        arr = s.split(" ")
        
        for string in arr:
            test += string[::-1]
            test += " "    
        
        
        return test.rstrip(" ")
        
        