class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = 0
        arr = []
        if nums is None or len(nums) ==0:
            return []
        nums.sort()
        set_add = set()
        
        for i, num in enumerate(nums):
            if num >0:
                break
            r = len(nums)-1
            m = i+1
            
            while m<r:
                add = nums[m]+nums[r]+num
                if add == 0:
                    temp_arr = [num, nums[m], nums[r]]
                    temp_set = (num, nums[m], nums[r])
                    
                    if temp_set not in set_add:
                        arr.append(temp_arr) 
                        set_add.add(temp_set)

                    r -=1
                    m +=1
                else:
                    if add > 0:
                        r -= 1
                    else:
                        m += 1

        return arr