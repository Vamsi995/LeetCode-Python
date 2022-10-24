class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        dp = [set()]
        for a in arr:
            #1
            if len(set(a))<len(a):
                 continue
            a = set(a)
            for c in dp[:]:
                #2
                if a & c:
                    continue
                #3     
                dp.append(a|c)
        return max(len(a) for a in dp)