class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMap = {}
        for word in s:
            if word in myMap:
                myMap[word] += 1
            else:
                myMap[word] = 1
        myMap2 = {}
        for word in t:
            if word in myMap2:
                myMap2[word] += 1
            else:
                myMap2[word] = 1
        if len(s) > len(t):
            for char in s:
                if char in myMap and char in myMap2:
                    if myMap[char] != myMap2[char]:
                        return False
                else:
                    return False
        else:
            for char in t:
                if char in myMap and char in myMap2:
                    if myMap[char] != myMap2[char]:
                        return False
                else:
                    return False
        return True
        
        