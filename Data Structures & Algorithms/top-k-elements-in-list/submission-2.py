class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = defaultdict(int)
        for num in nums:
            myMap[num] += 1

        arr = [[] for i in range(len(nums) + 1)]
        print(arr)

        for key, val in myMap.items():
            arr[val].append(key)

        print(arr)
        res = []
        temp = 0
        for i in range(len(arr) - 1, -1, -1):
            if len(arr[i]) == 0:
                continue
            for num in arr[i]:
                if temp != k:
                    res.append(num)
                    temp = temp + 1
                else:
                    return res

        return res

        
        
        