class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        rep_num = 0
        missing = 0
        
        hash_set = set()
        
        for i in range(len(nums)):
            
            if nums[i] in hash_set:
                rep_num = nums[i]
                # break
            else:
                hash_set.add(nums[i])
                
        for i in range(1,len(nums)+1):
            
            if i not in hash_set:
                missing = i
                break
                
        return [rep_num, missing]
                
        
            
        