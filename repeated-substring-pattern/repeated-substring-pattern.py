class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1,n//2+1):
            if n%i == 0:
                for j in range(i,n,i):
                    if s[0:i] != s[j:j+i]:
                        break
                    elif j==n-i:
                        return True
        return False
        