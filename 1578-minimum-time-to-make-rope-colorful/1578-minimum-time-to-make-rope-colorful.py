class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        min_time = 0
        i = 0
        
        while i <= len(colors) - 2:
            
            if colors[i] == colors[i+1]:
                # print(i, i+1, min_time)
                if neededTime[i] <= neededTime[i+1]:
                    min_time += neededTime[i]            
                else:
                    min_time += neededTime[i+1]
                    k = i + 2
                    
                    
                    while k < len(colors) and colors[k] == colors[i]:
                        
                        if neededTime[i] <= neededTime[k]:
                            min_time += neededTime[i]
                            break
                        else:
                            min_time += neededTime[k]
                            k += 1
        
                    i = k
                    continue
            
            
            i += 1
        return min_time