class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ans = []
        count = 0

        for num in nums:
            if num != 0:
                ans.append(num)
            else:
                count += 1

        for i in range(count):
            ans.append(0)

        nums[:] = ans
        return nums