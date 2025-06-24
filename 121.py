class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #strategy: take the first day and pick the best day to sell it
        #evaluate the profit. move to the next day.
        #if the best day has a best match, we change it.
        #we will go through the array len(array) times

