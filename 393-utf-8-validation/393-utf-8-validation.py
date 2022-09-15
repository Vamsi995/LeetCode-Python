class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        arr = self.convert_to_binary(data)
        r = 0
        # print(arr)
        
        while r < len(arr):
        
            if len(arr[r]) > 0:
                
                if arr[r][0] == "1":
                    k = len(arr[r])
                    if k == 1:
                        return False
                    if k > 4:
                        return False
 
                    for i in range(r+1, r+k):
                        if i > len(arr) - 1:
                            return False
                        if len(arr[i]) != 1 or arr[i][0] != "1":
                            return False
                    
                    r += k
                else:
                    r += 1
                    
        return True
        
            
            
        
    
    def convert_to_binary(self, data):
        
        
        ans = []
        
        for d in data:
            
            temp = ""
            
            for i in range(7, -1, -1):
                
                
                q = d // 2 ** i
                d = d % 2**i
                
                if len(temp) > 0 and temp[-1] == "1" and q == 0:
                    break
                temp += str(q)
            
            ans.append(temp)
            
        return ans