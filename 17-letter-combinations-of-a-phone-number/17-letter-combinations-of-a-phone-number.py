class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic = {
            2 : "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        ans = self.combine(digits, dic)
        return ans
        
    def combine(self, digits: str, dic):
        
        if len(digits) == 0:
            return []
        
        curr = digits[-1]
        digits = digits[:-1]
        curr_dic = dic[int(curr)]
        
        if len(digits) == 0:
            return [i for i in curr_dic]
        
        lis = []
        for j in curr_dic:
            for i in self.combine(digits, dic):
                lis.append(i + j)
        
        return lis