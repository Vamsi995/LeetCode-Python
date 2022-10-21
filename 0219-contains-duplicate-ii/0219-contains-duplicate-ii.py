class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_map = {}
        
        for i in range(len(nums)):
            hash_map[nums[i]] = [i] + hash_map.get(nums[i], [])
            
        
        for n, val in hash_map.items():
            
            if len(val) > 1:
                
                for i in range(len(val) - 1):
                    
                    if abs(val[i] - val[i+1]) <= k:
                        return True
        
        
        
        return False
            
        
        