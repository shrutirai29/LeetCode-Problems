class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n

        while True:
            product = 1
            x = num

            while x > 0:
                product *= x % 10
                x //= 10

            if product % t == 0:
                return num

            num += 1