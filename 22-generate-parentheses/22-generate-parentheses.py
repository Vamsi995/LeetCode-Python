class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
  

        stack = ""
        ans = []
        
        
        def genParen(open_counter, closed_counter, stack):
            
            if open_counter == closed_counter == n:
                ans.append(stack)
            
            
            if open_counter < n:
                
                genParen(open_counter + 1, closed_counter, stack + "(")
                
            
            if closed_counter < open_counter:
                
                genParen(open_counter, closed_counter + 1, stack + ")")
                

        genParen(0, 0, stack)
        return ans

#         ans = self.generatePairs(n)
#         return ans
    
#     def generatePairs(self, n):
        
#         if n == 1:
#             return ["()"]
        
#         lis = []
#         for k in range(2):
#             for i in self.generatePairs(n - 1):
                
#                 if k == 1:
#                     lis.append("(" + i + ")")
#                     lis.append("()" + i)
#                     lis.append(i + "()")
#                 else:
#                     nearest_left = 0
#                     for j in range(len(i) - 1):
                        
#                         if i[j] == " (":
#                             nearest_left = j
                            
#                         if i[j] == ")" and i[j+1] == "(":
#                             lis.append(i[0:nearest_left] + "(" + i[nearest_left:j+1] + ")" + i[j+1:])
#                             lis.append(i[0:j+1] + "(" + i[j+1:] + ")") 
#         return list(set(lis))