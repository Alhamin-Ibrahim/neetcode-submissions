class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, num in enumerate(nums):
            if num in myMap:
                return [myMap[num],i]
            else:
                myMap[target - num] = i