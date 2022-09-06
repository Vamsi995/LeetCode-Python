class Solution:
    def trap(self, height: List[int]) -> int:
        
#         water at i = Min(max(left hand side), max(right hand side)) - height[i]

#         res = 0
#         for i in range(1, len(height) - 1):

#                 c = min(max(height[0:i]), max(height[i+1:])) - height[i]
#                 if c > 0:
#                     res += c
#         return res


#          O(n) Time and O(n) Space
#         max_left = [0 for _ in range(len(height))]
#         max_right = [0 for _ in range(len(height))]
        
#         mini = 0
#         maxi = 0
#         for i in range(len(height)):
            
#             if height[i] > mini:
#                 max_left[i] = height[i]
#                 mini = height[i]
#             else:
#                 max_left[i] = mini
        
#         for i in range(len(height) - 1, -1, -1):
            
#             if height[i] > maxi:
#                 max_right[i] = height[i]
#                 maxi = height[i]
#             else:
#                 max_right[i] = maxi
        
#         res = 0

#         for i in range(len(height)):
            
#             c = min(max_left[i], max_right[i]) - height[i]
#             if c > 0: res += c
        
#         return res
        
        
# Two pointer Approach

        
        l = 0
        r = len(height) - 1
        
        max_left = height[l]
        max_right = height[r]
        res = 0
        
        while l < r:
            
            if height[l] < height[r]:
                l += 1
                if max_left - height[l] > 0: # Not required figure out why
                    res += max_left - height[l]
                max_left = max(max_left, height[l])        
                
            else:
                r -= 1
                if max_right - height[r] > 0:
                    res += max_right - height[r]
                max_right = max(max_right, height[r])
                
        return res
    
    
        
