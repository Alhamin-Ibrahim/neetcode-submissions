class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l, r = 0, 0
        ans = 0
        while r < len(s):
            if s[r] in mySet:
                ans = max(ans,r-l)
                mySet.remove(s[l])
                l += 1
            else:
                mySet.add(s[r])
                r += 1
        
        return max(ans,r-l)
            

        