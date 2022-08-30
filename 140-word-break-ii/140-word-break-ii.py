class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        words = set(wordDict)
        
        ans = []
        temp = ""
        self.word_break(s, words, ans, temp)
        
        return ans
    
    def word_break(self, s, words, ans, temp):
        
        if s == "":
            ans.append(temp.strip(" "))
        
       
        
        for i in range(len(s)):

            if s[0:i+1] in words:
                self.word_break(s[i+1:], words, ans, temp + " " + s[0:i+1])


        