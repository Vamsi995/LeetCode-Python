class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        
        arr = list(zip(efficiency, speed))
        
        arr.sort(reverse=True)
        
        min_heap = []
        running_sum = 0
        
        max_performance = 0
        
        for i in range(len(arr)):
            
            curr_eff = arr[i][0]
            running_sum += arr[i][1]
            heapq.heappush(min_heap, [arr[i][1], arr[i][0]])
            
            
            while len(min_heap) > 0 and len(min_heap) > k:
                
                sp, ef = heapq.heappop(min_heap)
                running_sum -= sp
                
            max_performance = max(max_performance, curr_eff * running_sum)
        
        
        
        return max_performance % (10**9 + 7)
        
        
        
        