class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        i, val = 0, 1
        for i in range(len(nums)):
            val = val * nums[i]
            left[i] = val

        i, val = len(nums) - 1, 1
        for i in range(i, -1, -1):
            val = val * nums[i]
            right[i] = val
        
        length = len(nums)
        for i in range(len(nums)):
            if i - 1 < 0:
                nums[i] = right[i + 1]
            elif i + 1 >= length:
                nums[i] = left[i - 1]
            else:
                nums[i] = left[i - 1] * right[i + 1]
        
        return nums
        


        