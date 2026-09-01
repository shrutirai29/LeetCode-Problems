from typing import List


class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        n = len(nums)

        # Store (value, original_index) and sort by value
        arr = sorted((value, index) for index, value in enumerate(nums))

        start = 0

        while start < n:
            end = start

            # Find all elements belonging to the same group
            while (
                end + 1 < n
                and arr[end + 1][0] - arr[end][0] <= limit
            ):
                end += 1

            # Get values and their original indices
            values = []
            indices = []

            for i in range(start, end + 1):
                values.append(arr[i][0])
                indices.append(arr[i][1])

            # Put smallest values at smallest indices
            indices.sort()

            for i in range(len(indices)):
                nums[indices[i]] = values[i]

            start = end + 1

        return nums