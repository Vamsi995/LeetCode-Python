class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        hash_map = {}
        ans = []
        
        for i in range(len(changed)):
            hash_map[changed[i]] = 1 + hash_map.get(changed[i], 0)
        
        changed.sort(reverse=True)
        for i in range(len(changed)):
            
            if changed[i] in hash_map and changed[i] * 2 in hash_map:
                ans.append(changed[i])
                hash_map[changed[i]] -= 1
                hash_map[changed[i]*2] -= 1
                
                if hash_map[changed[i]] == 0:
                    hash_map.pop(changed[i])
                
                if changed[i] * 2 in hash_map and hash_map[changed[i]*2] == 0:
                    hash_map.pop(changed[i]*2)
                
        
        if len(hash_map) == 0:
            return ans
        else:
            return []
        
        