class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charFreq = {} # Keep track of the count of every character in the pattern we are trying to match
        for char in t:
            if char not in charFreq:
                charFreq[char] = 0
            charFreq[char] += 1
        
        matched = 0 # Keep track of all the characters we have fully matched
        minStart = 0 # Keep track of the start of the smallest substring/window
        minLength = float('inf') # Keep track of the minimum window/substring length
        windowStart = 0
        
        for windowEnd in range(len(s)):
            char = s[windowEnd] # Current character
            
            if char in charFreq:
                charFreq[char] -= 1
                
                if charFreq[char] == 0:
                    matched += 1
            
            while matched == len(charFreq):
                windowSize = windowEnd - windowStart + 1 # Current window size
                if windowSize < minLength:
                    minLength = windowSize
                    minStart = windowStart
                
                remove = s[windowStart] # The character we are going to remove from the window
                
                if remove in charFreq:
                    # If we are removing the last instance of this character from our window
                    if charFreq[remove] == 0:
                        matched -= 1 # Decrement matched since we have 1 less matched character now
                    charFreq[remove] += 1 # Add that character back into the charFreq hashmap
                windowStart += 1 # Increment windowStart to shrink the window
        
        if minLength == float('inf'):
            return ""
        return s[minStart: minStart + minLength]