class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        store = set([c for c in sentence])
        
        for i in range(26):
            if chr(ord("a") + i) not in store:
                return False
            
        return True
            
            
        
        