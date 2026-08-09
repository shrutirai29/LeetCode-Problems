class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # starting from index i with M
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, M):
            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                next_i = i + X
                next_M = max(M, X)

                # Stones remaining after we take X
                # minus what opponent can get
                current = suffix[i] - dp(next_i, next_M)

                best = max(best, current)

            return best

        return dp(0, 1)