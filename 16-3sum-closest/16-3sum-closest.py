class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = inf
        ans = None
        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            
            while l < r :
                tot = nums[i] + nums[l] + nums[r]
                dif = abs(target-tot)
                
                if dif < min_diff:
                    min_diff = dif
                    ans = tot;
                
                if tot == target:
                    return tot
                
                elif tot < target:
                    l += 1
                
                elif tot > target:
                    r -= 1
                
        return ans