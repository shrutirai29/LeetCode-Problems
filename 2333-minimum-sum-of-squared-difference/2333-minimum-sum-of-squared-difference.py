class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        max_diff = max(diff)

        if sum(diff) <= k:
            return 0

        freq = [0] * (max_diff + 1)

        for d in diff:
            freq[d] += 1

        for d in range(max_diff, 0, -1):
            if k == 0:
                break

            count = freq[d]

            if k >= count:
                freq[d] -= count
                freq[d - 1] += count
                k -= count
            else:
                freq[d] -= k
                freq[d - 1] += k
                k = 0

        ans = 0

        for d in range(max_diff + 1):
            ans += freq[d] * d * d

        return ans