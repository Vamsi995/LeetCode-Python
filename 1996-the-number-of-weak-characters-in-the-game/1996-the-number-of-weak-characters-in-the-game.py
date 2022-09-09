class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key=lambda x: (-x[0], x[1]))
      
        count = 0
        
        curr_max = 0
        
        for i in range(len(properties)):
            p = properties[i]
            
            if curr_max > p[1]:
                count += 1
            
            curr_max = max(curr_max, p[1])
            
        return count
            
            
        
        
        
        