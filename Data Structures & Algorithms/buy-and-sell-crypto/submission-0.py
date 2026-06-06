class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0
        for i, r in enumerate(prices):
            if (prices[i] - prices[l]) <= 0:
                l = i
            else:
                if prices[i] - prices[l] > ans:
                    ans = prices[i] - prices[l]
        
        return ans
        