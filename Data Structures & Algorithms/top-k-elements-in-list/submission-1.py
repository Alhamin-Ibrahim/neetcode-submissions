class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = []
        myMap = {}
        for i in range(len(nums)):
            if(nums[i] in myMap):
                myMap[nums[i]] += 1
            else:
                myMap[nums[i]] = 1
        temp = 0
        while temp < k:
            max_key = max(myMap, key=myMap.get)
            array.append(max_key);
            del myMap[max_key]
            temp += 1

        return array

        