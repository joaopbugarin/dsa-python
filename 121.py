from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #strategy: take the first day and pick the best day to sell it
        #we will go through the array len(array) time
        profit = 0
        min_price = float('inf')
        max_profit = -float('inf')
        for current_price in prices:
            if current_price < min_price:
                min_price = current_price
            profit = current_price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit 
            

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
