class Solution:
    def minSwaps(self, nums: list[int]) -> int:

        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        n = len(nums)

        # Target sorted array
        target = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map number -> its original index
        index = {nums[i]: i for i in range(n)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or nums[i] == target[i]:
                visited[i] = True
                continue

            # Find cycle
            cycle_len = 0
            j = i

            while not visited[j]:
                visited[j] = True
                cycle_len += 1

                # Where target[j] currently exists
                j = index[target[j]]

            swaps += cycle_len - 1

        return swaps