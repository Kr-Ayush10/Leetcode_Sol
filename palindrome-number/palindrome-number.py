class Solution:
    def isPalindrome(self, x: int) -> bool:
 
        if x < 0:
            return False 
        
        numdigits = 1
        dummy = x
		
        
        while dummy >= 10:
            dummy /= 10
            numdigits += 1
        
        for i in range(math.ceil(numdigits/2)):
            front = math.floor(x/pow(10, i)) % 10
            back = math.floor(x/pow(10, numdigits-i-1)) % 10
            if (front != back):
                return False

        return True