class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        result = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with nums[i]
            r = num % k
            new_dp[r] += 1

            # Extend previous subarrays
            for rem in range(k):
                new_rem = (rem * num) % k
                new_dp[new_rem] += dp[rem]

            dp = new_dp

            # Add all subarrays ending here to answer
            for rem in range(k):
                result[rem] += dp[rem]

        return result