class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # total profit


        for i in range(1, len(prices)): # start from day 1 because we compare to day 0
            if prices[i] > prices[i-1]: # if price went up from yesterday to today
                profit += prices[i] - prices[i-1] # buy yesterday, sell today

        return profit

