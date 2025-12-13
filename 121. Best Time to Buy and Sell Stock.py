class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Prices[2] = price of stock on day 2.
        # Goal: Find a number earlier in the list that is lower than a future day in the list
        # If descending array, return 0
        # Find lowest number, and highest number, IF low is before high
        
        lowest_so_far = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            # Current day price
            today = prices[i] 

            if today < lowest_so_far:
                lowest_so_far = today
            else:
                profit_if_sell_today = today - lowest_so_far

                if profit_if_sell_today > max_profit:
                    max_profit = profit_if_sell_today

        return max_profit
