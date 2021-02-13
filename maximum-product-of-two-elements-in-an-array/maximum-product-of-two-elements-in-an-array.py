class Solution:
    def maxProduct(self, nums):
        a, b = float('-inf'), float('-inf')
        for x in nums:
            if x>a:
                a, b = x, a
            elif x>b:
                b = x
        return (a-1)*(b-1)