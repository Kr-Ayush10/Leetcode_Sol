class Solution:
    def removeDuplicates(self, num: 'List[int]') -> 'int':
        for i in range(len(num)-1, 0, -1):
            if num[i] == num[i-1]:
                del num[i]
        return len(num)