from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)

        s = set(nums)
        ans = []

        for i in range(low, high + 1):
            if i not in s:
                ans.append(i)

        return ans