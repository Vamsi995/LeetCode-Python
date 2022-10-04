class Solution:
    def deleteString(self, s: str) -> int:
        
        if len(set(s)) == 1: 
            return len(s)
        
        return self.find_count(s, {})

    
    def find_count(self, s, mem):
        
        if s == "":
            return 1
        
        
        if s not in mem:
            
            count = 0
            
            for stringlen in range(1, len(s)//2 + 1):
                if s[:stringlen] == s[stringlen:2*stringlen]:
                    count = max(count, self.find_count(s[stringlen:], mem))
            
            mem[s] = count + 1
        
        return mem[s]
     
        
        
        
        
        
        
        
        