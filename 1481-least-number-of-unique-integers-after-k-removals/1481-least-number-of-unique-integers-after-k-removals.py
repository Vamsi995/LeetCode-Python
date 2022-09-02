class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freq = {}
        
        for i in range(len(arr)):
            freq[arr[i]] = 1 + freq.get(arr[i], 0)
        
        
        min_heap = []
        
        for el, fr in freq.items():
            heapq.heappush(min_heap, [fr, el])
            
        
        while k != 0:
            
            fr, el = heapq.heappop(min_heap)
            
            fr -= 1
            k -= 1
            
            if fr != 0:
                heapq.heappush(min_heap, [fr, el])
        
        
        t = [el for fr, el in min_heap]
        
        return len(set(t))
            
        
        
        
        