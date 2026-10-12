class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        min_price = nums[0]
        profit = 0

        for price in nums:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit