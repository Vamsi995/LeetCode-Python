class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        triplet = [nums[0]]
        store_max = float("Inf")
        
        for i in range(1, len(nums)):
            
            if nums[i] > store_max:
                return True
            
            if len(triplet) == 1:
            
                if nums[i] > triplet[-1]:
                    triplet.append(nums[i])
                else:
                    triplet.pop()
                    triplet.append(nums[i])
                
            elif len(triplet) == 2:
                
                if nums[i] > triplet[-1]:
                    return True
                elif nums[i] < triplet[-1]:
                    
                    if nums[i] > triplet[0]:
                        triplet.pop()
                        triplet.append(nums[i])
                    elif nums[i] < triplet[0]:
                        if triplet[-1] < store_max:
                            store_max = triplet[-1]
                        triplet.clear()
                        triplet.append(nums[i])
                        
                    
        return False
            
            
        
        
        
        
        
        
        