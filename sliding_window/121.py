class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices [left] < prices[right]:
                diff = prices[right]-prices[left]
                maxx = max(maxx,diff)
            else:
                left = right
            right += 1
        return maxx

sol = Solution()
print(sol.maxProfit([1,2,5,0,]))