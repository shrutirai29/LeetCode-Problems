class Solution:
    def uniformArray(self, nums1):
        mn = min(nums1)

        # If the minimum is odd, every even number can subtract it
        if mn % 2 == 1:
            return True

        # If the minimum is even, all numbers must already be even
        return all(num % 2 == 0 for num in nums1)