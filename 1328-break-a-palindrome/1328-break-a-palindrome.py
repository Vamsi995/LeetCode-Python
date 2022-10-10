class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1:
            return ""
        
        pal = [v for v in palindrome]
        
        odd_flag = 0
        odd_index = 0
        odd_val = 0
        
        if len(palindrome) % 2 != 0:
            odd_flag = 1
            odd_index = (len(palindrome) - 1) // 2 
            odd_val = pal[odd_index]
            pal.pop(odd_index)
            
            palindrome = ''.join(pal)
            
        if len(set(palindrome)) == 1:
            
            if palindrome[0] == "a":
                if odd_flag == 1:
                    pal.insert(len(palindrome)//2, odd_val)
                    palindrome = ''.join(pal)
                return palindrome[:len(palindrome) - 1] + chr(ord("a") + 1)
            else:
                if odd_flag == 1:
                    pal.insert(len(pal)//2, odd_val)
                    palindrome = ''.join(pal)
                return "a" + palindrome[1:]
            
        # if len(palindrome) % 2 == 0:
        
        
#         temp = []
        
#         for i in range(len(pal)):
            
#             t = pal[i]
#             for k in range(26):
#                 pal[i] = chr(ord("a") + k)
#                 temp.append(''.join(pal))
#             pal[i] = t
            
#         temp.sort()
        
#         return temp[0]
            
        
        i = 0

        while pal[i] == "a":
            i += 1

        pal[i] = "a"

        # print(pal)
        if odd_flag == 1:
            pal.insert(len(pal)//2, odd_val)
        
        return ''.join(pal)

        # else:
        
        
        
        