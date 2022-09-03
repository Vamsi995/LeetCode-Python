class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        temp = []
        
        for i in range(10):
            temp.append(str(i))
            
        
        for r in range(n-1):
            # print(r, temp)
            ans = temp.copy()
            temp = []
    
            for i in range(len(ans)):
                s = ans[i]
       
                new_dig = ""
                if 0 <= int(s[0]) - k <= 9:
                    new_dig = str(int(s[0]) - k)
                    t = new_dig + s
                    temp.append(t)
                    
                if 0 <= int(s[0]) + k <= 9:
                    new_dig = str(int(s[0]) + k)
                    t = new_dig + s
                    temp.append(t)
        
        final_ans = []
        
        for st in temp:
            if len(str(int(st))) == n:
                final_ans.append(int(st))
        
        return set(final_ans)