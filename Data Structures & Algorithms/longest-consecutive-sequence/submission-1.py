class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        for num in nums:
            if num not in mySet: 
                mySet.add(num)

        res, c = 0, 1
        for num in nums:
            i = 1
            order = 1
            while(num + i) in mySet:
                print (order, num + i)
                order += 1
                i += 1
                c += 1
            if c > res:
                print("res", c)
                res = c
                c = 1
            else:
                c = 1
        
        return res

        

        
        