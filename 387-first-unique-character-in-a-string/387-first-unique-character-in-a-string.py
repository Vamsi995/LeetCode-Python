class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        freq_map = {}
        index_map = {}
        
        queue = []
        
        
        for i in range(len(s)):    
            if s[i] not in freq_map:
                freq_map[s[i]] = 1 + freq_map.get(s[i], 0)
                index_map[s[i]] = i
            else:
                if s[i] in index_map:
                    index_map.pop(s[i])

        if len(index_map) == 0:
            return -1
        else:
            return sorted(index_map.values())[0]
        
        
        
        