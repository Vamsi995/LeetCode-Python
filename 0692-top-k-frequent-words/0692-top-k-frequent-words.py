class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        
        freq = {}
        
        for w in words:    
            freq[w] = 1 + freq.get(w, 0)
            
        
        ans = sorted(freq.items(), key=lambda x: (-x[1],x[0]))
        
        final = []
        
        for i in range(k):
            final.append(ans[i][0])
            
        return final