class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        for num in nums:
            if num not in mySet: 
                mySet.add(num)

        res= 0
        for num in nums:
            i = 1
            while(num + i) in mySet:
                i += 1
            res = max(res, i)
        
        return res

        

        
        