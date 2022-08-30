class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for i in range(len(asteroids)):
            
            if len(stack) == 0:
                stack.append(asteroids[i])
                continue
                
            if (asteroids[i] > 0 and stack[-1]) > 0 or (asteroids[i] < 0 and stack[-1] < 0):
                stack.append(asteroids[i])
                continue
            
            

            while len(stack) > 0:
                
                
                if stack[-1] > 0 and asteroids[i] < 0:
                
                    if abs(stack[-1]) == abs(asteroids[i]):
                        stack.pop()
                        break

                    if abs(stack[-1]) > abs(asteroids[i]):
                        break

                    if abs(stack[-1]) < abs(asteroids[i]):
                        stack.pop()
                        if len(stack) == 0:
                            stack.append(asteroids[i])
                            break
                            
                else:
                    stack.append(asteroids[i])
                    break
                    
        return stack
                
                                
        