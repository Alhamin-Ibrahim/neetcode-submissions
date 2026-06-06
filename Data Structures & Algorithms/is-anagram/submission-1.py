class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for char in s:
            if char in sMap:
                sMap[char] = sMap[char] + 1
            else:
                sMap[char] = 1
        for char in t:
            if char in tMap:
                tMap[char] = tMap[char] + 1
            else:
                tMap[char] = 1
        if len(sMap) > len(tMap):
            for key in sMap:
                if key not in tMap:
                    return False
                elif(sMap[key] != tMap[key]):
                    return False 
        else:
            for key in tMap:
                if key not in sMap:
                    return False
                elif(sMap[key] != tMap[key]):
                    return False 
        return True



        