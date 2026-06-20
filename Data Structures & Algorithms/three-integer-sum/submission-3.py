class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        myset = set()

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r = r - 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l = l + 1
                else:
                    if tuple([nums[i],nums[l],nums[r]]) not in myset:
                        myset.add(tuple([nums[i],nums[l],nums[r]]))
                    l, r = l + 1, r - 1
                

        return [list(i) for i in myset]