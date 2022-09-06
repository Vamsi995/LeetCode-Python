class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited = {}
        
        for i in range(len(nums)):
            
            if target - nums[i] not in visited:
                visited[nums[i]] = i
            else:
                return [i, visited[target - nums[i]]]
        
        
        