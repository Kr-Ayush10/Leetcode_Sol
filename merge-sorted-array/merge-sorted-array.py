class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            #comparing the last element and replacing the value in num1 by value of nums2 or nums1 after each comparision 
            if nums1[m-1]<nums2[n-1]:
                nums1[m+n-1]=nums2[n-1]
                n-=1
            else:
                nums1[m+n-1]=nums1[m-1]
                m-=1
        # in case nums1 is null or 0 we replace its values and put nums2 values
        nums1[:n]=nums2[:n]
        return nums1  