class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = [x * x for x in nums]
        squares.sort()

        positive = (len(nums) + 1) // 2

        return sum(squares[-positive:]) - sum(squares[:-positive])