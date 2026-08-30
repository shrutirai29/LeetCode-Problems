class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        left = min(mn, mx)
        right = max(mn, mx)

        from_front = right + 1
        from_back = n - left
        from_both = (left + 1) + (n - right)

        return min(from_front, from_back, from_both)