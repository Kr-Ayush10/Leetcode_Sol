class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        i,j=0,len(a)-1
        while i<j:
            if a[i]+a[j]<t:
                i+=1
            elif a[i]+a[j]>t:
                j-=1
            else:
                return [i+1,j+1]