class Solution:
    def myAtoi(self, s: str) -> int:
        
        k = ""
        neg_flag = 0
        non_digit = 0
        flag = 0
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        for i in range(len(s)):
        
            if s[i] == " ":
                if flag == 1:
                    break
                continue
            elif s[i] == "+" or s[i] == "-":
                if flag == 1:
                    break
                if i < len(s) - 1:
                    if s[i] == "-":
                        neg_flag = -1
                    if s[i] == "+":
                        neg_flag = 1
                    if s[i+1] not in digits:
                        neg_flag = 0
                        flag = 2
                        break
                    else:
                        flag = 1
            
            elif s[i] in digits:
                k += s[i]
                flag = 1
            else:
                flag = 0
            
            
            if flag == 0:
                if len(k) >= 0:
                    break
        

        if k == "" or flag == 2:
            return 0
        
        if neg_flag == 0:
            k = int(k)
        else:
            k = neg_flag * int(k)
        
        low = -(2 ** 31)
        high = low * -1 - 1
        
        
        if k > high:
            return high 
        elif k < low:
            return low
        
        return k
                        
        