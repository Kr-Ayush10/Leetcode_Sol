class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "M": 1000, 
            "D": 500,  
            "C": 100, 
            "L": 50,  
            "X": 10, 
            "V": 5, 
            "I": 1
        }
        
        final_sum = 0
        prev = 0
        
        for c in s[::-1]:
            curr = roman[c]
            sign = 1
            
            if prev > curr :
                sign = -1
                
            final_sum += sign*curr
            prev = curr
            
        return final_sum