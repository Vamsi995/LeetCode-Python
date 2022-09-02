class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
       
        s = 0
        
        max_value = 0
        
        for i in range(len(damage)):
            
            if damage[i] > max_value:
                max_value = damage[i]
                
            s += damage[i]
            
        if max_value > armor:
            rem = max_value - armor
            s -= max_value 
            s += rem
        else:
            s -= max_value
        
        return s + 1
    