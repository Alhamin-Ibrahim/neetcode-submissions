class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = num + 1
        counter = 0;
        for num in nums:
            temp = num
            temp1 = 0
            while num in map:
                num = num + 1
                temp1 = temp1 + 1
            if counter < temp1:
                counter = temp1
        return counter
        
        