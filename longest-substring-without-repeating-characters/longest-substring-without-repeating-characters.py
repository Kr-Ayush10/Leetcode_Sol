class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

	  
        n = len(s)
        if n < 2:
            return n
		
        location = dict()
		
        i, m = -1, 1
        for j in range(n):
		   
            if s[j] in location:
                i = max(location[s[j]], i)
            location[s[j]] = j
            m = max(j-i, m)
        return m
        