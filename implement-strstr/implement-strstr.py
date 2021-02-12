class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack or needle == haystack == "":
            return 0
        
        if not (needle or haystack) or len(needle) > len(haystack): 
            return -1
        
        
        for i in range (len(haystack) - len(needle) + 1):
            if haystack[i:len(needle) + i] == needle:
                return i
        return -1