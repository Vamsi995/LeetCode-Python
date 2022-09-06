class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            
            first = i+1
            last = len(nums) - 1
            
            while last > first:
                
                s = nums[i] + nums[first] + nums[last]
                
                if s > 0:
                    last -= 1
                elif s < 0:
                    first += 1
                else:
                    lis = [nums[i], nums[first], nums[last]]
                    if lis not in ans:
                        ans.append(lis)
                    first += 1
        
        return ans