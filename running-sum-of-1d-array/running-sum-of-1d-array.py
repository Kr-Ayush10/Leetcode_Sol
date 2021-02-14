class Solution(object):
    def runningSum(self, nums):
        stack=[]
        sum=0
        for i in nums:
            sum+=i
            stack.append(sum)
        return stack