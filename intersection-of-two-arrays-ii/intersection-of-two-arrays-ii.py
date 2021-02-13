class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        n1 = len(nums1)
        n2 = len(nums2)
        nums1_s = sorted(nums1)
        nums2_s = sorted(nums2)
        res = []
        
        while i < n1 and j < n2:
            if nums1_s[i] < nums2_s[j]:
                i += 1
            elif nums1_s[i] > nums2_s[j]:
                j += 1
            else:
                res.append(nums1_s[i])
                i += 1
                j += 1
                
        return res