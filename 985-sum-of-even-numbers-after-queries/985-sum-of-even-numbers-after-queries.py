class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
       
        even_sum = 0
        ans = []
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_sum += nums[i]
                
                
        for q in queries:
            
            prev = nums[q[1]]
            nums[q[1]] += q[0]
            
            if prev % 2 == 0:
                even_sum -= prev
            if nums[q[1]] % 2 == 0:
                even_sum += nums[q[1]]
                
            ans.append(even_sum)
            
        return ans
    