class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0

            # Inclusion-exclusion
            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        curr_lcm = lcm(curr_lcm, coins[i])

                        if curr_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                multiples = x // curr_lcm

                if bits % 2 == 1:
                    ans += multiples
                else:
                    ans -= multiples

            return ans

        # Binary search for the smallest x
        # such that at least k valid amounts <= x
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left