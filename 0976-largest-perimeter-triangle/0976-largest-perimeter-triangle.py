class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        
        temp = collections.deque()
        
        for i in range(len(nums)):
            
            temp.append(nums[i])
            
            if len(temp) == 3:
                
                if temp[0] + temp[1] <= temp[2] or temp[1] + temp[2] <= temp[0] or                 temp[0] + temp[2] <= temp[1]:
                    temp.popleft()
                    continue
                
                
                return temp[0] + temp[1] + temp[2]
                       
                
        return 0