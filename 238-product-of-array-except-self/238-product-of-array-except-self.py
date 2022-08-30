class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        out_arr = []

        k = 1
        
        for i in range(len(nums)-1, -1, -1):
            k *= nums[i]    
            out_arr.insert(0, k)
        
        k = 1
        for i in range(len(nums)):
            k *= nums[i]
            nums[i] = k
        
        for i in range(len(nums)):
            if i == 0:
                out_arr[i] = out_arr[i+1]
            elif i == len(nums) - 1:
                out_arr[i] = nums[i-1]
            else:
                out_arr[i] = out_arr[i+1] * nums[i-1]
            
        
        return out_arr
        