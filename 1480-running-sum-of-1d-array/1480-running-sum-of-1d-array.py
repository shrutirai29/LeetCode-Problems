class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        add = 0
        for num in nums:
            add = add + num
            result.append(add)

        return result