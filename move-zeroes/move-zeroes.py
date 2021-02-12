class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.       
        write_non_zero = 0
        [0, 1, 0, 3, 12]
         w
           num 
        [1, 1, 0, 3, 12]
            w
                  num
        [1, 3, 0, 3, 12]
               w
                     num
        [1, 3, 12, 3, 12]
                  w  num
        # Once the num pointer reached the end.
        non_zero pointer need fill the rest of the array with zero.
        [1, 3, 12, 0, 0]
        """
        write_non_zero = 0
        # num pointer find non_zero element and notice the non_zero pointer to write it down.
        for num in nums:
            if num != 0:
                nums[write_non_zero] = num
                write_non_zero += 1
        # Once the num pointer reached the end.
        # non_zero pointer need fill the rest of the array with zero.
        for i in range(write_non_zero,len(nums)):
            nums[i] = 0      