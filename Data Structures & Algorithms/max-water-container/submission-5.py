class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            if (r - l) * (min(heights[l], heights[r])) > res:
                res = (r - l) * (min(heights[l], heights[r]))
            
            if heights[l] > heights[r]:
                r = r - 1
            else:
                l = l + 1
        
        return res

        