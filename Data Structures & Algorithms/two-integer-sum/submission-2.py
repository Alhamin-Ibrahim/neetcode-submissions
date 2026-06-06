class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        i = 0
        for num in nums:
            map[target - num] = i
            i += 1
        j = 0
        for num in nums:
            if num in map and j != map[num]:
                return [j, map[num]]
            j += 1
            
        